from datetime import datetime, timedelta, timezone

import pytest

from app.api import database, services


@pytest.fixture
def isolated_database(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "test.db")
    database.initialize_database()
    return database.DB_PATH


def food_payload():
    now = datetime.now(timezone.utc)
    return {
        "food_name": "Vegetable rice",
        "category": "Vegetarian",
        "quantity_kg": 3.5,
        "prepared_at": now,
        "best_before": now + timedelta(hours=3),
        "storage_condition": "covered container",
        "pickup_location": "Campus gate",
        "notes": "Test listing",
    }


def recipient_payload():
    return {
        "name": "Community Kitchen",
        "recipient_type": "Community kitchen",
        "contact_person": "Test Contact",
        "contact_phone": "0000000000",
        "location": "Test area",
        "preferred_categories": ["Vegetarian"],
        "capacity_kg": 10,
        "urgency": 4,
        "distance_km": 2.5,
        "is_active": True,
    }


def test_food_creation_records_initial_history(isolated_database):
    created = services.create_food(food_payload())
    history = services.get_status_history(created["id"])
    assert created["status"] == "available"
    assert len(history) == 1
    assert history[0]["new_status"] == "available"


def test_recipient_distance_is_persisted(isolated_database):
    recipient = services.create_recipient(recipient_payload())
    assert recipient["distance_km"] == 2.5
    assert services.list_recipients()[0]["distance_km"] == 2.5


def test_status_transitions_are_audited(isolated_database):
    created = services.create_food(food_payload())
    food_id = created["id"]
    services.update_food_status(food_id, "matched", "Coordinator shortlisted")
    services.update_food_status(food_id, "accepted", "Recipient confirmed")
    services.update_food_status(food_id, "picked_up", "Collected")
    delivered = services.update_food_status(food_id, "delivered", "Handover confirmed")
    assert delivered["status"] == "delivered"
    assert len(services.get_status_history(food_id)) == 5
    assert services.get_impact()["delivered_listings"] == 1
    assert services.get_impact()["delivered_kg"] == 3.5


def test_invalid_status_transition_is_rejected(isolated_database):
    created = services.create_food(food_payload())
    with pytest.raises(ValueError):
        services.update_food_status(created["id"], "delivered")
    assert services.get_status_history(created["id"])[-1]["new_status"] == "available"


def test_unknown_food_history_returns_none(isolated_database):
    assert services.get_status_history(999) is None
