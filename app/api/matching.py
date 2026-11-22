from datetime import datetime, timezone


UNSAFE_TERMS = {
    "unsafe", "spoiled", "contaminated", "unrefrigerated",
    "rotten", "expired", "stale", "bad smell",
}


def _as_utc(value):
    parsed = value if isinstance(value, datetime) else datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def rank_recipients(food: dict, recipients: list[dict], now=None) -> list[dict]:
    """Return explainable recipient suggestions; never certify food safety."""
    now = _as_utc(now or datetime.now(timezone.utc))
    if food.get("status", "available") != "available":
        return []
    best_before = food.get("best_before")
    if not best_before or _as_utc(best_before) <= now:
        return []

    condition = (food.get("storage_condition") or "").strip().lower()
    if not condition or any(term in condition for term in UNSAFE_TERMS):
        return []
    try:
        quantity = float(food["quantity_kg"])
        category = str(food["category"]).strip().lower()
    except (KeyError, TypeError, ValueError):
        return []
    if quantity <= 0 or not category:
        return []

    results = []
    for recipient in recipients:
        if not recipient.get("is_active", True):
            continue
        try:
            capacity = float(recipient.get("capacity_kg", 0))
            urgency = int(recipient.get("urgency", 3))
            distance = max(0.0, float(recipient.get("distance_km", 0)))
        except (TypeError, ValueError):
            continue
        if capacity < quantity or not 1 <= urgency <= 5:
            continue

        preferred = recipient.get("preferred_categories", [])
        if isinstance(preferred, str):
            preferred = [item.strip() for item in preferred.split(",") if item.strip()]
        preferred = {str(item).strip().lower() for item in preferred}
        if preferred and category not in preferred and "all" not in preferred:
            continue

        urgency_points = urgency * 15
        distance_points = max(0, 30 - distance * 3)
        capacity_points = min(capacity, 100) * 0.1
        score = round(urgency_points + distance_points + capacity_points, 2)
        reasons = [
            f"Capacity available: {capacity:g} kg",
            f"Urgency level: {urgency}/5",
            f"Coordinator-entered distance: {distance:g} km",
        ]
        results.append({
            "recipient_id": recipient["id"],
            "recipient_name": recipient["name"],
            "score": score,
            "reasons": reasons,
        })
    return sorted(results, key=lambda item: (-item["score"], item["recipient_name"].lower()))
