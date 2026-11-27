"""Synthetic tests: these do NOT establish real tourist relevance."""
import unittest
from src.hybrid_search import HybridRetriever

ROWS = [
 {"uc_seq": 1, "place": "Coastal Walking Trail", "district": "Seo-gu",
  "subtitle": "Walk along the coast with an ocean view"},
 {"uc_seq": 2, "place": "Coffee Museum", "district": "Busanjin-gu",
  "subtitle": "A museum about coffee beans"},
 {"uc_seq": 3, "place": "Book Cafe", "district": "Dong-gu",
  "subtitle": "Relax in a quiet cafe"},
 {"uc_seq": 4, "place": "Town Market", "district": "Yeongdo-gu",
  "subtitle": "A traditional shopping market"},
 {"uc_seq": 5, "place": "Busan Botanical Garden", "district": "Buk-gu",
  "subtitle": "An arboretum and flower garden"},
]

class HybridSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.retriever = HybridRetriever(ROWS)

    def test_seaside_walk_supported(self):
        r = self.retriever.search("quiet seaside promenade")
        self.assertEqual(r["supported"][0]["attraction_id"], "1")

    def test_coffee_museum_not_cafe(self):
        r = self.retriever.search("quiet cafe")
        self.assertEqual([h["attraction_id"] for h in r["supported"]], ["3"])

    def test_fish_stalls_not_invented(self):
        r = self.retriever.search("fish stalls and fresh seafood")
        self.assertEqual(r["supported"], [])
        self.assertTrue(any("fish/seafood stalls" in v["missing_evidence"]
                            for v in r["related_unverified"]))

    def test_garden_supported(self):
        r = self.retriever.search("botanical flowers and gardens")
        self.assertEqual(r["supported"][0]["attraction_id"], "5")

    def test_night_bridge_not_invented(self):
        r = self.retriever.search("illuminated suspension bridge")
        self.assertEqual(r["supported"], [])

    def test_gibberish(self):
        r = self.retriever.search("zzzxxyyq nosemantics")
        self.assertEqual(r["supported"], [])
        self.assertEqual(r["related_unverified"], [])

if __name__ == "__main__":
    unittest.main()
