# Mess2Meal — engineering reflection

## Project objective

Mess2Meal was developed as a Python-based prototype to make surplus-food coordination more structured. The intended users include food providers such as college messes, hostels, restaurants, cafeterias and households, along with NGOs, shelters and community kitchens that may be able to receive food.

The core engineering objective was to connect food listing, recipient management, matching and delivery tracking in one workflow rather than treating food donation as a simple form submission.

## Key engineering decisions

The application uses Streamlit for the user-facing dashboard and FastAPI for the backend API. This separation keeps the interface independent from the main business operations and makes the API available for future clients. Pydantic schemas validate incoming request data, while SQLite provides lightweight local persistence for the prototype.

The matching logic was kept rule-based and explainable. It filters listings by availability, best-before time and storage-description checks, then filters recipients by active status, capacity and food-category preference. Eligible recipients are ranked using urgency, coordinator-entered distance and capacity. The API returns reasons alongside the score so a coordinator can understand why a recipient appears in the shortlist.

A deliberate boundary is that matching is not food-safety certification. Software cannot inspect food or establish its handling history. The workflow therefore keeps human review and physical handover responsibility outside the algorithm.

## Data and evidence decisions

A small CSV dataset was included to make dashboard development and demonstration repeatable. Its 24 rows are synthetic examples across several food-source categories. They are explicitly marked SYNTHETIC_DEMO_ONLY so they cannot be confused with measured food waste, actual donors or completed donations.

The project documentation distinguishes secondary research from primary field evidence. Published FSSAI and UNEP material informs the workflow and data requirements, but it does not prove that a local NGO has partnered with the project or that food has been redistributed.

## Current limitations

The prototype is designed for local demonstration. It does not yet provide authentication, role-based access, independent recipient verification, automated notifications, GPS-based distance calculation, route planning or production deployment. The recipient distance used by the current API is a coordinator-supplied value. The dashboard and API rely on a local development setup.

The current workflow can generate recipient suggestions and record a status, but it does not arrange a physical pickup. Real-world operation would require verified organisations, clear collection responsibility, safe handling procedures, privacy controls and auditable handover confirmation.

## Next engineering priorities

1. Add authentication and role-based permissions for donors, recipients and coordinators.
2. Add explicit review, acceptance, pickup and handover states with an audit trail.
3. Verify recipient organisations and periodically refresh their capacity and availability.
4. Add notification and pickup scheduling workflows.
5. Move from local SQLite to a production database when deployment requirements are known.
6. Add privacy controls, secure configuration and deployment monitoring.
7. Validate the workflow with authorised stakeholders before using it for actual food redistribution.

## Closing reflection

The most important design lesson from Mess2Meal is that a useful matching result is only one part of a successful donation. Reliable coordination depends on accurate information, recipient confirmation, safe handling and a verified handover. The prototype provides a foundation for that workflow while keeping its current capabilities and limitations explicit.
