from pathlib import Path
import argparse

REQUIRED = [
    'qr_codes_29.pickle',
    'qr_codes_29_labels.pickle',
    'qr_full_feature_dataset_v2.csv',
    'FINAL_10feature_XGB_for_deployment.pkl',
    'phase14B_final_robust_features.json',
]
OPTIONAL = [
    'esann_icann_psl_snapshot.txt',
    'balanced_urls.csv',
    'matched_holdout_predictions.csv',
    'trad_style_raw_pixel_xgb_grouped.pkl',
    'sample_level_robustness_results.csv',
]

parser = argparse.ArgumentParser(description='Find common input artefacts in a local FYP directory')
parser.add_argument('--root', required=True, help='Folder containing your source/derived data')
args = parser.parse_args()
root = Path(args.root).expanduser()
if not root.is_dir():
    raise SystemExit(f'Not a directory: {root}')
found = {}
for item in root.rglob('*'):
    if item.is_file() and item.name in REQUIRED + OPTIONAL:
        found.setdefault(item.name, []).append(item)
print('Search directory:', root)
for name in REQUIRED + OPTIONAL:
    locations = found.get(name, [])
    print(('FOUND   ' if locations else 'MISSING '), name,
          (' -> ' + '; '.join(str(p) for p in locations[:3])) if locations else '')
print('\nNotes: Missing optional files may trigger a fallback or regeneration; see docs/REPRODUCIBILITY.md.')
