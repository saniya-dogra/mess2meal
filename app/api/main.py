from fastapi import FastAPI, HTTPException
from .database import initialize_database, get_connection
from .schemas import FoodCreate, RecipientCreate, StatusUpdate
from .matching import rank_recipients
from . import services
import json

app = FastAPI(
    title="Mess2Meal API",
    description="A local-first food rescue and redistribution prototype.",
    version="1.0.0",
)


@app.on_event("startup")
def startup():
    initialize_database()


@app.get("/health")
def health():
    return {"status": "ok", "service": "Mess2Meal API"}


@app.post("/food", status_code=201)
def add_food(payload: FoodCreate):
    return services.create_food(payload.model_dump())


@app.get("/food")
def get_food():
    return services.list_food()


@app.post("/recipients", status_code=201)
def add_recipient(payload: RecipientCreate):
    return services.create_recipient(payload.model_dump())


@app.get("/recipients")
def get_recipients():
    return services.list_recipients()


@app.get("/food/{food_id}/matches")
def get_matches(food_id: int):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM food WHERE id=?", (food_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Food listing not found")
    food = dict(row)
    recipients = services.list_recipients()
    # Distance is intentionally supplied by an operator, not obtained from an API.
    for recipient in recipients:
        recipient["distance_km"] = 0
    return {"food_id": food_id, "matches": rank_recipients(food, recipients)}


@app.patch("/food/{food_id}/status")
def change_status(food_id: int, payload: StatusUpdate):
    updated = services.update_food_status(food_id, payload.status.value)
    if not updated:
        raise HTTPException(status_code=404, detail="Food listing not found")
    return updated


@app.get("/impact")
def impact():
    return services.get_impact()
