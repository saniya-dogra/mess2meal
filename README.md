<div align="center">

# Mess2Meal

**A Python-based surplus food coordination platform**

Connect food donors with community organisations through structured listings, explainable recipient matching and delivery tracking.

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=16&pause=1800&color=16866A&center=true&vCenter=true&width=560&lines=Rescue+surplus.+Coordinate+responsibly.;Make+every+available+meal+count." alt="Animated project tagline" />

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)

</div>

---

## Overview

Food prepared by college messes, hostels, restaurants, cafeterias and households can remain unused while NGOs, shelters and community kitchens need timely food support. Coordinating a donation requires more than publishing an offer: quantity, preparation time, storage details, recipient capacity and pickup timing all matter.

**Mess2Meal** is a local-first prototype that brings these steps into one workflow. Donors can register surplus food, coordinators can review listings and view ranked recipient suggestions, and confirmed handovers can be reflected in delivery metrics.

The application is a coordination aid. It does not certify food safety, independently verify organisations or arrange physical transport.

## Product workflow

![Mess2Meal donation lifecycle](assets/donation-lifecycle.svg)

\`\`\`mermaid
flowchart TD
    A([Surplus food identified]) --> B[Create food listing]
    B --> C[Validate listing details]
    C --> D{Eligible for matching?}
    D -->|No| E[Hold for review / exclude]
    D -->|Yes| F[Find active recipients]
    F --> G[Filter by category and capacity]
    G --> H[Rank by urgency and distance]
    H --> I[Coordinator reviews suggestions]
    I --> J[Recipient acceptance and pickup coordination]
    J --> K[Human-confirmed handover]
    K --> L([Update delivery status and impact])
\`\`\`

## Architecture

\`\`\`mermaid
flowchart LR
    U[Donor / Coordinator] --> S[Streamlit dashboard]
    S -->|HTTP requests| A[FastAPI backend]
    A --> V[Pydantic validation]
    A --> M[Matching engine]
    A --> D[(SQLite)]
    M --> A
    S --> P[Pandas]
    P --> C[data/data.csv]
\`\`\`

| Layer | Implementation | Responsibility |
|---|---|---|
| User interface | Streamlit | Food listing, recipient registration, listings, matches and impact views |
| REST API | FastAPI | Validated endpoints for food, recipients, matching and status |
| Validation | Pydantic | Request schemas and field constraints |
| Business logic | Python | Eligibility checks and recipient ranking |
| Persistence | SQLite | Food listings, recipient records and status |
| Data analysis | Pandas | CSV loading and dashboard summaries |
| Testing | Pytest | Automated matching and application checks |

## Core capabilities

### Food donation management
- Create surplus-food listings with category, quantity, preparation time, best-before time, storage description and pickup location.
- Retrieve current listings through the API.
- Update a listing's donation status.

### Recipient management
- Register an NGO, shelter, community kitchen or other recipient group.
- Store accepted food categories, capacity, urgency and active status.
- Retrieve recipient records for coordinator review.

### Explainable matching
The matching module applies these rules:

1. The listing must be available and its best-before time must be in the future.
2. A blank storage description or one containing configured unsafe terms is excluded.
3. Only active recipients are considered.
4. Recipient capacity must meet the listed quantity.
5. Food category must match recipient preferences, unless the recipient accepts all categories.
6. Eligible recipients are ranked using urgency, coordinator-entered distance and capacity.
7. Each result includes a score and human-readable reasons.

**Important:** These checks are preliminary software filters, not food-safety inspection or certification. A responsible person must verify food condition, handling, recipient suitability and applicable requirements before redistribution.

## Technology stack

- **Language:** Python
- **Backend:** FastAPI, Uvicorn, Pydantic
- **Frontend:** Streamlit
- **Database:** SQLite
- **Data handling:** Pandas
- **HTTP client:** Requests
- **Testing:** Pytest, HTTPX
- **Documentation:** Markdown and Mermaid

## Repository structure

\`\`\`text
mess2meal/
├── app/
│   ├── main.py
│   └── api/
│       ├── main.py
│       ├── database.py
│       ├── matching.py
│       ├── schemas.py
│       └── services.py
├── assets/
│   ├── food-rescue-hero.svg
│   ├── donation-lifecycle.svg
│   ├── dashboard-concept.svg
│   └── README.md
├── data/
│   ├── data.csv
│   └── README.md
├── docs/
│   ├── architecture.md
│   └── flowcharts/
├── tests/
│   └── test_matching.py
├── ai-chats/
├── research.md
├── fieldwork.md
├── reflection.md
├── requirements.txt
└── README.md
\`\`\`

## Getting started

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/saniya-dogra/mess2meal.git
cd mess2meal
\`\`\`

### 2. Create a virtual environment

**Windows PowerShell**
\`\`\`powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
\`\`\`

**macOS / Linux**
\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
\`\`\`

### 3. Install dependencies

\`\`\`bash
python -m pip install --upgrade pip
pip install -r requirements.txt
\`\`\`

### 4. Start the API

\`\`\`bash
uvicorn app.api.main:app --reload
\`\`\`

API base URL: http://127.0.0.1:8000  
Interactive API documentation: http://127.0.0.1:8000/docs

### 5. Start the dashboard

Open a second terminal with the virtual environment activated:

\`\`\`bash
streamlit run app/main.py
\`\`\`

### 6. Run tests

\`\`\`bash
pytest -v
\`\`\`

## API reference

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | API health check |
| POST | /food | Create a food listing |
| GET | /food | List food records |
| POST | /recipients | Register a recipient |
| GET | /recipients | List recipients |
| GET | /food/{food_id}/matches | Retrieve ranked recipient suggestions |
| PATCH | /food/{food_id}/status | Update donation status |
| GET | /impact | Retrieve delivered-only impact totals |

## Sample dataset

[data/data.csv](data/data.csv) contains 24 **synthetic demonstration records** covering college messes, hostel messes, restaurants, cafes/bakeries, canteens and households. Every row is marked SYNTHETIC_DEMO_ONLY.

The sample data demonstrates CSV loading and dashboard visualisations. It is not a record of actual food waste, real donors, NGO partnerships or completed donations. Do not use its quantities as real-world impact figures.

See [data/README.md](data/README.md) for the data dictionary, provenance rules and usage notes.

## Project documentation

- [Architecture](docs/architecture.md) — application components and data flow.
- [Research](research.md) — secondary research, food recovery context and design implications.
- [Operational workflow](fieldwork.md) — use-case analysis, operational requirements and validation boundaries.
- [Development reflection](reflection.md) — engineering decisions, trade-offs and lessons from building the prototype.
- [AI-assisted development log](ai-chats/project-development-log.md) — summary of AI-assisted project work.
- [Visual assets](assets/README.md) — diagrams and illustrative graphics.

## Security, safety and limitations

- The prototype is intended for local demonstration and evaluation, not production deployment.
- Authentication and role-based access control are not currently implemented.
- Recipient records are not independently verified.
- Distance is coordinator-entered; there is no GPS or route optimisation.
- No SMS, WhatsApp or automated NGO notification integration is implemented.
- SQLite is suitable for this local prototype, not a multi-tenant production deployment.
- Matching is not a food-safety decision. Human checks and applicable food-handling requirements remain essential.
- Contact information should be handled carefully and must not be exposed in public screenshots or sample datasets.

## Future improvements

- [ ] Role-based authentication for donors, recipients and coordinators.
- [ ] Recipient verification and consent-based onboarding.
- [ ] Pickup scheduling and volunteer coordination.
- [ ] Notification integration for accepted matches.
- [ ] Audit history for listing and handover status changes.
- [ ] Production database and deployment configuration.
- [ ] Privacy-aware reporting based only on verified deliveries.

---

<div align="center">

**Mess2Meal** · Rescue surplus. Coordinate responsibly. Reduce avoidable food waste.

<sub>Built with Python.</sub>

</div>
