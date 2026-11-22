# Research report — Mess2Meal

**Project:** Python-based surplus-food coordination prototype  
**Research type:** Secondary research and product-scope analysis  
**Geographic context:** India; a specific local donor/recipient network has not been verified in this repository  
**Evidence boundary:** This report uses published institutional sources. It does not claim a local site visit, NGO interview, survey or measured local food-waste quantity.

## 1. Executive summary

Mess2Meal is a proposed coordination tool for recording surplus food from college messes, hostel kitchens, restaurants, cafeterias and households, then helping an authorised coordinator identify potential recipient organisations.

The research points to two core requirements:

1. Food rescue needs safe handling and a time-sensitive handover. India's Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019 place responsibilities on donors and surplus-food distribution organisations. Unsafe food must not be distributed, and surplus must be handed over in time for consumption within its usable shelf life.
2. Food-waste measurement needs consistent data. UNEP's Food Waste Index Report 2024 stresses measurement across household, food-service and retail sectors and the need for baselines to track progress.

India already has a national coordination initiative: the Indian Food Sharing Alliance (IFSA), associated with FSSAI's Save Food, Share Food, Share Joy programme. Mess2Meal should be positioned as a small local workflow prototype, not as the first or only food donation network.

## 2. Problem context

Surplus can arise when prepared quantities exceed demand, customer demand changes, or households prepare more than they consume. Community kitchens, shelters and local support organisations may need timely access to food.

The practical challenge is not simply finding someone who wants food. A donation workflow also needs a donor and responsible contact, clear food description and quantity, preparation and time information, appropriate packaging/storage/transport, a recipient able to accept the quantity within the available time, and a confirmed handover record.

The prototype focuses on coordination and traceability. It does not make food safe, inspect kitchens or guarantee delivery.

## 2.1 Five-line local problem statement — provisional, not yet field-verified

> **Important:** The following is a project hypothesis based on the software's intended use case. It is not evidence that the author personally observed this problem in the last seven days. Replace or confirm it only after a real nearby visit and conversation.

1. A nearby food-service outlet may have prepared food left over when actual demand is lower than expected.
2. The person responsible for the outlet may need to decide quickly what can be safely retained, used or offered for collection.
3. Finding a suitable recipient in time may require checking availability, accepted food categories and capacity.
4. Informal coordination can leave important details such as quantity, preparation time and collection status scattered across conversations.
5. Mess2Meal proposes one simple record and recipient-shortlisting workflow, subject to validation with one real local person.

**Required before submission:** Add the actual place, date, the person's role and the specific problem they described. If the person does not confirm this hypothesis, rewrite the five lines to reflect what they actually said.

## 2.2 Two existing approaches and their local fit — validation pending

| Existing approach | What it offers | Potential mismatch for the proposed small local workflow | What must be checked with the real person |
|---|---|---|---|
| Indian Food Sharing Alliance (IFSA) | A wider food-sharing initiative connecting donors, beneficiaries and recovery stakeholders; see the official IFSA sources in Section 3.2. | A national initiative may not by itself tell us whether a particular nearby outlet has an active, reachable collection partner at the exact time surplus is available. This is a local-coverage question, not a claim that IFSA is ineffective. | Has the person heard of IFSA? Have they used it or contacted a recovery organisation? Was a suitable local partner available? |
| Direct phone calls / messaging between a donor and a known contact | A lightweight way to notify someone without learning a new application. | Details can remain in separate messages, and the donor may need to repeat quantity, timing, handling and collection updates. Whether this causes difficulty at the selected site is not yet known. | Does the person currently use calls or WhatsApp? Which details are difficult to track? Would a structured listing actually save time? |

**Local-fit conclusion:** No real person has yet been interviewed in the repository evidence. Therefore, neither mismatch above is confirmed for the user's chosen person. Record the person's answers in `fieldwork.md` and revise this comparison before submission.


## 3. Evidence from published sources

### 3.1 FSSAI — surplus-food recovery and distribution regulations (2019)

**Source:** Food Safety and Standards Authority of India, Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019.  
Official regulation: https://www.fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Surplus_Food_06_08_2019.pdf  
FSSAI regulations index: https://fssai.gov.in/food-law/regulations

