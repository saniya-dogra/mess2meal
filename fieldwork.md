# Mess2Meal — operational workflow and validation

## Document purpose

This document describes the operational use case the Mess2Meal prototype is designed to support, the workflow assumptions used in development, and the checks required before the system could be used in a real food redistribution programme.

It is a product and operational design document. It is not a claim that a site visit, interview, NGO partnership or food handover has taken place.

## 1. Problem statement

Food providers such as college messes, hostel kitchens, restaurants, cafeterias and households may have surplus prepared food. Potential recipient organisations may need food but require reliable information about the food, quantity, timing and collection arrangements.

The coordination problem includes identifying surplus while it is still within its usable period, recording accurate quantity and preparation details, sharing handling information for responsible review, finding a recipient with suitable preferences and capacity, confirming acceptance and coordinating pickup, and recording the actual handover separately from a suggested match.

Mess2Meal provides a structured digital workflow for these coordination steps.

## 2. Users and responsibilities

| User | Main responsibility | System interaction |
|---|---|---|
| Food donor | Provide accurate listing and handling details | Create a surplus listing |
| Recipient organisation | Confirm needs, capacity and acceptance | Register recipient details; review a proposed match |
| Coordinator | Review listings, recipient suitability and timing | Inspect ranked suggestions and update status |
| Volunteer / pickup partner | Coordinate and complete collection | Participate in the offline handover process |
| Administrator | Maintain records and review outcomes | View listings and delivered-only impact totals |

The current prototype does not implement separate authenticated roles. These roles describe the intended operating model.

## 3. End-to-end operating workflow

| Step | Operational activity | Information recorded | Responsible party |
|---|---|---|---|
| 1. Identify surplus | Donor identifies food that may be available | Source, food name, category and quantity | Donor |
| 2. Create listing | Donor enters listing details | Preparation time, best-before time, storage description and pickup location | Donor |
| 3. Review details | Coordinator checks completeness and suitability | Review decision and missing information | Coordinator |
| 4. Find recipients | System filters and ranks eligible recipients | Category preference, capacity, urgency and entered distance | System + coordinator |
| 5. Confirm acceptance | Recipient agrees to accept the offered quantity | Acceptance and agreed quantity | Recipient |
| 6. Arrange collection | Parties agree pickup time and responsibility | Pickup plan and contact coordination | Donor + recipient |
| 7. Verify handover | Food is physically handed over | Actual handover time, quantity and confirmation | Parties involved |
| 8. Close listing | Coordinator updates final status | Delivered / other final status | Coordinator |

A match suggestion is not an acceptance. Acceptance is not a completed pickup. Only a verified handover should be counted as delivered.

## 4. Information required for a useful listing

| Field | Why it matters |
|---|---|
| Donor/source | Identifies where the food is offered |
| Food name and category | Helps recipient assess suitability |
| Quantity and unit | Allows capacity comparison |
| Preparation date/time | Provides context for time-sensitive review |
| Best-before / use-by information | Helps responsible people assess the remaining usable period |
| Storage and packaging description | Provides handling context for review |
| Pickup location | Allows the parties to plan collection |
| Notes | Captures relevant constraints without exposing private data |

The donor must provide accurate information. A text description is not proof that food has been stored safely.

## 5. Recipient information

The prototype supports recipient records with organisation/group name, recipient type, contact person and phone field, location, preferred food categories, maximum capacity in kilograms, urgency level and active/inactive availability.

In a real deployment, recipient identity, authority to receive food, contact details and capacity would need to be verified. The current prototype does not independently verify organisations.

## 6. Matching logic and decision boundaries

The Python matching module applies these filters:

1. Listing status must be available.
2. Best-before timestamp must be in the future.
3. Storage description must be present and must not contain configured unsafe terms.
4. Recipient must be active.
5. Recipient capacity must be at least the listed quantity.
6. Recipient category preferences must include the food category or the value All.

Eligible recipients are ranked using urgency, coordinator-entered distance and capacity. The response includes a score and reasons.

**Decision boundary:** the algorithm performs data-based filtering and prioritisation only. It cannot inspect food, validate temperature history, identify contamination, determine legal suitability or guarantee that a recipient can collect the food. A responsible human must make those decisions.

## 7. Operational risks and controls

| Risk | Potential consequence | Control / next improvement |
|---|---|---|
| Inaccurate preparation or expiry details | Incorrect time-based decision | Require donor confirmation and coordinator review |
| Incomplete storage information | Unsafe assumption about handling | Hold incomplete listings for human review |
| Recipient details are unverified | Failed or misdirected donation | Add verification and periodic re-confirmation |
| Recipient capacity is outdated | Excess quantity offered | Confirm capacity before acceptance |
| Pickup is delayed | Food may no longer be suitable | Add pickup windows and escalation process |
| Match mistaken for delivery | Inflated impact reporting | Separate suggested, accepted, collected and delivered states |
| Personal data exposure | Privacy risk | Restrict access and minimise stored contact details |
| Synthetic data treated as evidence | Misleading project claims | Preserve provenance labels and disclose demo data |

## 8. Validation status

The repository includes a local prototype, a synthetic CSV dataset and matching tests. These demonstrate software behaviour, not live operational performance.

| Validation area | Current status |
|---|---|
| Python application structure | Implemented in repository |
| FastAPI food and recipient endpoints | Implemented in repository |
| SQLite persistence | Implemented in repository |
| Recipient filtering and ranking | Implemented in repository |
| Streamlit dashboard | Implemented in repository |
| Synthetic CSV dashboard view | Implemented in repository |
| Unit tests | Test files present; execute before release |
| Live donor onboarding | Not implemented / not verified |
| Live NGO onboarding and verification | Not implemented / not verified |
| Real pickup coordination | Manual / outside current prototype |
| Confirmed real-world food handovers | Not documented |
| Production security and deployment | Not implemented |

## 9. Compliance and responsible use

The workflow is informed by the Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019. The application is not a compliance tool and does not replace donor responsibilities, recipient procedures or applicable food-safety requirements.

Before operational use, the organisation responsible for redistribution must establish appropriate processes for food eligibility, hygiene, packaging, temperature control, transport, traceability, recipient verification and incident handling.

## 10. Scope conclusion

The current Mess2Meal prototype demonstrates how surplus listings, recipient records, explainable matching and delivery status can be organised in one Python application. Its next engineering steps are role-based access, recipient verification, explicit acceptance and pickup states, audit history, notification support and a production-ready database.

The current repository should be evaluated as a functional prototype rather than a live food distribution service.
