# Revisiting Quishing Detection: Research Code

Companion code for **Revisiting Quishing Detection: Encoding Sensitivity, Generalisation, and Pipeline Trade-offs** (ESANN 2027 manuscript).

This repository organises the original study notebooks without changing their **code cells or markdown explanations**. For safer, smaller public distribution, previously saved **execution outputs and execution counts have been cleared**. See [`docs/SOURCE_MAP.md`](docs/SOURCE_MAP.md) for exact original filenames and integrity checks.

> **Reproducibility status:** This is an organised *research-code snapshot*, not a one-command reproducibility package. The original code archive contains only eight notebooks; separate output archives supply eleven result/evidence files; the source QR dataset, cleaned feature table, saved classifiers, feature-selection metadata and domain-rule snapshot are **not included**; 10 final summary/CI/audit tables and one public-safe per-URL mask sensitivity file **are included**. Full raw per-mask predictions and the original hostname values are not included. Some notebooks still refer to the author's original Windows paths and may require setting working directories. See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## What the paper evaluates

1. **Matched discrimination:** raw-pixel vs. decoded-URL lexical features on matched QR samples (Experiment 6).
2. **Structural attribution:** QR structural statistics and incremental information relative to URL features (corrected Experiments 2/4 notebook).
3. **Payload-preserving mask intervention:** eight legal QR masks at fixed payload and encoding settings (Experiment 8).
4. **Entity-disjoint generalisation:** random, hostname-disjoint and registered-domain-disjoint train/test protocols (Experiment 9).
5. **Full-pipeline reliability:** image distortions, decoding success and correct decisions on all input samples (Experiment 7).

The earlier development and external URL validation are recorded in the development notebooks, and baseline/related-work reproduction is in the reproduction notebook.

## Find the code

| Manuscript component | Notebook |
|---|---|
| Dataset preparation, initial feature engineering, model development and external URL evaluation | [`notebooks/00_development_archive/qr_code_detection_model.ipynb`](notebooks/00_development_archive/qr_code_detection_model.ipynb) |
| Publication-oriented development summary and Exp1–Exp5 | [`notebooks/00_development_archive/qr_phishing_experiment.ipynb`](notebooks/00_development_archive/qr_phishing_experiment.ipynb) |
| Trad/Chehab and Do et al. reproduction, matched CNN experiments | [`notebooks/01_baseline_reproduction/baseline_literature_reproduction.ipynb`](notebooks/01_baseline_reproduction/baseline_literature_reproduction.ipynb) |
| Corrected structural attribution and earlier held-out QR robustness | [`notebooks/02_structural_robustness/exp2_exp4_corrected.ipynb`](notebooks/02_structural_robustness/exp2_exp4_corrected.ipynb) |
| Matched XGBoost comparison, paired hostname bootstrap | [`notebooks/03_paper_experiments/exp6_matched_comparison.ipynb`](notebooks/03_paper_experiments/exp6_matched_comparison.ipynb) |
| Matched image robustness, decoding failure, full-sample correctness | [`notebooks/03_paper_experiments/exp7_end_to_end_robustness.ipynb`](notebooks/03_paper_experiments/exp7_end_to_end_robustness.ipynb) |
| Controlled QR-mask intervention and prediction instability | [`notebooks/03_paper_experiments/exp8_qr_mask_intervention.ipynb`](notebooks/03_paper_experiments/exp8_qr_mask_intervention.ipynb) |
| Repeated entity-disjoint splitting and split-integrity checks | [`notebooks/03_paper_experiments/exp9_entity_generalisation.ipynb`](notebooks/03_paper_experiments/exp9_entity_generalisation.ipynb) |

**Note:** The development archive includes exploratory/superseded variants, and the corrected Exp2/Exp4 notebook was saved without executed outputs. For the paper's final Exp6–Exp9 procedures, start with the dedicated notebooks rather than trying to run the entire historical archive indiscriminately.

## Reproduction and data

- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md): inputs, dependencies, execution order and known caveats
- [`data/README.md`](data/README.md): data sourcing, required files and redistribution cautions
- [`results/README.md`](results/README.md): eleven final result/evidence files, including anonymised per-URL sensitivity data
- [`docs/EXPERIMENT_MAP.md`](docs/EXPERIMENT_MAP.md): correspondence between notebooks and paper claims
- [`docs/RESULTS_VALIDATION.md`](docs/RESULTS_VALIDATION.md): which paper figures are supported by the supplied output tables and per-URL verification
- [`scripts/verify_reported_results.py`](scripts/verify_reported_results.py): check aggregate values and recompute Exp8 F_mask from 1,777 per-URL rows
- [`docs/RELEASE_CHECKLIST_CN.md`](docs/RELEASE_CHECKLIST_CN.md): Chinese pre-publication checklist


## Environment

The experimental environment was based on Anaconda with Python 3.10.19 on Windows (64-bit).
The environment used for Experiment 8 was:
- Conda environment: `tf`
- Python version: 3.10.19
- Package dependencies: `requirements.txt`
- Installed package versions: `environment-freeze.txt`
The repository documents the research code and experimental results. Full reproduction requires the original datasets, trained models, and intermediate artifacts described in `docs/REPRODUCIBILITY.md`.


## Scope and limitations

The results describe the evaluated dataset, trained models and preprocessing pipelines. Mask intervention measures prediction inconsistency, not misclassification rate. The ten lexical features were selected on the original benchmark before repeated split comparisons, rather than within each training fold. Please consult the manuscript for the complete assumptions and limitations.

## Code/data attribution and reuse

The QR-image benchmark originates from the work of Trad and Chehab (2026), *Detecting Quishing Attacks with Machine Learning Techniques Through QR Code Analysis*. The external URL benchmark is separately attributed in the manuscript. **Original third-party datasets are not redistributed here.** No open-source license has been chosen in this generated copy; agree on code-sharing rights and a license with the co-authors/supervisor before public release.
