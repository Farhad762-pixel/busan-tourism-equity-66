"""Build figures from existing attraction counts and archived summary tables.

These figures do not constitute a rerun of the archived economic experiment.
"""

import csv
from collections import Counter
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "work/.matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / "work/.cache"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = ROOT / "results/figures"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "svg.hashsalt": "busan-research-audit"})
    with (ROOT / "data/processed/busan_attractions.csv").open(encoding="utf-8-sig", newline="") as handle:
        counts = Counter(row["district"] for row in csv.DictReader(handle))
    pairs = sorted(counts.items(), key=lambda item: (item[1], item[0]))
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained")
    bars = ax.barh([p[0] for p in pairs], [p[1] for p in pairs], color="#24788a")
    ax.bar_label(bars, padding=3)
    ax.set(xlabel="Attractions in repository snapshot (count)", xlim=(0, 25),
           title="207 official attractions across 16 Busan districts")
    fig.savefig(OUT / "attraction_distribution.svg", metadata={"Date": None})
    plt.close(fig)

    with (ROOT / "experiments/equity/results/rq3_policy_summary.csv").open(newline="") as handle:
        policies = list(csv.DictReader(handle))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    labels = [r["lambda"] for r in policies]
    axes[0].bar(labels, [100*float(r["undercapture_exposure"]) for r in policies], color="#24788a")
    axes[0].set(ylabel="Undercapture exposure (%)", ylim=(0, 100), xlabel="Lambda")
    axes[1].plot(labels, [100*float(r["relevance_retained"]) for r in policies], marker="o", color="#9a5426")
    axes[1].axhline(99, linestyle="--", color="gray", label="Reported 99% policy threshold")
    axes[1].set(ylabel="TF-IDF relevance retained (%)", ylim=(90, 101), xlabel="Lambda")
    axes[1].legend(fontsize=8)
    fig.suptitle("Archived RQ3 summary — arithmetic checked; full rerun pending")
    fig.savefig(OUT / "archived_policy_summary.svg", metadata={"Date": None})
    plt.close(fig)
    print(f"Wrote figures to {OUT}")


if __name__ == "__main__":
    main()
