
# EnergyFlow 360 — User Stories

## US-001: Validate Meter-Reading JSON

As a Billing Agent,
I want incoming meter readings to be validated,
so that malformed data does not enter billing.

Priority: Must
Story Points: 3
Status: Done — Pending PO Review
Epic: EPIC-001

### Acceptance Criteria

Scenario: Valid meter reading

Given a meter-reading JSON follows the approved schema
When the validation process runs
Then the reading should pass validation

Scenario: Missing mandatory field

Given a meter reading is missing a required field
When the validation process runs
Then the reading should be rejected

Scenario: Invalid consumption

Given a meter reading has negative consumption
When the validation process runs
Then the reading should be rejected

---

## US-002: Validate Timestamp Format

As a Billing Agent,
I want timestamps to be validated,
so that readings have reliable time information.

Priority: Must
Story Points: 2
Status: Done — Pending PO Review
Epic: EPIC-001

### Acceptance Criteria

Scenario: Valid timestamp

Given a reading contains a valid date-time value
When schema validation runs
Then the timestamp should be accepted

Scenario: Invalid timestamp

Given the timestamp is "not-a-date"
When schema validation runs
Then the reading should be rejected

---

## US-003: Actionable Validation Errors

As a Billing Agent,
I want clear validation error messages,
so that I can investigate invalid readings quickly.

Priority: Must
Story Points: 3
Status: To Do
Epic: EPIC-001

### Acceptance Criteria

Scenario: Invalid consumption

Given a reading has consumption_kwh = -5
When the validation process runs
Then the reading should be rejected
And the error should identify consumption_kwh
And the error should explain the invalid value

Scenario: Valid reading

Given a reading satisfies the schema
When the validation process runs
Then no validation errors should be returned

---

## US-004: Duplicate Meter Event Detection

As a Billing Agent,
I want duplicate meter events to be detected,
so that energy consumption is never counted twice.

Priority: Must
Story Points: 5
Status: To Do
Epic: EPIC-002

### Acceptance Criteria

Scenario: First occurrence

Given an event ID has not been processed
When the event is received
Then the event should be accepted

Scenario: Duplicate occurrence

Given event ID EVT-1001 has already been processed
When another event with ID EVT-1001 arrives
Then the system should identify it as a duplicate
And it should not increase consumption totals

---

## US-005: Rejected Readings Dashboard

As a Billing Agent,
I want to view rejected meter readings,
so that I can investigate errors efficiently.

Priority: Should
Story Points: 5
Status: To Do
Epic: EPIC-003

### Acceptance Criteria

Scenario: View rejected readings

Given rejected readings are available
When an agent opens the anomaly dashboard
Then rejected readings should be displayed
And each item should show its error reason

Scenario: Filter readings

Given multiple meters have rejected readings
When the agent filters by meter ID
Then only matching readings should be displayed

---

## US-006: Electricity Charge Calculation

As a Billing Manager,
I want electricity charges to be calculated,
so that manual billing effort is reduced.

Priority: Won't (MVP-1)
Story Points: 8
Status: To Do
Epic: EPIC-004

### Acceptance Criteria

Scenario: Calculate charges

Given validated consumption readings exist
And an electricity tariff is configured
When billing is triggered
Then charges should be calculated
And a billing breakdown should be provided

Release Decision:
Deferred from MVP-1 due to limited delivery capacity.
