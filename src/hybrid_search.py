"""Experimental source-evidence-aware search for the 207 Busan attraction records.

This is NOT the archived TF-IDF economic re-ranking experiment. It does not
estimate economic undercapture or claim independently validated relevance.
"""
import csv
import re
from functools import lru_cache
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FIELDS = ("place", "subtitle", "main_title")
# Conservative, inspectable semantic families rather than generated descriptions.
FAMILIES = {
    "coast": r"\b(sea|seaside|ocean|coast|coastal|beach|shore|shoreline|maritime|waterfront|waterside|harbor|harbour)\b",
    "walk": r"\b(walk|walking|trail|stroll|promenade|path|pedestrian|alley|alleys|staircase|stairway)\b",
    "forest": r"\b(forest|wooded|woods|bamboo)\b",
    "mountain": r"\b(mountain|hill|hillside|peak)\b",
    "garden": r"\b(garden|gardens|arboretum|botanical|botanic|flowers|flower|wildflower|rose)\b",
    "museum": r"\b(museum|exhibit|exhibition|gallery|galleries|memorial hall|science center)\b",
    "history": r"\b(history|historical|historic|heritage|fortress|monument|memorial|past|traditional|old)\b",
    "temple": r"\b(temple|monastery|buddhist|shrine|sacred)\b",
    "market": r"\b(market|markets|shopping|vendors|stalls)\b",
    "cafe": r"\b(cafe|café|coffee|tea house|teahouse|bakery|brunch)\b",
    "village": r"\b(village|neighborhood|neighbourhood|hamlet)\b",
    "art": r"\b(art|arts|mural|murals|painted|gallery|creative)\b",
    "scenic": r"\b(view|scenic|scenery|panorama|observatory|overlook|skywalk|sunset|sunrise|skyline)\b",
    "night": r"\b(night|nighttime|evening|starlight|stars|illuminated|city lights)\b",
    "family": r"\b(family|children|child|kids|playground|interactive|theme park)\b",
    "science": r"\b(science|scientific|mathematics|discovery)\b",
    "bridge": r"\bbridge\b",
}
REQUIREMENTS = [
    ("beach", r"\b(beach|beaches|sandy)\b", r"\b(beach|beaches|sandy)\b"),
    ("coast/waterfront", r"\b(coast|coastal|sea|seaside|ocean|shore|shoreline|waterfront|waterside|harbor|harbour)\b", r"\b(coast|coastal|sea|seaside|ocean|shore|shoreline|waterfront|waterside|maritime|harbor|harbour|beach)\b"),
    ("walking route", r"\b(walk|walking|trail|stroll|promenade|pedestrian|paths?|staircase|stairway)\b", r"\b(walk|walking|trail|stroll|promenade|pedestrian|paths?|alley|staircase|stairway)\b"),
    ("forest", r"\b(forest|wooded|woods)\b", r"\b(forest|woods|wooded|bamboo)\b"),
    ("mountain", r"\b(mountain|hillside|hilltop)\b", r"\b(mountain|hill|hillside|peak)\b"),
    ("garden", r"\b(garden|gardens|botanical|botanic|flowers|wildflowers)\b", r"\b(garden|gardens|arboretum|botanical|botanic|flowers|wildflower|flower|rose)\b"),
    ("museum/exhibition", r"\b(museum|exhibits?|exhibitions?|galler(y|ies))\b", r"\b(museum|exhibit|exhibition|gallery|galleries|memorial hall|science center)\b"),
    ("history", r"\b(history|historical|historic|heritage|fortress|monument|ancient|old korean)\b", r"\b(history|historical|historic|heritage|fortress|monument|memorial|past|war|traditional|old)\b"),
    ("temple/sacred", r"\b(buddhist|monastery|temple|shrine|sacred)\b", r"\b(temple|monastery|buddhist|shrine|sacred)\b"),
    ("market", r"\b(market|stalls?|vendors?|street snacks|produce shopping|shopping lanes)\b", r"\b(market|markets|shopping|stalls|vendors)\b"),
    ("cafe", r"\b(cafe|café|coffee|teahouse|tea house|bakery|brunch)\b", r"\b(cafe|café|coffee shop|book cafe|tea house|teahouse|bakery|brunch)\b"),
    ("village", r"\b(village|neighborhood|neighbourhood)\b", r"\b(village|neighborhood|neighbourhood|hamlet)\b"),
    ("bridge", r"\bbridge\b", r"\bbridge\b"),
    ("street art", r"\b(murals?|painted houses)\b", r"\b(mural|murals|painted houses|street art)\b"),
    ("nighttime", r"\b(night|nighttime|evening|after dark|illuminated|city lights)\b", r"\b(night|nighttime|evening|starlight|stars|illuminated|city lights)\b"),
    ("science", r"\b(science|scientific|discovery gallery)\b", r"\b(science|scientific|mathematics|science museum)\b"),
    ("children/family", r"\b(kids?|children|child friendly|family friendly)\b", r"\b(children|kids|child|family|playground|theme park)\b"),
    ("maritime", r"\b(naval|maritime)\b", r"\b(naval|maritime|marine|ships?|fisheries)\b"),
    ("cliffs", r"\bcliffs?\b", r"\bcliffs?\b"),
    ("swimming", r"\bswimming?\b", r"\bswimming?\b"),
    ("fortress", r"\bfortress\b", r"\bfortress\b"),
    ("art studio", r"\bstudios?\b", r"\bstudios?\b"),
    ("painted houses", r"\bpainted houses\b", r"\bpainted houses\b"),
    ("wildlife", r"\b(wildlife|animals?)\b", r"\b(wildlife|animals?|aquarium|marine life)\b"),
    ("fish/seafood stalls", r"\b(fish stalls?|seafood)\b", r"\b(fish stalls?|seafood|fish market)\b"),
    ("street snacks", r"\b(street snacks?|vendors?)\b", r"\b(street snacks?|vendors?|food stalls?)\b"),
    ("produce", r"\bproduce\b", r"\bproduce\b"),
    ("meditation", r"\bmeditation\b", r"\bmeditation\b"),
    ("tea house", r"\btea house\b", r"\btea house\b"),
    ("bakery/brunch", r"\b(bakery|brunch)\b", r"\b(bakery|brunch)\b"),
    ("illuminated", r"\billuminat", r"\billuminat"),
    ("staircase", r"\b(staircase|stairway)\b", r"\b(staircase|stairway)\b"),
    ("harbor", r"\b(harbor|harbour)\b", r"\b(harbor|harbour|port)\b"),
    ("sunset", r"\bsunset\b", r"\bsunset\b"),
    ("alley", r"\b(alleys|alley)\b", r"\b(alleys|alley)\b"),
]


