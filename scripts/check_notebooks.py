"""Validate tracked learning notebooks without executing cells or downloading data."""
from pathlib import Path
import sys
import warnings
import nbformat

root = Path(__file__).resolve().parents[1]
paths = sorted(path for path in root.rglob("*.ipynb")
               if not any(part in {".ipynb_checkpoints", ".venv", "venv", ".git"} for part in path.parts))
failures = []
error_outputs = []
for path in paths:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", nbformat.warnings.MissingIDFieldWarning)
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
        count = sum(output.get("output_type") == "error"
                    for cell in notebook.cells for output in cell.get("outputs", []))
        if count:
            error_outputs.append((path.relative_to(root), count))
    except Exception as exc:
        failures.append((path.relative_to(root), str(exc)))
print(f"Validated structure of {len(paths)} notebooks; no cells were executed.")
for path, count in error_outputs:
    print(f"Historical error outputs ({count}): {path}")
for path, message in failures:
    print(f"INVALID {path}: {message}", file=sys.stderr)
if not paths:
    print("No notebooks found", file=sys.stderr)
sys.exit(1 if failures or not paths else 0)
