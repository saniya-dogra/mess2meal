# Data files — read before using

This project deliberately keeps real field evidence separate from software demo records.

## `data.csv` — real field observations

- This is the file for your own 20+ observations collected at the actual mess, restaurant, cafe, household or community location.
- Record the actual date, time, location, food, quantity and storage details you observed.
- Add the collection method and limitations in `fieldwork.md`.
- Never invent missing measurements. Use `not recorded` when a value genuinely was not collected.
- Obtain permission before photos or personal information are recorded.

## `demo_data.csv` — synthetic test data

- Contains 24 illustrative rows across college messes, hostel messes, restaurants, cafes/canteens and household food.
- Locations and recipient names are fictional examples.
- Quantities and timestamps are invented to help test the dashboard and charts.
- Every row is marked `SYNTHETIC_DEMO_ONLY`.
- **Do not count these rows toward the assignment's 20 real entries. Do not describe them as fieldwork.**

The dashboard lets you switch between the real-observation file and the demo file so the two datasets do not get mixed.
