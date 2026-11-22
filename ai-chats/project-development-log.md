# Mess2Meal — development session summary

This is a companion summary to the AI conversation notes in README.md. It groups the main development discussions by outcome and records the decisions that shaped the prototype. It is not a verbatim transcript.

## Session 1 — Turning the idea into an application

**Discussion:** How can surplus food from messes, hostels, restaurants and households be listed and connected with possible recipients?

**Approach considered:** A dashboard, backend API, persistent records and a matching workflow.

**Project direction:** FastAPI for API routes, Streamlit for the dashboard, SQLite for local persistence and Pydantic for request validation.

## Session 2 — Recipient suggestions

**Discussion:** What makes a recipient suitable for a particular food listing, and how can the result be explained?

**Approach considered:** Filter by listing availability, best-before time, storage description, recipient activity, category preference and capacity. Rank eligible results using urgency and coordinator-entered distance.

**Project direction:** A rule-based matching function that returns scores and reasons. Human review remains necessary; the score is not a food-safety judgement.

## Session 3 — Dashboard test data

**Discussion:** How can the dashboard and charts be demonstrated across several types of food sources?

**Approach considered:** A single CSV with consistent fields and sample categories.

**Project direction:** 24 synthetic demonstration records in data/data.csv, covering college messes, hostel messes, restaurants, cafes/canteens and households. Each row is marked SYNTHETIC_DEMO_ONLY.

## Session 4 — Documentation and visual explanation

**Discussion:** What should a reviewer see first, and how can the architecture and donation process be made clear?

**Approach considered:** A README with setup steps, API details, feature summary, Mermaid diagrams and supporting SVG illustrations.

**Project direction:** A structured README and project-specific visual assets.

## Session 5 — Operational boundaries

**Discussion:** How should the documentation describe the intended real-world process without inventing fieldwork?

**Approach considered:** Document user roles, each handover stage, required information, risks and validation status. Keep primary field evidence separate from desk research and software design.

**Project direction:** An operational workflow document that explicitly identifies features and activities that are not yet verified or implemented.

## Verification checklist

- [ ] Run the API and dashboard locally.
- [ ] Run the test suite and review its output.
- [ ] Compare the repository against the original project brief.
- [ ] Verify each documented endpoint against the running API.
- [ ] Keep synthetic data provenance labels intact.
- [ ] Add genuine screenshots only after running the application.
- [ ] Add actual field evidence only if it has been collected with appropriate permission.
