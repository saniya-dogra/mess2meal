import json
from datetime import datetime, timezone

from .database import get_connection


ALLOWED_TRANSITIONS = {
    "available": {"matched", "cancelled"},
    "matched": {"accepted", "available", "cancelled"},
    "accepted": {"picked_up", "cancelled"},
    "picked_up": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
}


def create_food(payload: dict) -> dict:
    with get_connection() as conn:
        now = datetime.now(timezone.utc).isoformat()
        cursor = conn.execute(
            """INSERT INTO food
            (food_name, category, quantity_kg, prepared_at, best_before,
             storage_condition, pickup_location, notes, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'available', ?)""",
            (payload["food_name"], payload["category"], payload["quantity_kg"],
             payload["prepared_at"].isoformat(), payload["best_before"].isoformat(),
             payload["storage_condition"], payload["pickup_location"],
             payload.get("notes", ""), now),
        )
        food_id = cursor.lastrowid
        conn.execute(
            """INSERT INTO status_history
            (food_id, old_status, new_status, changed_at, note)
            VALUES (?, NULL, 'available', ?, 'Listing created')""",
            (food_id, now),
        )
        return dict(conn.execute("SELECT * FROM food WHERE id=?", (food_id,)).fetchone())


def list_food() -> list[dict]:
    with get_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM food ORDER BY id DESC")]


def create_recipient(payload: dict) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            """INSERT INTO recipients
            (name, recipient_type, contact_person, contact_phone, location,
             preferred_categories, capacity_kg, urgency, is_active, distance_km)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (payload["name"], payload["recipient_type"], payload["contact_person"],
             payload["contact_phone"], payload["location"],
             json.dumps(payload["preferred_categories"]), payload["capacity_kg"],
             payload["urgency"], int(payload["is_active"]), payload.get("distance_km", 0)),
        )
        result = dict(conn.execute("SELECT * FROM recipients WHERE id=?", (cursor.lastrowid,)).fetchone())
        result["preferred_categories"] = json.loads(result["preferred_categories"])
        result["is_active"] = bool(result["is_active"])
        return result


def list_recipients() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM recipients ORDER BY id DESC").fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["preferred_categories"] = json.loads(item["preferred_categories"])
            item["is_active"] = bool(item["is_active"])
            result.append(item)
        return result


def update_food_status(food_id: int, status: str, note: str = "") -> dict | None:
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM food WHERE id=?", (food_id,)).fetchone()
        if row is None:
            return None
        old_status = row["status"]
        if status == old_status:
            return dict(row)
        if status not in ALLOWED_TRANSITIONS.get(old_status, set()):
            raise ValueError(f"Cannot move a listing from '{old_status}' to '{status}'.")
        changed_at = datetime.now(timezone.utc).isoformat()
        conn.execute("UPDATE food SET status=? WHERE id=?", (status, food_id))
        conn.execute(
            """INSERT INTO status_history
            (food_id, old_status, new_status, changed_at, note)
            VALUES (?, ?, ?, ?, ?)""",
            (food_id, old_status, status, changed_at, note.strip()),
        )
        return dict(conn.execute("SELECT * FROM food WHERE id=?", (food_id,)).fetchone())


def get_status_history(food_id: int) -> list[dict] | None:
    with get_connection() as conn:
        if conn.execute("SELECT 1 FROM food WHERE id=?", (food_id,)).fetchone() is None:
            return None
        rows = conn.execute(
            """SELECT old_status, new_status, changed_at, note
            FROM status_history WHERE food_id=? ORDER BY id""",
            (food_id,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_impact() -> dict:
    with get_connection() as conn:
        row = conn.execute(
            """SELECT COUNT(*) AS delivered_listings,
            COALESCE(SUM(quantity_kg), 0) AS delivered_kg
            FROM food WHERE status='delivered'"""
        ).fetchone()
        return dict(row)
