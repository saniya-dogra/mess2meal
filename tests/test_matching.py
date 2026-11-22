from datetime import datetime, timedelta, timezone

from app.api.matching import rank_recipients


def sample_food(**overrides):
    food = {
        "food_name": "Rice",
        "category": "vegetarian",
        "quantity_kg": 8,
        "best_before": (datetime.now(timezone.utc) + timedelta(hours=3)).isoformat(),
        "storage_condition": "covered and kept hot",
        "status": "available",
    }
    food.update(overrides)
    return food


def sample_recipient(**overrides):
    recipient = {
        "id": 1,
        "name": "Community Kitchen",
        "capacity_kg": 12,
        "preferred_categories": ["vegetarian"],
        "urgency": 4,
        "distance_km": 2,
        "is_active": True,
    }
    recipient.update(overrides)
    return recipient


def test_matching_returns_eligible_recipient():
    matches = rank_recipients(sample_food(), [sample_recipient()])
    assert len(matches) == 1
    assert matches[0]["recipient_name"] == "Community Kitchen"
    assert matches[0]["reasons"]


def test_expired_food_is_never_matched():
    expired = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat()
    assert rank_recipients(sample_food(best_before=expired), [sample_recipient()]) == []


def test_unsafe_storage_is_never_matched():
    assert rank_recipients(
        sample_food(storage_condition="spoiled food"),
        [sample_recipient()],
    ) == []


def test_recipient_with_insufficient_capacity_is_excluded():
    assert rank_recipients(
        sample_food(quantity_kg=20),
        [sample_recipient(capacity_kg=5)],
    ) == []


def test_inactive_recipient_is_excluded():
    assert rank_recipients(
        sample_food(),
        [sample_recipient(is_active=False)],
    ) == []


def test_category_mismatch_is_excluded():
    assert rank_recipients(
        sample_food(category="vegetarian"),
        [sample_recipient(preferred_categories=["bread"])],
    ) == []
