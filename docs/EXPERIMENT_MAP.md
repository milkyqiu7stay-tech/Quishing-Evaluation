# Experiment-to-notebook mapping

| Manuscript claim/section | Source notebook | Notes |
|---|---|---|
| Dataset construction: 9,987 raw → 9,713 aligned pairs | `00_development_archive/qr_code_detection_model.ipynb` and `qr_phishing_experiment.ipynb` | Earlier development lineage; verify final exported CSV before reproducing |
| Baseline/literature reproduction | `01_baseline_reproduction/baseline_literature_reproduction.ipynb` | Contains classical ML and representative CNN reproduction, including matched CNN work |
| Structural attribution; native QR matrix analysis (Sec. 3.2) | `02_structural_robustness/exp2_exp4_corrected.ipynb` | Corrected structural experiment and older corrected Exp4 robustness; this notebook was **not executed** in the supplied archive copy |
| Initial raw pixel / lexical representation and Exp1–Exp5 development | `00_development_archive/qr_phishing_experiment.ipynb` | Long publication-oriented historical notebook; contains multiple sections beyond final main text |
| Matched raw-pixel vs lexical comparison (Sec. 3.1) | `03_paper_experiments/exp6_matched_comparison.ipynb` | Produces `matched_holdout_predictions.csv` for Exp8 and raw-pixel model for Exp7/Exp8 |
| End-to-end distortions (Sec. 3.4, Table 3) | `03_paper_experiments/exp7_end_to_end_robustness.ipynb` | Correct payload decoding, full-sample correct decision, conditional AUC; the +10° values were checked from sample CSV during the conversation, but **the CSV itself is not in this ZIP** |
| Eight legal QR-mask interventions (Sec. 3.2) | `03_paper_experiments/exp8_qr_mask_intervention.ipynb` | Requires Exp6 holdout. `RUN_MODE='full'` generates final mask summaries, alignment audit and sample-level data |
| Three protocols × three seeds (Sec. 3.3, Table 2) | `03_paper_experiments/exp9_entity_generalisation.ipynb` | Domain-parser/overlap audit and repeated XGBoost training. Earlier feature selection is **not nested** in each repeated split |
| External benign/malicious URL evaluation (Sec. 3.3) | `00_development_archive/qr_code_detection_model.ipynb` and `qr_phishing_experiment.ipynb` | Separate dataset; do not describe as exclusively phishing QR data |

## Scientific interpretation cautions

- Exp8 `F_mask` is the fraction of evaluated URLs with at least one hard-prediction change relative to the original QR encoding across valid masks; it is *not* a classification error rate.
- The saved Exp8 protocol explicitly warns that the full holdout had previously been inspected during CNN diagnostics; do not characterise it as an untouched pristine evaluation set without qualification.
- In Exp7, the +10° conditional lexical AUC excludes incorrectly decoded samples; full-sample lexical correct-decision rate counts decoding failures as unsuccessful.
- In Exp9, zero train/test overlap at registered-domain level is an evaluated split property, not proof of unconstrained real-world domain generalisation.
- The notebooks' original cell sources were not modified in this GitHub package; the previous **cell outputs** were removed to avoid exposing unreviewed data and to reduce file size.
