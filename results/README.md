# Experiment output summaries

Eight summary/audit files from `Experiments Output.zip` plus three subsequently provided final-run evidence files are included under `exp6/`–`exp9/` (11 files total).

**File-format note:** The uploaded filenames ended in `.xls`, but their contents are ordinary CSV text, **not Excel workbooks**. The ten aggregate/audit files were copied **byte-for-byte** with `.csv` extensions. The per-URL sensitivity file was deliberately **privacy-reduced for public review**: original `hostname` values are replaced with anonymous `hostname_group_id` labels (preserving within-file clusters), and `original_index` is omitted. All per-URL prediction and sensitivity values remain unchanged. The private original should be retained locally; the public repository does not contain hostname strings from this file. See [`SOURCE_MANIFEST.csv`](SOURCE_MANIFEST.csv) for the original filenames, row counts and SHA-256 fingerprints.

| Experiment | Included file | What it records |
|---|---|---|
| Exp6 | `exp6/matched_holdout_summary.csv` | Matched holdout metrics for raw-pixel and lexical XGBoost |
| Exp6 | `exp6/paired_hostname_bootstrap_ci.csv` | Paired effect-size intervals |
| Exp7 | `exp7/matched_robustness_summary.csv` | Decoder success, full-sample correctness and conditional AUC by distortion |
| Exp8 | `exp8/original_and_mask_summary.csv` | Original and eight valid-mask predictions / decoding summaries |
| Exp8 | `exp8/mask_specific_summary.csv` | Per-mask metrics |
| Exp8 | `exp8/encoder_alignment_audit.csv` | Per-sample original-vs-generated matrix alignment audit |
| Exp9 | `exp9/summary_mean_sd_by_regime_model.csv` | Mean and standard deviation by split regime and model |
| Exp9 | `exp9/split_integrity_audit.csv` | Overlap counts for three regimes and three seeds |

| Exp8 | `exp8/per_url_mask_sensitivity.csv` | 1,777 per-URL records; hostname replaced with nonreversible group IDs; confirms flip union and mean probability range |
| Exp8 | `exp8/hostname_bootstrap_ci.csv` | Stored hostname-cluster bootstrap CIs for F_mask and per-mask AUC deltas |
| Exp9 | `exp9/paired_auc_cluster_bootstrap_ci.csv` | Stored paired AUC-difference cluster bootstrap CIs for 3 protocols × 3 seeds |

## Validation and scope

Run `python scripts/verify_reported_results.py` from the repository root and read [`docs/RESULTS_VALIDATION.md`](../docs/RESULTS_VALIDATION.md) for verified manuscript numbers and remaining limitations.

**What can now be verified:** Exp8's 1,132/1,777 flip count and 0.6038 mean within-URL probability range are directly recomputed from 1,777 public, hostname-anonymised records; the stored hostname-bootstrap CIs and all nine Exp9 paired CIs are also checked against the reported paper values. The bootstrap *resampling procedure itself* has not been independently rerun, and no original model training has been repeated. These are audit outputs, not a ready-to-run full reproduction package.

**Privacy and provenance:** Public per-URL data omit original hostnames and original dataset row indices; stable anonymous group labels are provided to retain cluster structure. Do not distribute the original file without checking dataset rights. This repository excludes original third-party QR matrices, URL records, and models.
