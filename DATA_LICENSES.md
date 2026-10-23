# Data licenses and access

* Synthetic observations, latent trajectories, hidden-state labels, candidate scores and original aggregate tables: MIT, as provided in this repository.
* `msc_sessions123.npz`: a prepared Pearson-connectivity derivative of the Midnight Scan Club, OpenNeuro `ds000224`, version 1.0.4, distributed under CC0. Source: [dataset record](https://doi.org/10.18112/openneuro.ds000224.v1.0.4). Retain the source attribution when reusing it. The exported array contains ten participants, the first three sessions, five processing paths and 79,800 FC edges.
* `locked_adni_mean_history.npy`, `locked_adni_mean_target.npy` and `fixed_coefficients.json`: population-level averages and shared model coefficients from 69 training participants. They contain no participant axis or participant identifiers.
* ADNI raw data and participant-level derived records are not part of this release. Obtain data through [ADNI](https://adni.loni.usc.edu/) and follow the applicable agreement when supplying local inputs.

The forecast split file contains row indices only. Reproducing the human analysis requires the authorized local participant-order manifest and data; the public synthetic example uses the same index plan on synthetic rows.
