# Personal response transfer

Manuscript: Personalized Prediction of Preprocessing Responses Across Longitudinal fMRI Visits.

The model learns four coefficients shared across FC edges. It predicts the third visit's FA-minus-BASE response from that visit's BASE FC and the first two visits' A, F and AF responses. `response.py` implements the four-coefficient fit, complete-participant holdout, repeated-BASE control and early agreement. `participant_operator_atlas_complete.py` provides the seven original controls and participant-specific control envelope.

From the repository root, after installation:

```sh
python papers/01_response_transfer/run.py --output results/response_demo.json
python papers/01_response_transfer/run.py --mode msc --output results/msc_transfer.json
```

The second command needs `data/msc_sessions123.npz`, supplied in the **paper-01 ZIP** or as a separate [release asset](https://github.com/cornada/fmri-observation-benchmarks/releases/download/v1.0.0/msc_sessions123.npz). Place the separate asset in this folder's `data/` directory. It contains the unchanged float64 prepared MSC fields for sessions 1-3. No fitting on MSC occurs. The fixed personal-model mean MSE is about **0.00433179**, versus **0.00457413** for fixed repeated BASE and **0.00476962** for fixed ADNI mean history; `msc_expected.json` contains full precision and per-MSC-row results. The run reports the difference from saved means.

## Input conventions

`responses` has axes **participant × visit × node × edge**. Nodes are `BASE, A, F, AF, FA`; FC coordinates are the 79,800 entries selected by `np.tril_indices(400, -1)`. Values are Pearson correlations, not Fisher z scores. The released MSC array is `(10, 3, 5, 79800)` in MSC01-MSC10 order and session order 1-3.

BASE is the motion-24 residual field. A removes the effective five-component anatomical nuisance subspace recovered from the baseline/joint-regression difference. F is the finite-record DCT-II high-pass projection at 0.01 Hz. AF means F(A(BASE)); FA means A(F(BASE)). The effective A basis is held fixed when applied after F. The prediction target is a processing response, not an unavailable future scan: the target scan's BASE FC is an input.

For your own already measured fields, pass an NPZ with `responses`, a finite participant-by-feature `reliability` array and a finite participant-by-feature `design` array:

```sh
python papers/01_response_transfer/run.py --input local_fields.npz --output results/local_response.json
```

The latter arrays are explicit control inputs, not features learned from target outcomes. The default demonstration fills them synthetically. Reliability and operator-design construction for a new study must be specified with that study's measurement protocol.

## Included results

`adni_aggregate.json` retains the original seven-control comparison. `fixed_coefficients.json` contains the personal4 and base3 coefficient vectors; the two NPY files contain population means with no participant axis. The MSC source is CC0; see the root data-license file. MSC had been used during programme development, so this example reproduces transport with fixed coefficients rather than claiming a new untouched validation cohort.
