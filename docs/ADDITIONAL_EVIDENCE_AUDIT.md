# Supplementary evidence audit (2026-11-12)

Three author-supplied `.xls` files were in fact CSV text:

| Source file | Repository file | Source SHA-256 | Distribution |
|---|---|---|---|
| `hostname_bootstrap_ci(1).xls` | `results/exp8/hostname_bootstrap_ci.csv` | `ed680c1f3c0e16ecab1057053dc7e6d4b9fb2b7bb89b9d02485bbb795f887c41` | Byte-identical CSV with renamed extension |
| `paired_auc_cluster_bootstrap_ci(1).xls` | `results/exp9/paired_auc_cluster_bootstrap_ci.csv` | `26e187388b651db3e4335a51a72b8b59deea43409e1c869e48c6d84844146e0e` | Byte-identical CSV with renamed extension |
| `per_url_mask_sensitivity(2).xls` | `results/exp8/per_url_mask_sensitivity.csv` | `24c3b6902a7e1470fd5483c593f51cce92b50d92dda604c1d269a74ec584218f` | Sanitised per-URL derivative |

The public per-URL derivative replaces hostnames with stable, anonymous within-file group IDs; it drops original dataset indices. `SOURCE_MANIFEST.csv` SHA-256 values describe the **repository version**. The 1,777 per-URL flip flags and probability ranges are unchanged.

Run `python scripts/verify_reported_results.py` from anywhere to verify the results against manuscript rounding. This does not constitute a fresh data-generation or model-training replication.