The regulations state that a food business operator may donate surplus food to a surplus-food distribution organisation in accordance with the regulations. Donors must not distribute unsafe food. Food should be handed over with enough time for it to reach people for consumption within its shelf life.

The schedule addresses segregation of perishable and non-perishable food, appropriate packing to prevent contamination, hygienic storage at suitable temperatures, keeping surplus away from waste material, advance notice to the receiving organisation, clean covered containers and hygienic transport at appropriate temperatures.

**Design implications:**
- Capture donor/source identity and a responsible contact reference.
- Capture food category, quantity, preparation time and donor-provided use-by information where known.
- Capture reported storage and packaging information.
- Support time-sensitive listings and a pickup/handover status.
- Require coordinator review; do not label an algorithmic match as food-safety approval.
- Do not recommend unsafe, expired or unverifiable food for donation.

This is a software-design interpretation, not legal advice or compliance certification.

### 3.2 FSSAI — Indian Food Sharing Alliance (IFSA)

**Sources:**
- IFSA overview: https://sharefood.eatrightindia.gov.in/what_ifsa.html
- IFSA homepage: https://sharefood.eatrightindia.gov.in/
- Donor information: https://sharefood.eatrightindia.gov.in/donor.html
- Beneficiary information: https://sharefood.eatrightindia.gov.in/beneficiary.html

Official IFSA material describes a collaborative initiative associated with FSSAI that brings together food businesses, food-sharing organisations, recovery agencies, NGOs, volunteers, government and local bodies. Its stated aims include reducing food waste, facilitating safe distribution of surplus food and connecting trained food recovery agencies with food chains. The site provides pathways for food donors and beneficiaries.

**Design implications:**
- Complement existing food recovery networks rather than claim to replace them.
- Represent verified organisations, not invented NGO names.
- Record whether a recipient has confirmed acceptance.
- A future integration could direct donors to existing recovery networks rather than create a disconnected parallel system.

The existence of IFSA does not prove that a particular mess or neighbourhood has an active collection partner. Local coverage and availability need direct verification.

### 3.3 UNEP — Food Waste Index Report 2024

**Sources:**
- Report page: https://wedocs.unep.org/items/dbe2cd4c-8384-4636-8359-5847f42b9711
- Key messages PDF: https://wedocs.unep.org/bitstream/handle/20.500.11822/45275/Food-Waste-Index-2024-key-messages.pdf?sequence=8

The report estimates that 1.05 billion tonnes of food waste were generated globally in 2022 at retail, food-service and household levels. Its key messages attribute 60% of this consumer-level food waste to households, 28% to food service and 12% to retail. The report highlights improved measurement, comparable methods, baselines and multi-stakeholder collaboration.

**Design implications:**
- Keep donor source category as a structured field.
- Record observation date, food category, quantity and measurement method.
- Distinguish measured quantities from staff estimates and visual estimates.
- Keep missing values explicit.
- Report only confirmed handovers as delivered impact.
- Never use synthetic CSV totals as real food-waste reduction or meals-served claims.

These are global estimates, not measurements of a particular Indian college, city or neighbourhood.

## 3.4 Two source-reading notes to verify before submission

> These concise notes summarise the cited material for review. The assignment asks for sources the student actually read. Read the linked originals yourself and edit these notes to reflect your own understanding before claiming that requirement as complete.

**Source 1 — FSSAI, Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019**

- The regulations establish responsibilities for surplus-food donors and distribution organisations and prohibit distribution of unsafe food.
- The schedule addresses handling, packing, storage, notice to recipients and hygienic transport.
- For Mess2Meal, this means a match score must never be presented as food-safety approval; human review and timely handover remain necessary.

**Source 2 — UNEP, Food Waste Index Report 2024**

- The report measures food waste across household, food-service and retail sectors and highlights the need for comparable measurement.
- Its global estimates provide context, but they do not measure food waste at the selected college, shop or neighbourhood.
- For Mess2Meal, every local quantity needs its own date, source and measurement method, and synthetic examples must not be presented as impact.

## 4. Existing approach and project positioning

| Existing approach | What the published source establishes | What Mess2Meal can contribute |
|---|---|---|
| FSSAI surplus-food regulations | Regulatory framework for safe recovery and distribution | Structured listing fields and human-review workflow |
| Indian Food Sharing Alliance | National collaborative initiative connecting stakeholders and recovery networks | Small local coordination interface and traceable listing lifecycle |
| UNEP Food Waste Index | Measurement framework and global food-waste evidence | Consistent records for source, date, category, quantity and method |

