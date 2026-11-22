# Mess2Meal dataset — data dictionary and usage guide

## Current dataset

- File: data.csv
- Current records: 24
- Columns: 12
- Provenance: every current row is marked SYNTHETIC_DEMO_ONLY.
- Categories: college mess, hostel mess, restaurant, cafe/bakery, canteen and household.

Locations, quantities, recipients and timestamps are illustrative. They are not observations from a site visit, real donor records or confirmed donations.

## Data dictionary

| Column | Meaning | Format / unit |
|---|---|---|
| date | Date recorded | YYYY-MM-DD |
| time | Local time recorded | HH:MM, 24-hour |
| location | Donor site or agreed location label | Text; avoid private addresses |
| source_type | Food source category | Controlled category |
| food_name | Food item | Text |
| quantity_kg | Available quantity | Numeric kilograms |
| prepared_at | Preparation time, if known | HH:MM |
| best_before | Donor-provided use-by information | Preserve its exact meaning |
| storage_condition | Reported handling/storage description | Text; not safety certification |
| recipient_or_contact | Recipient label or authorised reference | Do not publish private contact details |
| observation_notes | Context, estimate method and uncertainty | Text |
| data_origin | Provenance | SYNTHETIC_DEMO_ONLY or documented genuine collection label |

## Data quality rules

1. Keep one row per food item and listing event.
2. Use kilograms consistently.
3. Distinguish measured quantities from estimates; describe the method in notes.
4. Use not recorded when a value is genuinely unavailable. Never invent missing times or counts.
5. Distinguish untouched surplus from plate waste, spoiled food and food already served.
6. Preserve the donor's exact meaning of preparation, use-by and best-before information.
7. Do not treat a storage description as proof that food is safe.
8. Keep synthetic and genuinely collected records distinguishable.
9. Do not publish personal phone numbers, private addresses or identifiable details without permission.

## Inspect the CSV

```bash
python -c "import pandas as pd; d=pd.read_csv('data/data.csv'); print(d.head()); print(d['source_type'].value_counts())"
```

The sample can demonstrate CSV loading, tables, grouping and charts. It cannot establish local food-waste quantities, actual donor/NGO participation, completed collection, meals served or environmental impact.

Never remove the synthetic marker from generated rows to make them appear to be field observations.
