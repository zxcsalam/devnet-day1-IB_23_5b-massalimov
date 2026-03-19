import json, os, subprocess
from pathlib import Path
import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA_PATH = ROOT / "schemas" / "day5_summary.schema.json"

def test_day5_summary_full_validation():

    for var in ["STUDENT_TOKEN", "STUDENT_NAME", "STUDENT_GROUP"]:
        assert os.getenv(var), f"Environment variable {var} is missing"

    res = subprocess.run(["python3", "src/day5_summary_builder.py"], capture_output=True, text=True)
    assert res.returncode == 0, f"Builder failed: {res.stdout} {res.stderr}"

    summary_file = ART / "summary.json"
    assert summary_file.exists()
    summary = json.loads(summary_file.read_text())
    schema = json.loads(SCHEMA_PATH.read_text())

    jsonschema.validate(instance=summary, schema=schema)

    assert summary["yang"]["ok"] is True, "YANG tree check failed"
    assert summary["webex"]["ok"] is True, "Webex room title must contain token_hash8"
    assert summary["pt"]["empty_ticket_seen"] is True, "PT External check must show empty ticket"
    assert summary["validation_passed"] is True, "Final validation status must be True"