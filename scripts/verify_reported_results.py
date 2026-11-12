#!/usr/bin/env python3
"""Check the supplied aggregate CSVs against selected ESANN manuscript claims.

Does not rerun models, reconstruct bootstrap samples, or prove the raw data split.
Uses Python standard library only; run from any working directory.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

def table(path):
    with (RESULTS / path).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def row(rows, **filters):
    found = [r for r in rows if all(str(r[k]) == str(v) for k, v in filters.items())]
    assert len(found) == 1, f"Expected one row for {filters}, found {len(found)}"
    return found[0]

def approx(actual, expected, digits=4, label="metric"):
    actual = float(actual)
    assert round(actual, digits) == round(expected, digits), (label, actual, expected)
    print(f"PASS {label}: {actual:.6f}")

exp6 = table("exp6/matched_holdout_summary.csv")
raw = row(exp6, model="Trad-style raw-pixel XGBoost")
lex = row(exp6, model="Frozen 10-feature lexical XGBoost")
assert int(raw["n"]) == int(lex["n"]) == 1777
approx(raw["roc_auc"], .8822, label="Exp6 raw AUC")
approx(lex["roc_auc"], .9509, label="Exp6 lexical AUC")
ci = row(table("exp6/paired_hostname_bootstrap_ci.csv"), metric="roc_auc")
approx(ci["delta_lex_minus_raw"], .0688, label="Exp6 paired AUC delta")
approx(ci["ci95_lower"], .0551, label="Exp6 CI lower")
approx(ci["ci95_upper"], .0857, label="Exp6 CI upper")

exp7 = row(table("exp7/matched_robustness_summary.csv"), condition="Rotation_plus_10.0deg")
assert int(exp7["n"]) == 1777
approx(100 * float(exp7["lexical_correct_payload_rate"]), 68.20, digits=2, label="Exp7 +10 decode %")
approx(100 * float(exp7["lexical_strict_end_to_end_correct_rate"]), 60.16, digits=2, label="Exp7 +10 strict lexical correct %")
approx(exp7["lex_common_subset_auc"], .9478, label="Exp7 +10 conditional AUC")

exp8 = table("exp8/original_and_mask_summary.csv")
orig = row(exp8, condition="Original encoder-selected mask")
mask0 = row(exp8, mask=0)
mask4 = row(exp8, mask=4)
mask6 = row(exp8, mask=6)
for r in [orig, mask0, mask4, mask6]: assert int(r["n"]) == 1777
approx(orig["raw_auc"], .8822, label="Exp8 original AUC")
approx(mask0["raw_auc"], .8845, label="Exp8 mask0 AUC")
approx(mask6["raw_auc"], .4811, label="Exp8 mask6 AUC")
approx(mask6["raw_predicted_phishing_rate"], 1.0, label="Exp8 mask6 phishing prediction fraction")
approx(100 * float(mask4["correct_decode_rate"]), 85.93, digits=2, label="Exp8 mask4 decode %")
approx(100 * float(mask4["lexical_strict_correct_rate"]), 75.91, digits=2, label="Exp8 mask4 strict lexical correct %")

align = table("exp8/encoder_alignment_audit.csv")
assert len(align) == 1777
assert all(r["valid"].strip().lower()=="true" for r in align)
assert len({r["sample_row"] for r in align}) == 1777
share = 100 * sum(r["original_mask"] in ("0", "2") for r in align) / len(align)
approx(share, 96.90, digits=2, label="Exp8 original mask0/2 %")
print("PASS Exp8 original-QR matrix audit: 1777/1777 valid as recorded")

exp9 = table("exp9/summary_mean_sd_by_regime_model.csv")
expected = {
 ("random_stratified", "lexical_10"):(.9617,.0070),
 ("random_stratified", "raw_pixel"):(.9129,.0077),
 ("hostname_disjoint", "lexical_10"):(.9578,.0063),
 ("hostname_disjoint", "raw_pixel"):(.8881,.0105),
 ("registered_domain_disjoint", "lexical_10"):(.9572,.0091),
 ("registered_domain_disjoint", "raw_pixel"):(.8881,.0252),
}
for (regime,model),(mean,sd) in expected.items():
    r=row(exp9, regime=regime, model=model)
    assert int(r["runs"])==3
    approx(r["auc_mean"],mean,label=f"Exp9 {regime}/{model} mean AUC")
    approx(r["auc_sd"],sd,label=f"Exp9 {regime}/{model} AUC SD")

integrity = table("exp9/split_integrity_audit.csv")
assert len(integrity)==9
regrows=[r for r in integrity if r["regime"]=="registered_domain_disjoint"]
assert {r["seed"] for r in regrows}=={"42","43","44"}
assert all(int(r["hostname_overlap"])==int(r["registered_domain_overlap"])==0 for r in regrows)
print("PASS Exp9 audit records: zero hostname/domain overlap in three registered-domain splits")
# Newly provided full-run evidence: independently recompute F_mask and the mean probability range.
per_url = table("exp8/per_url_mask_sensitivity.csv")
assert len(per_url) == 1777
assert len({r["sample_row"] for r in per_url}) == 1777
assert len({r["hostname_group_id"] for r in per_url}) == 1387
assert all(r["any_flip_across_masks"] == r["any_flip_vs_original"] for r in per_url)
assert all((r["any_flip_vs_original"].lower() == "true") == (float(r["flip_vs_original_fraction"]) > 0) for r in per_url)
flip_total = sum(r["any_flip_vs_original"].lower() == "true" for r in per_url)
assert flip_total == 1132
approx(flip_total / len(per_url), .6370, label="Exp8 F_mask independently recomputed")
mean_range = sum(float(r["prediction_probability_range"]) for r in per_url) / len(per_url)
approx(mean_range, .6038, label="Exp8 mean within-URL probability range")

host_ci = table("exp8/hostname_bootstrap_ci.csv")
flip_ci = row(host_ci, metric="URL_any_classification_flip_rate", condition="all_masks")
assert flip_ci["bootstrap_unit"] == "hostname"
approx(flip_ci["estimate"], flip_total / len(per_url), digits=10, label="Exp8 stored flip-rate CI point estimate")
approx(flip_ci["ci_low"], .6035, label="Exp8 F_mask CI lower")
approx(flip_ci["ci_high"], .6644, label="Exp8 F_mask CI upper")
mask6_ci = row(host_ci, metric="AUC_delta_vs_original", condition="mask_6")
assert mask6_ci["bootstrap_unit"] == "hostname"
approx(mask6_ci["estimate"], -.4011, label="Exp8 mask6 paired AUC delta")
approx(mask6_ci["ci_low"], -.4405, label="Exp8 mask6 CI lower")
approx(mask6_ci["ci_high"], -.3595, label="Exp8 mask6 CI upper")

exp9_ci = table("exp9/paired_auc_cluster_bootstrap_ci.csv")
assert len(exp9_ci) == 9
assert {(r["regime"],r["seed"]) for r in exp9_ci} == {(regime,seed) for regime in ["random_stratified","hostname_disjoint","registered_domain_disjoint"] for seed in ["42","43","44"]}
assert all(r["cluster"] == "registered_domain" and int(r["valid_bootstraps"]) == 300 for r in exp9_ci)
assert all(float(r["ci95_lower"]) > 0 and float(r["ci95_upper"]) > float(r["ci95_lower"]) for r in exp9_ci)
print("PASS Exp9: all 9 stored paired cluster-bootstrap 95% CIs exclude 0; 300 valid resamples each")

print("\nPASS: All selected manuscript claims match the provided saved results, including newly supplied per-URL results and bootstrap summaries.")
print("SCOPE: Bootstrap intervals are verified as stored outputs, not regenerated from resampling.")
print("SCOPE: No original QR dataset/model retraining or full split-membership reconstruction was performed.")
