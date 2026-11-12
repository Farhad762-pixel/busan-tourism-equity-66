# Accessibility sensitivity experiment

The project tested equity-aware ranking with Haversine **straight-line distance** eligibility around approximate Busan Station, Seomyeon Station and Haeundae Station. It did **not** measure subway/bus driving or walking travel times.

**Published in this organization stage:** [15 km policy summary](results/accessibility_15km_summary.csv).

The prepared ZIP contains the full `run_accessibility_experiment.py`, 5 distance caps per origin, source CSV tables, figure and report. These are pending further safe synchronization into GitHub.

**Interpretation:** The number of eligible queries depends on each origin/limit; compare baseline and equity on the same eligible set **within** each origin, not between different origins as though they were identical samples.

**Next:** Add route-based duration data once valid, use the same constraints for all compared policies, and obtain human-rated attraction relevance.
