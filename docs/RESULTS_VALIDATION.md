# Verification of the supplied final summary files

**Basis:** Eight CSV-text files from `Experiments Output.zip` plus three separately supplied full-run evidence CSV-text files. Ten files were preserved byte-for-byte with `.csv` extensions; the per-URL sensitivity file was privacy-reduced by replacing hostnames with opaque in-file group IDs and omitting original dataset row indices. This audit checks reported saved records, including 1,777 per-URL sensitivity rows, but does not rerun QR generation, model training, or bootstrap resampling. See `results/SOURCE_MANIFEST.csv` for fingerprints.

## Metrics reproduced from supplied summaries

| Paper / finding | Source column and evidence | Status |
|---|---|---|
| Exp6 raw-pixel ROC–AUC 0.8822 / lexical 0.9509 | `exp6/matched_holdout_summary.csv` `roc_auc` | Confirmed against rounded manuscript values |
| Exp6 paired AUC improvement 0.0688, 95% CI [0.0551, 0.0857] | `exp6/paired_hostname_bootstrap_ci.csv` | Confirmed as reported in stored bootstrap summary; resamples not regenerated |
| Exp7 +10° decoding 68.20%, lexical full-sample correct 60.16%, conditional AUC 0.9478 | `exp7/matched_robustness_summary.csv` | Confirmed; user also independently recomputed all three from 1,777 sample records in the prior Notebook check |
| Exp8 1,777 original QR matrices all match a valid mask | `exp8/encoder_alignment_audit.csv`: 1,777 `valid=True` | Confirmed from stored audit rows; generating them anew requires original dataset |
| Exp8 original mask 0 or 2 accounts for 96.90% | `exp8/encoder_alignment_audit.csv` `original_mask` | Recomputed from 1,777 rows |
| Exp8 original AUC 0.8822 / mask 0 AUC 0.8845 / mask 6 AUC 0.4811 | `exp8/original_and_mask_summary.csv` | Confirmed |
| Exp8 mask 6 all samples predicted phishing at fixed threshold | `exp8/mask_specific_summary.csv` predicted-phishing rate 1.0 | Confirmed |
| Exp8 mask 4 decode success 85.93%, strict lexical correct 75.91% | `exp8/original_and_mask_summary.csv` | Confirmed |
| Exp9 random / hostname / registered-domain mean±SD AUC table | `exp9/summary_mean_sd_by_regime_model.csv` (3 runs per cell) | Confirmed against rounded manuscript values |
| Exp9 0 hostname and registered-domain overlap for all three registered-domain-disjoint seeds | `exp9/split_integrity_audit.csv` | Confirmed **as recorded by the audit**, not independently recomputed from sample membership |

## Additional verified evidence from the three newly supplied files

| Finding | Computed/inspected evidence | Outcome |
|---|---|---|
| **Exp8 F_mask** | 1,132 `any_flip_vs_original=True` of 1,777 unique `sample_row` records | **0.6370287001 → 0.6370**, direct per-record recomputation |
| Exp8 mean probability range | Mean of 1,777 `prediction_probability_range` values | **0.6038099504 → 0.6038**, direct per-record recomputation |
| Exp8 F_mask hostname-bootstrap CI | Stored `hostname_bootstrap_ci.csv` row `URL_any_classification_flip_rate` | **[0.6035100, 0.6644381]**, interval checked as saved; bootstrap not rerun |
| Exp8 mask-6 AUC delta CI | Stored `AUC_delta_vs_original, mask_6` row | **-0.4010923; CI [-0.4404552, -0.3595014]**, checked as saved |
| Exp9 paired lexical-minus-raw AUC | Nine protocol × seed records in `paired_auc_cluster_bootstrap_ci.csv` | **All nine 95% confidence intervals exclude zero**, 300 valid cluster bootstrap resamples recorded per comparison |

## Remaining reproducibility limits

- The available CI tables are **saved bootstrap outputs**. They have not been regenerated independently from predictions and cluster-sampling code in this audit.
- The published public-safe per-URL file uses opaque `hostname_group_id` values instead of original hostnames and omits `original_index`; the original data were retained privately by the author.
- Fresh reproduction from QR images still requires the third-party input dataset, derived feature table, frozen model checkpoints, domain-rule dependencies and environment versions. Sample-level membership for Exp9 splits was not independently reconstructed here.

**Security/publication:** The released results contain no original URL or hostname columns, but authors must still verify all repository notebooks for credentials, local names, third-party redistribution rights and unpublished data before making the repository public.
