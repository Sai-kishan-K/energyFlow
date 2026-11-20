# Initial Requirements (hypotheses — not yet client-approved)

| ID | Requirement | Priority | Acceptance idea |
|---|---|---|---|
| FR-01 | Accept valid JSON meter events | Must | A conforming event is accepted |
| FR-02 | Reject schema-invalid meter events with reason | Must | Missing/invalid field produces readable error |
| FR-03 | Identify repeated event IDs | Must | Same event ID does not double-count |
| FR-04 | Display accepted and rejected event counts | Should | Dashboard reconciles test fixture counts |
| FR-05 | Calculate sample electricity bills | Should | Agreed examples match expected results |
| NFR-01 | Audit validation outcomes | Must | Status, time and reason available in logs |
| NFR-02 | Restrict access to sensitive data | Must | Role permissions are specified and tested |

**Assumption:** Sample readings express non-negative consumption in kWh for a time interval. Confirm with client.

## Business Requirements — Discovery Workshop 1

### Business Problem
The billing team receives meter readings containing invalid
or incomplete information. These errors create manual
investigation work and may delay billing operations.

### Business Objective
Improve meter-reading data quality before billing.

### Functional Requirements

- FR-001: Validate incoming readings using JSON Schema.
- FR-002: Reject negative consumption values.
- FR-003: Reject timestamps that do not follow the required format.
- FR-004: Reject readings missing mandatory fields.
- FR-005: Return actionable validation error messages.

### Non-Functional Requirements

- NFR-001: Target p95 API latency below 500 ms under
  an agreed test workload.
- NFR-002: Maintain automated tests for critical
  validation rules.

### Assumptions
- The platform receives JSON meter-reading events.
- The initial implementation uses synthetic data.
- Billing calculations are outside the current
  validation-only increment.

### Open Questions
- What is the expected daily event volume?
- What timestamp timezone policy should we use?
- How should rejected readings be stored or reported?
- Which fields uniquely identify a meter-reading event?
- Which business team owns the validation rules?