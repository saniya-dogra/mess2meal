import json
from datetime import datetime, timezone

from .database import get_connection


def create_food(payload: dict) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            """INSERT INTO food
            (food_name, category, quantity_kg, prepared_at, best_before,
             storage_condition, pickup_location, notes, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'available', ?)""",
            (payload["food_name"], payload["category"], payload["quantity_kg"],
             payload["prepared_at"].isoformat(), payload["best_before"].isoformat(),
             payload["storage_condition"], payload["pickup_location"],
             payload.get("notes", ""), datetime.now(timezone.utc).isoformat()),
        )
        row = conn.execute("SELECT * FROM food WHERE id=?", (cursor.lastrowid,)).fetchone()
        return dict(row)


def list_food() -> list[dict]:
    with get_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM food ORDER BY id DESC")]


def create_recipient(payload: dict) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            """INSERT INTO recipients
            (name, recipient_type, contact_person, contact_phone, location,
             preferred_categories, capacity_kg, urgency, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (payload["name"], payload["recipient_type"], payload["contact_person"],
             payload["contact_phone"], payload["location"],
             json.dumps(payload["preferred_categories"]), payload["capacity_kg"],
             payload["urgency"], int(payload["is_active"])),
        )
        row = conn.execute("SELECT * FROM recipients WHERE id=?", (cursor.lastrowid,)).fetchone()
        result = dict(row)
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


def update_food_status(food_id: int, status: str) -> dict | None:
    allowed = {"available", "matched", "accepted", "picked_up", "delivered", "cancelled"}
    if status not in allowed:
        raise ValueError("Unsupported donation status")
    with get_connection() as conn:
        conn.execute("UPDATE food SET status=? WHERE id=?", (status, food_id))
        row = conn.execute("SELECT * FROM food WHERE id=?", (food_id,)).fetchone()
        return dict(row) if row else None


def get_impact() -> dict:
    with get_connection() as conn:
        row = conn.execute(
            """SELECT COUNT(*) AS delivered_listings,
            COALESCE(SUM(quantity_kg), 0) AS delivered_kg
            FROM food WHERE status='delivered'"""
        ).fetchone()
        return dict(row)
