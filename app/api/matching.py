from datetime import datetime, timezone


UNSAFE_TERMS = {"unsafe", "spoiled", "contaminated", "unrefrigerated"}


def rank_recipients(food: dict, recipients: list[dict], now=None) -> list[dict]:
    """Return explainable matches. This is prioritisation, not safety certification."""
    now = now or datetime.now(timezone.utc)
    if food.get("status", "available") != "available":
        return []
    expiry = datetime.fromisoformat(food["best_before"])
    if expiry.tzinfo is None:
        expiry = expiry.replace(tzinfo=timezone.utc)
    if expiry <= now:
        return []

    condition = (food.get("storage_condition") or "").strip().lower()
    if not condition or any(term in condition for term in UNSAFE_TERMS):
        return []

    quantity = float(food["quantity_kg"])
    category = food["category"].strip().lower()
    results = []

    for recipient in recipients:
        if not recipient.get("is_active", True):
            continue
        capacity = float(recipient.get("capacity_kg", 0))
        if capacity < quantity:
            continue

        preferred = recipient.get("preferred_categories", [])
        if isinstance(preferred, str):
            preferred = [x.strip() for x in preferred.split(",") if x.strip()]
        preferred = {x.lower() for x in preferred}
        if preferred and category not in preferred and "all" not in preferred:
            continue

        urgency = int(recipient.get("urgency", 3))
        # Lower operator-entered distance and higher urgency improve priority.
        distance = max(0.0, float(recipient.get("distance_km", 0)))
        score = round(urgency * 15 + max(0, 30 - distance * 3) +
                      min(capacity, 100) * 0.1, 2)
        reasons = [f"Capacity available: {capacity:g} kg"]
        reasons.append(f"Urgency level: {urgency}/5")
        reasons.append(f"Coordinator-entered distance: {distance:g} km")
        results.append({
            "recipient_id": recipient["id"],
            "recipient_name": recipient["name"],
            "score": score,
            "reasons": reasons,
        })

    return sorted(results, key=lambda item: item["score"], reverse=True)
