
from copy import deepcopy

from src.validate_backlog import (
    load_backlog,
    validate_backlog,
)


def test_valid_backlog_passes():
    backlog = load_backlog()

    errors = validate_backlog(backlog)

    assert errors == []


def test_duplicate_story_id_is_rejected():
    backlog = deepcopy(load_backlog())

    backlog["stories"][1]["id"] = "US-001"

    errors = validate_backlog(backlog)

    assert any("Duplicate story ID" in e for e in errors)


def test_invalid_priority_is_rejected():
    backlog = deepcopy(load_backlog())

    backlog["stories"][0]["priority"] = "Very High"

    errors = validate_backlog(backlog)

    assert any("Invalid priority" in e for e in errors)


def test_missing_acceptance_criteria_is_rejected():
    backlog = deepcopy(load_backlog())

    backlog["stories"][0]["acceptance_criteria"] = []

    errors = validate_backlog(backlog)

    assert any("Acceptance criteria" in e for e in errors)


def test_sprint_overcapacity_is_rejected():
    backlog = deepcopy(load_backlog())

    # Assign US-005 (5 points) to Sprint 1.
    # Sprint 1 already contains 8 points.
    backlog["stories"][4]["sprint"] = 1

    errors = validate_backlog(backlog)

    assert any("exceed capacity" in e for e in errors)


def test_deferred_story_cannot_be_scheduled():
    backlog = deepcopy(load_backlog())

    # US-006 is deferred from MVP-1.
    backlog["stories"][5]["sprint"] = 1

    errors = validate_backlog(backlog)

    assert any("Deferred story" in e for e in errors)


def test_missing_required_field_is_rejected():
    backlog = deepcopy(load_backlog())

    del backlog["stories"][0]["persona"]

    errors = validate_backlog(backlog)

    assert any("Missing fields" in e for e in errors)


def test_unknown_epic_is_rejected():
    backlog = deepcopy(load_backlog())

    backlog["stories"][0]["epic"] = "EPIC-999"

    errors = validate_backlog(backlog)

    assert any("Unknown Epic" in e for e in errors)
