import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def get_validator():
    schema = json.loads((ROOT / "schemas/meter_reading.schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_file(path: Path):
    data = json.loads(path.read_text())
    return sorted(get_validator().iter_errors(data), key=lambda e: str(e.path))


def main():
    for filename in ("valid_meter_reading.json", "invalid_meter_reading.json"):
        errors = validate_file(ROOT / "samples" / filename)
        status = "PASS" if not errors else "REJECTED"
        print(f"{filename}: {status}")
        for err in errors:
            print(f"  Reason: {err.message}")


if __name__ == "__main__":
    main()
