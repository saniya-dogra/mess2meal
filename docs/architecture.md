# Mess2Meal architecture

## Components
- Streamlit: Python dashboard for mess operators and coordinators.
- FastAPI: validates requests and exposes donation/recipient workflows.
- Pydantic: validates payload fields and basic constraints.
- Matching module: transparent eligibility filters and ranking reasons.
- SQLite: stores listings, recipients and donation state.
- Pandas: presents listing and impact summaries in the dashboard.

## Data flow
1. Operator submits surplus food through Streamlit.
2. Streamlit sends JSON to FastAPI.
3. Pydantic validates the request.
4. The service persists the listing in SQLite.
5. The coordinator requests matching suggestions.
6. Matching excludes expired or unsafe/incomplete listings and filters recipients by activity, category and capacity.
7. Coordinator confirms acceptance and handover; status is updated.
8. Delivered-only records contribute to impact totals.

## Trust and safety
Matching is not food-safety certification. A trained/authorised human must inspect food, verify handling and follow local regulations before redistribution. Contact details are sensitive and should not be placed in public CSVs or screenshots.
