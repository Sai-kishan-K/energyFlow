# EnergyFlow 360 — Product Vision (v0.1)

## Problem
Fictional electricity supplier receives inconsistent smart-meter readings; invalid or duplicate events may delay billing and increase manual investigation.

## Product vision
Give billing and support teams a reliable, understandable view of customer meter readings and billing anomalies.

## Users
Billing manager, customer support agent, data operations analyst, residential customer.

## Product goal
Allow valid readings to enter a centralized system while giving business users clear reasons for rejected or suspicious readings.

## MVP in scope
- Customer and contract registration
- JSON meter reading ingestion and JSON Schema validation
- Duplicate detection
- Simple consumption and tariff calculations
- Business dashboard for readings, bills and anomalies

## Out of scope
- Real electricity provider integrations
- Real-time smart grid controls
- Payment collection
- Production-grade identity integration

## Candidate measurable outcomes (to be validated)
- 100% of defined invalid fixture cases rejected
- 100% of defined duplicate event-ID cases counted once
- All agreed billing examples match expected results
- All critical UAT scenarios pass

## Key risks and open questions
- Source and version of metering JSON contracts
- Meaning and units of consumption values
- Required meter and customer identifiers
- Timezone and late-arriving events
- Billing tariff and tax rules
- GDPR/privacy and retention obligations
