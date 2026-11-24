
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKLOG_PATH = ROOT / "backlog" / "product_backlog.json"

VALID_PRIORITIES = {"Must", "Should", "Could", "Won't"}
VALID_STATUSES = {"To Do", "In Progress", "Done", "Blocked"}

VALID_EPICS = {
    "EPIC-001",
    "EPIC-002",
    "EPIC-003",
    "EPIC-004",
}

VALID_STORY_POINTS = {1, 2, 3, 5, 8, 13}
SPRINT_CAPACITY = {1: 8}

REQUIRED_FIELDS = {
    "id",
    "epic",
    "title",
    "persona",
    "goal",
    "benefit",
    "priority",
    "story_points",
    "status",
    "sprint",
    "acceptance_criteria",
}


def load_backlog(path=BACKLOG_PATH):
    """Read the product backlog from a JSON file."""
    with Path(path).open(encoding="utf-8") as file:
        return json.load(file)


def validate_backlog(backlog):
    """
    Validate product backlog rules.

    Returns:
        list[str]: Validation errors.
                   Empty list means validation passed.
    """
    errors = []

    if not isinstance(backlog, dict):
        return ["Backlog must be a JSON object"]

    stories = backlog.get("stories")

    if not isinstance(stories, list):
        return ["The 'stories' field must be a list"]

    if not stories:
        return ["The product backlog cannot be empty"]

    seen_ids = set()
    sprint_totals = {}

    for index, story in enumerate(stories, start=1):
        if not isinstance(story, dict):
            errors.append(
                f"Story #{index} must be a JSON object"
            )
            continue

        story_id = story.get("id")
        label = story_id if isinstance(story_id, str) else f"#{index}"

        missing = REQUIRED_FIELDS - story.keys()

        if missing:
            errors.append(
                f"{label}: Missing fields: {', '.join(sorted(missing))}"
            )

        if not isinstance(story_id, str) or not story_id.strip():
            errors.append(f"{label}: Invalid story ID")
        elif story_id in seen_ids:
            errors.append(f"{label}: Duplicate story ID")
        else:
            seen_ids.add(story_id)

        if story.get("epic") not in VALID_EPICS:
            errors.append(f"{label}: Unknown Epic")

        for field in ("title", "persona", "goal", "benefit"):
            value = story.get(field)

            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{label}: '{field}' must be non-empty text"
                )

        priority = story.get("priority")

        if priority not in VALID_PRIORITIES:
            errors.append(f"{label}: Invalid priority")

        status = story.get("status")

        if status not in VALID_STATUSES:
            errors.append(f"{label}: Invalid status")

        points = story.get("story_points")

        if type(points) is not int or points not in VALID_STORY_POINTS:
            errors.append(f"{label}: Invalid story points")

        criteria = story.get("acceptance_criteria")

        if (
            not isinstance(criteria, list)
            or not criteria
            or any(
                not isinstance(item, str) or not item.strip()
                for item in criteria
            )
        ):
            errors.append(
                f"{label}: Acceptance criteria must be "
                "a non-empty list of text"
            )

        sprint = story.get("sprint")

        if sprint is not None and (
            type(sprint) is not int or sprint < 0
        ):
            errors.append(f"{label}: Invalid Sprint assignment")
            continue

        if priority == "Won't" and sprint is not None:
            errors.append(
                f"{label}: Deferred story assigned to a Sprint"
            )

        if sprint == 0 and status != "Done":
            errors.append(
                f"{label}: Sprint 0 work must be marked Done"
            )

        if sprint is not None and sprint > 0:
            if status == "Done":
                # A finished story remains part of Sprint scope.
                pass

            if sprint in SPRINT_CAPACITY:
                if type(points) is int and points in VALID_STORY_POINTS:
                    sprint_totals[sprint] = (
                        sprint_totals.get(sprint, 0) + points
                    )

    for sprint, total in sprint_totals.items():
        capacity = SPRINT_CAPACITY[sprint]

        if total > capacity:
            errors.append(
                f"Sprint {sprint}: {total} story points "
                f"exceed capacity of {capacity}"
            )

    return errors


def main():
    try:
        backlog = load_backlog()
    except (OSError, json.JSONDecodeError) as exc:
        print(f"BACKLOG VALIDATION FAILED: {exc}")
        return 1

    errors = validate_backlog(backlog)

    print("=" * 45)
    print("ENERGYFLOW 360 — PRODUCT BACKLOG VALIDATOR")
    print("=" * 45)

    if errors:
        print("STATUS: FAILED")

        for error in errors:
            print(f"[ERROR] {error}")

        return 1

    print("STATUS: PASSED")
    print(f"Total User Stories: {len(backlog['stories'])}")

    for sprint, capacity in SPRINT_CAPACITY.items():
        total = sum(
            story["story_points"]
            for story in backlog["stories"]
            if story["sprint"] == sprint
        )

        print(
            f"Sprint {sprint}: {total}/{capacity} Story Points"
        )

    print("All Product Backlog rules passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
