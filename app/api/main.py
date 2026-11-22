from fastapi import FastAPI, HTTPException

from .database import get_connection, initialize_database
from .matching import rank_recipients
from .schemas import FoodCreate, RecipientCreate, StatusUpdate
from . import services


app = FastAPI(
    title="Mess2Meal API",
    description="A local-first food rescue and redistribution coordination prototype.",
    version="1.1.0",
)


@app.on_event("startup")
def startup():
    initialize_database()


@app.get("/health")
def health():
    return {"status": "ok", "service": "Mess2Meal API", "version": app.version}


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
    if row is None:
        raise HTTPException(status_code=404, detail="Food listing not found")
    return {"food_id": food_id, "matches": rank_recipients(dict(row), services.list_recipients())}


@app.patch("/food/{food_id}/status")
def change_status(food_id: int, payload: StatusUpdate):
    try:
        updated = services.update_food_status(food_id, payload.status.value, payload.note)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    if updated is None:
        raise HTTPException(status_code=404, detail="Food listing not found")
    return updated


@app.get("/food/{food_id}/history")
def get_food_history(food_id: int):
    history = services.get_status_history(food_id)
    if history is None:
        raise HTTPException(status_code=404, detail="Food listing not found")
    return {"food_id": food_id, "history": history}


@app.get("/impact")
def impact():
    return services.get_impact()
