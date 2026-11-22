# Mess2Meal — field research and operational case study

**Document status:** Desk research and workflow case study completed; primary field evidence is not available in this repository.  
**Purpose:** Document the research method, operational scenario, requirements and evidence boundaries without presenting an unverified visit or interview as fact.

## 1. Research method

This document combines secondary research from FSSAI's surplus-food regulations and Indian Food Sharing Alliance (IFSA) material, UNEP's Food Waste Index Report 2024, and a hypothetical end-to-end workflow used to test product requirements.

It does not record a physical site visit, a real interview, an NGO partnership, measured local quantities or a completed food handover. No date, person, quote, photo or location has been invented.

## 2. Operational case study — illustrative scenario

**Scenario:** A college dining facility has prepared more food than its service demand. A community organisation may be able to accept some surplus, but the two parties need to coordinate food details, quantity, timing, transport and safe handling.

This is a design scenario, not an observed event.

| Stage | Information needed | Mess2Meal feature | Human decision |
|---|---|---|---|
| Surplus identified | Food item, quantity, source, time | Create listing | Donor confirms food is available |
| Details recorded | Preparation time, use-by information, storage description | Validated listing fields | Donor supplies accurate information |
| Initial review | Food condition and handling requirements | Review prompts | Responsible person checks food; software cannot certify safety |
| Recipient search | Recipient category, capacity and availability | Matching shortlist | Coordinator verifies recipient suitability |
| Acceptance | Quantity accepted and collection time | Acceptance status | Recipient confirms |
| Pickup | Responsible collector and agreed time | Pickup status | Donor and recipient coordinate transport |
| Handover | Actual quantity and timestamp | Delivered status | Both parties confirm handover |
| Reporting | Confirmed quantity delivered | Impact dashboard | Administrator checks records |

## 3. Requirements derived from published research

FSSAI's 2019 surplus-food regulations state that unsafe food must not be distributed and that food must be handed over in time for consumption within its usable shelf life. The schedule addresses segregation, appropriate packing, hygienic storage and transport, and timely coordination.

The resulting project requirements are:
1. Store preparation and use-by information when available and verified.
2. Store quantity and unit.
3. Record reported storage and packaging conditions.
4. Keep a coordinator review step before a match is treated as actionable.
5. Record recipient acceptance separately from a system-generated match.
6. Record pickup and delivery separately.
7. Do not describe the application as a food-safety certification tool.

IFSA's published material describes a national initiative connecting donors, recovery agencies and beneficiaries. The project should complement existing networks and verify local recipient organisations rather than inventing a directory.

UNEP's Food Waste Index Report 2024 emphasises measurement across household, food-service and retail sectors. The CSV therefore retains source category, date, food category, quantity and provenance.

## 4. Observation protocol

This is a protocol, not a record that a visit occurred.

- Select a mess, restaurant, cafeteria or household with permission to observe.
- Observe for at least 20 minutes if required by the assignment.
- Separate untouched surplus from plate waste and spoiled food.
- Record the time and exact food item.
- Record weight from a scale where possible; otherwise label it as an estimate and note who estimated it.
- Ask how food is stored and who decides whether it can be shared.
- Do not handle or distribute food unless authorised and appropriately trained.
- Ask whether the donor currently has a collection arrangement.
- Obtain permission before taking photos or recording identifiable details.

## 5. Interview guide

Suggested roles include a mess manager, cook, restaurant manager, NGO coordinator or community kitchen organiser. These are proposed questions; no answers are attributed to a real person.

1. What happens to untouched surplus after meal service?
2. How do you distinguish untouched surplus from plate returns?
3. Who decides whether surplus can be donated?
4. How do you measure quantity?
5. How are preparation time, storage and use-by details tracked?
6. Does an NGO or recovery organisation currently collect food?
7. What collection timing and transport arrangements are needed?
8. What is the biggest coordination problem in the current process?
9. What information would make a digital listing useful?
10. What would make you unwilling or unable to use such a system?

## 6. Evidence register

| Evidence item | Repository status | What it supports |
|---|---|---|
| FSSAI 2019 regulations | Official source reviewed for this report | Regulatory design requirements |
| IFSA official website | Official source reviewed for this report | Existing national initiative and stakeholder model |
| UNEP Food Waste Index 2024 | Public report reviewed for this report | Measurement rationale and global context |
| 24 rows in data/data.csv | Synthetic demonstration records | Dashboard and CSV testing only |
| Physical site observation | Not documented / not verified | No local observation claim |
| Interview with donor or recipient | Not documented / not verified | No stakeholder quote or local workflow claim |
| Timestamped field photographs | Not present | SVG project artwork is not fieldwork evidence |
| Confirmed donation handover | Not documented | No meals-delivered impact claim |

## 7. Local primary-evidence register

No verifiable primary field evidence was supplied for this repository update. These values are therefore recorded as not recorded.

| Required field | Record |
|---|---|
| Site name and area | Not recorded |
| Visit date | Not recorded |
| Start/end time | Not recorded |
| Observation duration | Not recorded |
| Person interviewed and role | Not recorded |
| Interview date/time | Not recorded |
| Three stakeholder statements | Not recorded |
| Measured surplus quantity | Not recorded |
| Photo 1 and timestamp | Not recorded |
| Photo 2 and timestamp | Not recorded |
| Permission for notes/photos | Not recorded |

## 8. Product decisions from this case study

A successful algorithmic match must not be treated as a donation. The lifecycle needs separate states for listing, review, match suggestion, recipient acceptance, pickup and confirmed delivery. This prevents the dashboard from counting uncollected food as impact.

The data model should preserve provenance and measurement method. A generated example row, staff estimate and scale measurement must never be indistinguishable.

## 9. Conclusion

The desk research and hypothetical workflow provide a grounded requirements basis for the Mess2Meal prototype. They support a system that records surplus details, helps coordinators shortlist recipients and tracks a handover. They do not establish that a local donor or recipient has been interviewed, that a visit occurred, or that food was donated.

See research.md for the source list and official links.
