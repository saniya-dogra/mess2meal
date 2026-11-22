# Research report — Mess2Meal

**Project:** Python-based surplus-food coordination prototype  
**Research type:** Secondary research and product-scope analysis, written from my project perspective  
**Geographic context:** India; a specific local donor/recipient network has not been verified in this repository  
**My research approach:** I reviewed published institutional sources and compared existing food-recovery approaches to understand the problem and define the scope of Mess2Meal. This is desk research; I have not used it to claim a local site visit, NGO interview, survey or personally measured food-waste quantity.

## 1. Executive summary

Mess2Meal is a proposed coordination tool for recording surplus food from college messes, hostel kitchens, restaurants, cafeterias and households, then helping an authorised coordinator identify potential recipient organisations.

From this research, I identified two core requirements:

1. Food rescue needs safe handling and a time-sensitive handover. India's Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019 place responsibilities on donors and surplus-food distribution organisations. Unsafe food must not be distributed, and surplus must be handed over in time for consumption within its usable shelf life.
2. Food-waste measurement needs consistent data. UNEP's Food Waste Index Report 2024 stresses measurement across household, food-service and retail sectors and the need for baselines to track progress.

I also found that India already has a national coordination initiative: the Indian Food Sharing Alliance (IFSA), associated with FSSAI's Save Food, Share Food, Share Joy programme. Mess2Meal should be positioned as a small local workflow prototype, not as the first or only food donation network.

## 2. Problem context

Surplus can arise when prepared quantities exceed demand, customer demand changes, or households prepare more than they consume. Community kitchens, shelters and local support organisations may need timely access to food.

The practical challenge is not simply finding someone who wants food. A donation workflow also needs a donor and responsible contact, clear food description and quantity, preparation and time information, appropriate packaging/storage/transport, a recipient able to accept the quantity within the available time, and a confirmed handover record.

I have therefore scoped my prototype around coordination and traceability. It does not make food safe, inspect kitchens or guarantee delivery.

## 2.1 Five-line local problem statement — provisional, not yet field-verified

 > **My current status:** I developed the following five lines as a hypothesis from my desk research and software scope. I have not yet verified them through a local visit or conversation, so I will revise them if primary research gives me different findings.

1. A nearby food-service outlet may have prepared food left over when actual demand is lower than expected.
2. The person responsible for the outlet may need to decide quickly what can be safely retained, used or offered for collection.
3. Finding a suitable recipient in time may require checking availability, accepted food categories and capacity.
4. Informal coordination can leave important details such as quantity, preparation time and collection status scattered across conversations.
5. Mess2Meal proposes one simple record and recipient-shortlisting workflow, subject to validation with one real local person.

**My next step:** I need to add the actual place, date, person's role and the problem they describe after I complete a local visit. If their experience does not support this hypothesis, I will rewrite these five lines.

## 2.2 Existing solutions and comparison

I compared these approaches using publicly available programme information reviewed on 22 November 2026. This tells me how the programmes describe their work, but it does not confirm whether a particular chapter or collection route is active near my chosen site.

| Existing solution | Publicly described model | Strengths | What Mess2Meal should not assume / possible gap for a small outlet |
|---|---|---|---|
| **Indian Food Sharing Alliance (IFSA)** | FSSAI's IFSA initiative connects food businesses, food-sharing networks, food recovery agencies, NGOs, volunteers and beneficiaries. It provides donor and beneficiary registration pathways and a directory of food recovery agencies. | Established national coordination framework; donor registration asks about business details, food categories, logistics and quality-check facilities; agency directory indicates different organisation capabilities. | The public directory is not proof that a listed agency can collect from a particular outlet at a particular time. Donor registration and a network directory do not themselves provide a live listing-level workflow for this prototype's chosen location. Verify current local coverage and contact process before claiming a gap. |
| **Robin Hood Army (RHA)** | A volunteer-led, zero-funds organisation that collects surplus food from restaurants and communities and distributes it to people in need. Its public description says local chapters are run by volunteers; its FAQ describes volunteers serving groups such as homeless families, orphanages, public-hospital patients and old-age homes. | A practical community redistribution model that relies on local volunteers and relationships with food donors. | The public information does not establish real-time availability, capacity or pickup status for every local chapter. Do not claim that RHA is absent or ineffective in the project area without contacting a relevant chapter. |
| **Direct calls / messaging between a donor and a known contact** | Informal one-to-one coordination by phone or messaging. | Familiar, low setup cost and can work well when the donor and recipient already know each other. | Listing details, updates and handover confirmation may be spread across messages. Whether this creates a real problem at the selected site must be established through interview, not assumed. |

