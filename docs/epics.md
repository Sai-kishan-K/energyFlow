
# EnergyFlow 360 — Product Epics

## Product Goal

Enable billing teams to receive trustworthy electricity
meter readings and investigate incorrect data efficiently.

## EPIC-001: Meter Data Validation

Business Value:
Prevent incorrect consumption data from entering billing.

Scope:
- Validate incoming meter-reading JSON.
- Reject negative consumption values.
- Reject invalid timestamps.
- Reject missing mandatory fields.
- Provide clear error messages.

Primary Stakeholder: Billing Manager

Success Criteria:
- All defined invalid test cases are rejected.
- Valid meter readings pass schema validation.

## EPIC-002: Duplicate Detection

Business Value:
Prevent repeated meter events from being counted twice.

Scope:
- Identify duplicate event IDs.
- Reject or safely ignore duplicate events.
- Record duplicate-event details.

Primary Stakeholder: Billing Operations

Success Criteria:
- Repeated event IDs never create duplicate
  consumption records.

## EPIC-003: Anomaly Monitoring

Business Value:
Help billing agents investigate data-quality issues.

Scope:
- Display rejected meter readings.
- Show validation error reasons.
- Filter anomalies by meter and date.

Primary Stakeholder: Billing Agent

Success Criteria:
- Agents can identify and review rejected readings.

## EPIC-004: Billing Automation

Business Value:
Reduce manual invoice calculations.

Scope:
- Apply electricity tariffs.
- Calculate energy charges.
- Generate billing summaries.

Primary Stakeholder: Billing Manager

Release Decision:
Deferred beyond the initial six-week MVP.

## Initial Release Strategy

Priority 1: Meter Data Validation
Priority 2: Duplicate Detection
Priority 3: Anomaly Monitoring
Deferred: Billing Automation

All priorities are provisional until sponsor approval.
