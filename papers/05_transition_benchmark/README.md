# Conditional HMM/VAR transition benchmark

Manuscript: Evaluating State-Transition Models in Short Resting-State fMRI with Continuous-Dynamics Controls.

The full synthetic release contains 216 latent realizations and four observation branches per realization (**864 conditions**). Worlds are cyclic/reversible three-state generators at two amplitudes, a common-factor AR process and a rotating AR process. Each condition has eight HMM and eight VAR candidates: **13,824 saved fits**.

```sh
# Two-candidate executable example, compared with saved scores:
python papers/05_transition_benchmark/run.py --output results/transition_demo.json
# The complete 64-candidate menu for one latent realization and its four branches:
python papers/05_transition_benchmark/run.py --mode case --case cyclic_N97_A1.0_S101 --output results/transition_case.json
# All saved condition-level readouts, without refitting:
python papers/05_transition_benchmark/run.py --mode summary --output results/transition_results.json
```

The runner reports exact generator replay and maximum score difference from the saved candidate table. Small platform-dependent floating-point differences can occur. `--case` selects any ID in `data/config.json`; `--branch` selects the observation branch for the small example. Running `--mode case` for every production case reconstructs the complete fit grid and takes substantially longer than the quick example.

## Arrays and tables

`synthetic_216_cases.npz` is pickle-free. Keys are `<case_id>__latent`, `<case_id>__hidden_state` for discrete worlds, and `<case_id>__<branch>` for `identity`, `stationary_filter`, `filter_change_at_test` and `unit_change`. Fields have shape N × 7. Hidden states have length N and labels 0-2. `config.json` fixes lengths, seeds, means, transitions, observation filters and candidate menus.

`candidate_scores.csv` includes validation/test log density in nats per frame, selected flags and HMM flux for all fits. `readout.json` contains the 864 condition rows and paired cyclic/reversible flux comparisons. The four branches share their latent realization and are not independent draws.

## Scoring contract

Training ends at `int(.6*N)` and validation at `int(.8*N)`. Models and observation-transform parameters fit training data only. Validation chooses candidates; the test score conditions on all available past observations. HMM filtering state is carried across boundaries. VAR uses the same history convention. Scores include the inverse-filter and training-standardization Jacobians in the original observation units. The source-defined HMM fit uses 20 EM iterations; the released VAR evaluator preserves the study's 50-decimal-digit calculation. Candidate failure is visible as an exception in the public runner.

The true-generator labels support model-comparison research. HMM flux is a fitted-model statistic; the continuous worlds supply controls against interpreting it as direct evidence of discrete physiological states. No human time series are included.