### What Mess2Meal can contribute

Mess2Meal is not a replacement for IFSA or RHA. Its potential contribution is a small, transparent record for one local workflow: capture a listing, show recipient eligibility reasons, record coordinator-entered distance, and preserve status history through handover. This is useful only if a real donor/coordinator confirms that the workflow solves a problem they actually experience.

### Local validation questions

Before claiming that an existing solution does not fit the selected person, ask:
1. Which organisation or person do you contact today when surplus food is available?
2. Have you tried IFSA, Robin Hood Army or another food recovery organisation?
3. How long does it usually take to find a recipient and arrange collection?
4. What information is repeatedly missing or needs to be shared again?
5. Would a simple listing and status record improve the process, or is the current method already sufficient?

**What I can conclude:** This comparison is secondary research, not an interview or local service audit. I cannot conclude that an organisation is unavailable in Srinagar or another locality without checking directly.


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

## 3.4 Focused source notes from public research

**Source A — FSSAI, Food Safety and Standards (Recovery and Distribution of Surplus Food) Regulations, 2019**

Official links:
- Regulation PDF: https://www.fssai.gov.in/upload/uploadfiles/files/Gazette_Notification_Surplus_Food_06_08_2019.pdf
- FSSAI regulations index: https://fssai.gov.in/food-law/regulations

Research notes:
1. The regulation permits food business operators with surplus food to donate it to a surplus-food distribution organisation in accordance with the regulation.
2. Donors must not distribute unsafe food. Food must be handed over with enough time for recipients to consume it within its shelf life.
3. Schedule I addresses segregation, suitable packing, hygienic storage, advance notice, clean covered containers and appropriate transport conditions.

**Design decision:** Mess2Meal records preparation/best-before information and reported storage conditions, and it treats matching as a coordination aid only. The software cannot inspect food, certify safety or establish legal compliance.

**Source B — FSSAI / Indian Food Sharing Alliance (IFSA), “What is IFSA?” and donor registration**

Official links:
- IFSA overview: https://sharefood.eatrightindia.gov.in/what_ifsa.html
- Donor registration fields: https://sharefood.eatrightindia.gov.in/donor.html
- Agency directory: https://sharefood.eatrightindia.gov.in/agency-list.html

Research notes:
1. IFSA describes itself as an FSSAI initiative intended to connect food-sharing organisations, food recovery agencies, NGOs and food businesses.
2. Its donor registration asks for business identity and contact information, FSSAI registration, business type, food categories, whether surplus food is available, and whether logistics and quality-check facilities are available.
3. The public agency directory lists organisations and their stated recovery/distribution capabilities. A directory entry does not prove that a specific organisation is currently available for a specific pickup.

**Design decision:** A future production version should verify organisations and their current coverage/capacity. Mess2Meal's sample recipient records must remain labelled as demo records until a real organisation has consented to be listed.

**Additional comparator — Robin Hood Army (RHA)**

Official links:
- About: https://robinhoodarmy.in/
- FAQ: https://robinhoodarmy.in/faqs

RHA publicly describes a volunteer-based, zero-funds model that collects surplus food from restaurants and communities and distributes it to people in need. Its local-chapter model is relevant as an existing community-led alternative. Its public pages do not prove current availability in the project owner's exact locality; local contact and confirmation would be required before drawing that conclusion.

**Research method and limitation:** These notes were prepared from the linked public webpages and regulation text, accessed 22 November 2026. They are secondary research summaries. The project owner should open and read the original sources and add any personal observations required by the assignment. They do not substitute for primary fieldwork.

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
11. FSSAI / IFSA. Food Donating Agencies — state-wise agency directory. https://sharefood.eatrightindia.gov.in/agency-list.html
12. FSSAI / IFSA. Food Business — recovery agency guidance for collection from caterers. https://sharefood.eatrightindia.gov.in/regulation-food-business.html
13. Robin Hood Army. About the organisation and its surplus-food collection model. https://www.robinhoodarmy.com/sites/main/about
14. Robin Hood Army. Frequently Asked Questions. https://robinhoodarmy.in/faqs