Mess2Meal is not a substitute for FSSAI, IFSA, a licensed food business, NGO operating procedures or a food-safety professional.

## 5. Proposed users and needs

| User group | Need | Prototype support |
|---|---|---|
| Mess / cafeteria operator | Record surplus quickly and share accurate details | Food listing form |
| Restaurant / cafe | Offer suitable surplus before it becomes unusable | Time and quantity fields |
| Household donor | Share excess prepared food through a responsible channel | Simple donor listing |
| NGO / community kitchen | See available food and decide whether it can accept it | Recipient profile and match suggestions |
| Volunteer / coordinator | Coordinate timing and record collection | Status tracking and handover record |
| Project administrator | Review records and understand activity | Dashboard and impact summary |

These are proposed user roles, not people interviewed for this project.

## 6. Proposed end-to-end workflow

1. A donor creates a surplus listing.
2. The system validates required fields and basic eligibility information.
3. An authorised coordinator reviews the food details and handling requirements.
4. Matching logic filters potential recipients by availability, category and capacity.
5. The recipient or coordinator confirms acceptance.
6. Pickup time and responsibility are agreed by the people involved.
7. Handover is confirmed and listing status is updated.
8. Dashboard counts the donation as delivered only after confirmation.

A match score is a prioritisation aid, not a guarantee of acceptance, safe food, pickup or delivery.

## 7. Data and measurement plan

The prototype CSV includes date, time, location label, source type, food name, quantity in kilograms, preparation time, best-before information, storage description, recipient/contact reference, notes and data origin.

For credible future analysis:
- Keep kilograms as the standard quantity unit.
- Record whether a value was weighed, counted or estimated.
- Keep untouched surplus separate from plate waste and spoiled food.
- Record date/time consistently.
- Use not recorded for genuinely missing values.
- Retain provenance for synthetic versus collected records.
- Count delivered quantity only after a confirmed handover.

The current 24 CSV entries are synthetic examples, not a baseline.

## 8. Risks, safeguards and limitations

| Risk | Why it matters | Prototype safeguard / limitation |
|---|---|---|
| Unsafe or expired food | Can cause harm | Human review; software cannot certify safety |
| Incorrect quantity or time | Can lead to failed pickups | Record measurement method and source |
| Recipient unavailable | Food may remain undistributed | Recipient confirmation before accepted status |
| Transport delay | Food may pass its usable time window | Record pickup timing and require human coordination |
| Personal data exposure | Donors and recipients can be identifiable | Minimise contact data and use permission-based sharing |
| False impact claims | Synthetic/unconfirmed records mislead | Count confirmed deliveries only; label synthetic data |
| Uneven local network coverage | Software cannot create a nearby NGO | Verify recipient organisations before operational use |

## 9. Research conclusion

The reviewed sources support safe, coordinated surplus-food recovery and consistent measurement. They also show that India already has a national food-sharing initiative and a regulatory framework. Mess2Meal's defensible contribution is a lightweight Python prototype for structured listings, recipient shortlisting, status tracking and transparent records.

The strongest next research step for local deployment is to verify one donor workflow and one recipient workflow in the selected area, with permission, and use those findings to revise the prototype. No local interview, visit, NGO partnership or real donation is claimed in this report.

## 10. References

1. FSSAI. Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019. https://www.fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Surplus_Food_06_08_2019.pdf
2. FSSAI. Food Law — Regulations. https://fssai.gov.in/food-law/regulations
3. FSSAI / IFSA. What is IFSA? https://sharefood.eatrightindia.gov.in/what_ifsa.html
4. FSSAI / IFSA. Donor information. https://sharefood.eatrightindia.gov.in/donor.html
5. FSSAI / IFSA. Beneficiary information. https://sharefood.eatrightindia.gov.in/beneficiary.html
6. UNEP. Food Waste Index Report 2024. March 2024. https://wedocs.unep.org/items/dbe2cd4c-8384-4636-8359-5847f42b9711
7. UNEP. Food Waste Index Report 2024 — Key Messages. https://wedocs.unep.org/bitstream/handle/20.500.11822/45275/Food-Waste-Index-2024-key-messages.pdf?sequence=8
