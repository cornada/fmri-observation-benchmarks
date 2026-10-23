# Matched static and dispersion forecasting

Manuscript: Windowed Connectivity Variability for Two-Year Clinical Severity Prediction in Mild Cognitive Impairment.

The package compares clinical-only, clinical + static FC, clinical + windowed dispersion, and clinical + both features on identical participant folds. Every scaler, categorical vocabulary, PLS projection and ridge fit uses training rows only. Three inner folds select 2, 5 or 10 PLS components and ridge penalty 0.1, 1, 10 or 100. Five outer folds are repeated for three saved seeds.

```sh
python papers/04_mci_forecast/run.py --output results/forecast_demo.json
python papers/04_mci_forecast/run.py --mode summary --output results/forecast_aggregates.json
```

The default input is the 48-row **synthetic software fixture**, not the 48-person clinical panel. Saved human aggregate MAEs are in `data/aggregate_results.json`. The output provides each representation's MAE by repetition and selected settings; the repetitions reuse rows and are not independent cohorts.

## Local input and split plan

Supply a pickle-free NPZ with `target` (N,), `static` (N,21), `dispersion` (N,21), `clinical_numeric` (N,C), and Unicode `categories` (N,K). Empty categorical matrices may have shape (N,0). Optional `participant_ids` must be unique. Use one row per person. A JSON split plan has one object per outer fold: `seed`, `fold`, `train`, `test`, and `inner` (a list of `train`/`test` row-index partitions of the outer training set). The runner validates non-overlap and complete coverage.

```sh
python papers/04_mci_forecast/run.py --input local_features.npz --splits local_splits.json --output results/local_forecast.json
```

The included row-index plan is the historical 48-row plan without participant identities. To reproduce the human result, authorized users need its corresponding local participant-order manifest and clinical/feature arrays.

## Measurement helpers

`features.extract(timeseries, tr_seconds)` takes an already prepared N × 7 M24 residual field. Static FC uses all 21 upper-triangle Pearson correlations. Window width is `max(8, round(60/TR))`, stride `max(1, round(30/TR))`; dispersion is the sample SD of window correlations (`ddof=1`). Combined features concatenate static and dispersion into one 42-coordinate block. `fc_windows.py` and `connectivity.py` also expose the finite-window geometry and common-phase controls. Correlations are not Fisher-transformed. Image preprocessing and clinical target construction precede this interface.