def _normalize(value):
    return re.sub(r"\s+", " ", str(value or "").casefold()).strip()


def _source_text(row):
    pieces = []
    for field in FIELDS:
        s = str(row.get(field) or "")
        s = re.sub(r"\b(photographed by|photography by|written and photographed by|written and illustrated by)\b.*", "", s, flags=re.I)
        pieces.append(s)
    return _normalize(" ".join(pieces))


def _families(s):
    found = {key for key, pattern in FAMILIES.items() if re.search(pattern, s, re.I)}
    if "museum" in found and "cafe" in found and not re.search(r"\b(cafe|café|coffee shop|tea house|bakery)\b", s):
        found.remove("cafe")
    return found


class HybridRetriever:
    def __init__(self, attractions):
        self.rows = list(attractions)
        self.cores = [_source_text(row) for row in self.rows]
        self.tags = [_families(text) for text in self.cores]
        documents = [core + " " + " ".join(sorted(tags)) for core, tags in zip(self.cores, self.tags)]
        self.word = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), sublinear_tf=True, strip_accents="unicode")
        self.char = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)
        self.words = self.word.fit_transform(documents)
        self.chars = self.char.fit_transform(documents)

    def search(self, query, limit=10):
        if not query or not query.strip() or not 1 <= limit <= 30:
            raise ValueError("Use a nonblank query and limit 1..30")
        q = _normalize(query)
        qtags = _families(q)
        requirements = [(label, re.compile(evidence, re.I)) for label, rule, evidence in REQUIREMENTS
                        if re.search(rule, q, re.I)]
        enriched = q + " " + " ".join(sorted(qtags))
        ws = cosine_similarity(self.word.transform([enriched]), self.words)[0]
        cs = cosine_similarity(self.char.transform([enriched]), self.chars)[0]
        strict, related = [], []
        for i, row in enumerate(self.rows):
            overlap = sorted(qtags & self.tags[i])
            if not overlap and ws[i] < 0.065:
                continue
            score = 0.65 * float(ws[i]) + 0.25 * float(cs[i]) + 0.10 * len(overlap) / max(1, len(qtags))
            if score < 0.045:
                continue
            missing = [label for label, pattern in requirements if not pattern.search(self.cores[i])]
            hit = {"attraction_id": str(row.get("uc_seq") or i),
                   "place": str(row.get("place") or row.get("main_title") or ""),
                   "district": str(row.get("district") or ""),
                   "score": round(score, 7), "matched_concepts": overlap,
                   "source_excerpt": self.cores[i][:180]}
            if not missing:
                strict.append(hit)
            elif overlap:
                related.append((len(missing), -score, hit, missing))
        strict.sort(key=lambda h: (-h["score"], h["attraction_id"]))
        related.sort(key=lambda x: (x[0], x[1], x[2]["attraction_id"]))
        return {"query": query, "supported": strict[:limit],
                "related_unverified": [{"hit": hit, "missing_evidence": missing}
                                       for _, _, hit, missing in related[:limit]],
                "required_evidence": [label for label, _ in requirements],
                "note": "Source-text support only. Missing metadata is not proof an activity is impossible; human relevance not evaluated.",
                "economic_score_used": False}


def load_catalog(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))
