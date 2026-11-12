# Reproducing and navigating the study

## Scope of this archive

This release is a **navigable source-code snapshot**, not a tested one-command rerun. The submitted ZIP contained only eight notebooks. Running the code requires third-party source files, previously derived data, saved models and the original environment. References to old local Windows paths remain in the notebook source.

## Recommended environment

1. Use an isolated Python environment compatible with the notebook author's original installation.
2. Install the dependencies in `requirements.txt`; they are inferred package names, not an exact tested lockfile.
3. Record the actual final environment using `python -m pip freeze > environment-freeze.txt` and include Python, OpenCV, XGBoost, scikit-learn, qrcode, and TensorFlow versions where applicable.
4. Launch Jupyter, and make the experiment's required input paths point to your local data. Some cells use `DATA_DIR = Path('.')` and must run in a working directory containing `qr_full_feature_dataset_v2.csv`. Others search for the old `C:\Users\LENOVO\...` layout. If run from nested notebook directories, configure paths explicitly. No paths have been silently rewritten in this code snapshot.

## Practical execution order

The historical development notebooks are exploratory and contain multiple successive implementations. Their full top-to-bottom execution has not been verified in this package. The following is a **dependency order**, not a claim that every notebook can be run without adjustment:

1. **Input dataset and feature/model preparation** — study `notebooks/00_development_archive/qr_code_detection_model.ipynb`, producing or obtaining `qr_full_feature_dataset_v2.csv`, `FINAL_10feature_XGB_for_deployment.pkl`, `phase14B_final_robust_features.json`. Use the second development notebook for a condensed explanation and external validation lineage.
2. **Baseline and structural analyses** — review/run `notebooks/01_baseline_reproduction/baseline_literature_reproduction.ipynb` and `notebooks/02_structural_robustness/exp2_exp4_corrected.ipynb` with required inputs. Note that the matched CNN section within the baseline notebook additionally requires Exp6-produced files.
3. **Experiment 6** — run `notebooks/03_paper_experiments/exp6_matched_comparison.ipynb`. Expected outputs include `matched_holdout_predictions.csv` and `trad_style_raw_pixel_xgb_grouped.pkl`.
4. **Experiment 7** — run `notebooks/03_paper_experiments/exp7_end_to_end_robustness.ipynb`, using the exact frozen lexical model and preferably the Exp6 raw model. An Exp4 decoding cache may be supplied; otherwise decoding is computed live.
5. **Experiment 8** — run `notebooks/03_paper_experiments/exp8_qr_mask_intervention.ipynb` in `RUN_MODE = 'full'`, using Exp6's matched holdout. The default frozen-model inputs are required even if some optional models can be reconstructed.
6. **Experiment 9** — run `notebooks/03_paper_experiments/exp9_entity_generalisation.ipynb` with the final features, raw matrices and domain rules; this experiment does **not** depend on Exp6/7/8 outputs, only on upstream data/features.
7. **Matched CNN comparison** — the matching section of the baseline/literature reproduction notebook can be evaluated after Exp6 has produced the matched split information.

## Inputs and outputs

See `data/README.md` for required input names and `results/README.md` for output filenames to copy from the original experimental run. Uploading only notebooks is not enough for third parties to reproduce the manuscript's exact metrics.

## Preservation decisions

- All code cells and markdown content have been preserved verbatim in their respective Notebook documents.
- Stored outputs and execution counts are removed from the public-sharing copies. The source ZIP must be retained by the author as an original record.
- Files are renamed/moved for navigation only; Jupyter's working directory can change when a notebook is relocated. Reconfigure paths locally and rerun *only* after validating that unchanged sample IDs and models are used.
- The original archive has several very large, exploratory notebooks; these are intentionally separated from final Exp6–Exp9. Different variants should not be mixed when reproducing final tables.
