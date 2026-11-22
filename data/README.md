# Mess2Meal dataset — data dictionary and usage guide

## Dataset overview
The single data.csv file is the CSV input used by the prototype dashboard.

- Current records: 24
- Format: UTF-8 CSV with 12 columns
- All current rows are synthetic demonstration records.
- Source categories: college mess, hostel mess, restaurant, cafe/bakery, canteen and household.
- Every current row carries the provenance marker SYNTHETIC_DEMO_ONLY.

Locations, recipient labels, quantities and timestamps are illustrative. They are not measured observations or confirmed donations.

## Data dictionary

| Column | Meaning | Format / unit |
|---|---|---|
| date | Date entry was recorded | YYYY-MM-DD |
| time | Local time of entry | 24-hour HH:MM |
| location | Donor site or agreed location label | Text; avoid private addresses |
| source_type | Type of food source | Controlled category |
| food_name | Food item listed | Text |
| quantity_kg | Available quantity | Numeric kilograms |
| prepared_at | Preparation time, if known | HH:MM |
| best_before | Donor-provided use-by information, if verified | Exact source meaning; never guess |
| storage_condition | Reported storage / handling description | Text; not a safety certification |
| recipient_or_contact | Intended recipient label or authorised contact reference | Text; no private phone numbers |
| observation_notes | Context, uncertainty and measurement method | Text |
| data_origin | Provenance label | SYNTHETIC_DEMO_ONLY for generated examples |

## Source categories represented

| Category | Example setting | Example items |
|---|---|---|
| College mess | Institutional meal service | Rice, rajma, chapati, curry |
| Hostel mess | Residential dining | Pulao, dal, raita |
| Restaurant | Commercial food service | Rice, chana masala, roti |
| Cafe / bakery | Cafe or bakery counter | Bread rolls, sandwiches |
| Canteen | Campus food counter | Lemon rice, sambar |
| Household | Home-prepared surplus | Dal, rice, sabzi, chapati |

These are category examples, not claims that the named sites or recipients exist.

## Data quality rules
1. Keep one row per food item and listing event.
2. Record date and time consistently.
3. Use kilograms as the standard quantity unit.
4. If a scale is unavailable, label the value as an estimate and describe the method in observation_notes.
5. Never convert a visual guess into a measured value.
6. Use not recorded when a value is genuinely unavailable.
7. Distinguish untouched surplus from plate waste, spoiled food and food already served.
8. Preserve the donor's exact meaning of preparation, use-by and best-before information.
9. Do not treat a storage description as proof that food is safe.
10. Do not publish personal phone numbers, private addresses or identifiable details without permission.
11. Keep synthetic and collected data distinguishable through provenance labels.

## Load and inspect the CSV

From the repository root:

    python -c "import pandas as pd; d=pd.read_csv('data/data.csv'); print(d.head()); print(d['source_type'].value_counts())"

The dashboard reads this single file. Keep the column names unchanged unless the dashboard and tests are updated too.

## What the sample can and cannot show

**It can demonstrate:** CSV loading, dashboard tables, grouping by source category, example food items, chart rendering and repeatable software tests.

**It cannot establish:** actual local food waste, real donor or NGO participation, actual collection or delivery, meals served, or environmental impact.

Do not calculate or advertise real-world impact from synthetic rows.

## Assignment and provenance note

The 24 current rows are synthetic test data. They do not count as primary fieldwork. If the assignment requires real observations, use genuinely collected or authorised records and preserve their source, date, measurement method, uncertainty and permission notes.

Never remove the synthetic marker from generated rows to make them look like field observations.
