# Temporal surrogates and finite descriptors

Manuscript: Temporal Structure in Resting-State fMRI Under Marginal and Cross-Spectral Surrogate Controls.

`surrogates.py` provides sample entropy with common two-/three-template starts, finite MFDFA and Higuchi curve shapes, 25- and 250-iteration IAAFT, and multichannel common-phase references. The generators retain their study constants. Unsupported measurements remain explicit; they are not replaced with zero.

```sh
python papers/02_temporal_surrogates/run.py --output results/surrogates.json
python papers/02_temporal_surrogates/run.py --mode summary --output results/surrogate_aggregates.json
```

The example uses a saved-generator Gaussian process on 197 samples. It evaluates seven channels, 20 references per family and IAAFT applied to a fixed IAAFT output as a pseudo-observation. It records descriptor ranks and actual constraint errors. The example is a compact calibration demonstration; full paper readouts are in `data/`.

For local data, supply an NPZ containing finite `timeseries` with shape **samples × 7**:

```sh
python papers/02_temporal_surrogates/run.py --input local_networks.npz --output results/local_surrogates.json
```

The study's human observation surface averages equally weighted Schaefer parcels into seven networks after removal of leading non-steady-state frames, before nuisance regression. Preserve native TR and retained support when interpreting the sample-domain scales.

## Saved results and reuse

`observation_support_ranks.csv` contains all 1,280 synthetic conditions: 32 process seeds × ten sample/TR cells × four observation branches. Within each condition it retains all seven networks, three descriptor families and three reference families. A blank rank denotes unsupported measurement support. Reuse `latent_paths`, `cells`, `observation`, `iaaft_pair` and `phase_draw` to regenerate inputs and references. `iaaft_aggregate.json`, `iaaft_calibration_aggregate.json` and `common_phase_aggregate.json` retain the human aggregate comparisons.

IAAFT exactly retains the sorted samples but only approximates Fourier amplitudes at its fixed iteration budget. Common-phase references retain the full discrete complex cross-spectrum and full-record FC, while their marginal distributions can change. A rank of 1 among 21 objects is a finite reference-family comparison; the algorithm-on-algorithm readout should be considered when interpreting it.
