import json
from pathlib import Path

from src.validate_meter import ROOT, get_validator, validate_file


def test_valid_reading_is_accepted():
    assert not validate_file(ROOT / "samples/valid_meter_reading.json")


def test_negative_consumption_is_rejected():
    errors = validate_file(ROOT / "samples/invalid_meter_reading.json")
    assert errors
    assert any(e.validator == "minimum" for e in errors)


def test_missing_event_id_is_rejected():
    data = json.loads((ROOT / "samples/valid_meter_reading.json").read_text())
    del data["event_id"]
    assert any(e.validator == "required" for e in get_validator().iter_errors(data))


def test_invalid_timestamp_is_rejected():
    data = json.loads((ROOT / "samples/valid_meter_reading.json").read_text())
    data["timestamp"] = "not-a-date"
    assert any(e.validator == "format" for e in get_validator().iter_errors(data))
