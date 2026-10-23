# fMRI observation benchmarks

Code, synthetic data and worked examples accompanying five studies of preprocessing responses and temporal fMRI measurements. Each paper has its own instructions, saved results and command-line entry point. Shared methods live in `src/fmri_observation`.

| Paper | Reusable contribution | Included data |
|---|---|---|
| [1. Personal response transfer](papers/01_response_transfer) | Four-coefficient response prediction, seven controls and fixed-coefficient transfer | Aggregate ADNI coefficients; MSC sessions 1-3 in the release download |
| [2. Temporal surrogates](papers/02_temporal_surrogates) | Sample entropy, finite MFDFA/Higuchi shapes, IAAFT and common-phase controls | Aggregate human results and 1,280 synthetic-condition rank readouts |
| [3. Paired clinical response](papers/03_clinical_response) | Joint nuisance projection, common-DCT comparison, delay concentration and mechanism generators | Aggregate clinical and synthetic-panel results |
| [4. MCI forecasting](papers/04_mci_forecast) | Static/dispersion features and matched nested PLS/ridge prediction | Synthetic fixture, row-index split plan and aggregate MAEs |
| [5. Transition benchmark](papers/05_transition_benchmark) | Discrete/continuous generators and conditional HMM/VAR comparison | All 216 latent realizations, 864 observed conditions and 13,824 candidate scores |

## Install and run

Python 3.11 or newer. The reference environment uses Python 3.14 and the versions in `requirements-repro.txt`.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-repro.txt
python -m pip install --no-deps -e .
python papers/05_transition_benchmark/run.py --output results/transition_demo.json
python -m unittest discover -s tests -v
```

Each `papers/*/run.py` defaults to a small executable example. `--mode summary` reads the saved paper-level results without fitting models. Outputs go to stdout, or to a new path supplied with `--output`. Examples limit numerical thread pools to one thread for reproducibility.

Download the [versioned release](https://github.com/cornada/fmri-observation-benchmarks/releases/tag/v1.0.0) for five self-contained paper ZIPs. Each ZIP includes the common library, its paper folder, dependencies and license. The paper-01 ZIP also includes the prepared MSC array; it is a release asset because of its size. The repository includes the complete synthetic transition dataset.

## Reproduction scope

The transition dataset and candidate score table reproduce the full synthetic benchmark. The MSC example reproduces the saved fixed-coefficient transfer means. Other examples execute the reusable measurements and learning workflow; the saved aggregates report the completed human analyses. ADNI participant records and participant-level derived features remain with authorized users under the [ADNI Data Use Agreement](https://adni.loni.usc.edu/wp-content/themes/adni_2023/documents/ADNI_Data_Use_Agreement.pdf). Instructions describe local input schemas for these methods.

Prepared FC and residual time-series inputs start after image preprocessing. This release does not rerun fMRIPrep or download restricted images. `SOURCE_PROVENANCE.json` records the implementation snapshots used; portability changes remove local paths and add the public entry points. Completed study outputs are preserved separately from software-demo outputs.

## License and citation

Our code, synthetic arrays and original aggregate tables are released under the [MIT license](LICENSE). The MSC derivative retains the source dataset's CC0 terms; see [DATA_LICENSES.md](DATA_LICENSES.md) and [CITATION.md](CITATION.md). NumPy, SciPy, scikit-learn, mpmath and threadpoolctl are external dependencies with their own licenses.
