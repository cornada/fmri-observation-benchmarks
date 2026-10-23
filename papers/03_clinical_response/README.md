# Paired nuisance-regression response

Manuscript: Clinical Associations of Nuisance-Regression Responses in Joint fMRI Representations.

This package exposes the measurement: joint orthogonal projection, fixed seven-network aggregation, the leading-two energy fraction of a channel-major length-10 delay matrix, and excess above 199 independent-channel phase references. `paired.py` adds a shared set of saved cosine columns to both nuisance designs. `mechanisms.py` provides the five observation/proxy worlds; `lag_control.py` provides delayed Gaussian coupling with independent prehistory.

```sh
python papers/03_clinical_response/run.py --output results/paired_demo.json
python papers/03_clinical_response/run.py --mode summary --output results/paired_aggregates.json
```

The example runs two mechanism settings and three lag-coupling settings. Complete clinical, 800-condition mechanism and delayed-coupling aggregate results are supplied in `data/`. The code produces a paired measurement; participant-level clinical fitting is outside this release.

## Local input

An NPZ passed with `--input` must contain these arrays on the **same retained frames**:

| Array | Shape | Meaning |
|---|---|---|
| `parcels` | N × 400 | Prepared parcel series |
| `motion24` | N × 24 | The fixed 24 motion columns |
| `a5` | N × 5 | Five already selected anatomical nuisance columns |
| `cosines` | N × K | Original saved cosine columns; K=0 omits common DCT |
| `membership` | 400 | Integer network assignments 0-6, all represented |

```sh
python papers/03_clinical_response/run.py --input local_parcels.npz --output results/local_pair.json
```

Both designs include an intercept and trend; nuisance columns enter one joint projector. Network fields are centered and scaled to unit RMS before delay construction. Output `delta_J` is **A5 minus BASE**, in fractional units; multiply by 100 for percentage points. The local example shares phase seeds across the two branches to expose the paired measurement. The historical human analyses used their saved branch-specific phase seeds, so this example is not a replay of clinical bootstrap estimates.

The paper's positive paired severity coefficient and common-DCT sensitivity are retained in `aggregate_results.json`. Reusing the measurement in a new clinical study requires that study's participant protocol and clinical model; restricted ADNI participant records are not redistributed.
