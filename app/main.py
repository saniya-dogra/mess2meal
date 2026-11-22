import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
from pathlib import Path

API = "http://127.0.0.1:8000"
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "data.csv"

st.set_page_config(page_title="Mess2Meal", page_icon="🍱", layout="wide")
st.markdown("""
<style>
    .block-container {padding-top: 1.8rem; padding-bottom: 2.5rem;}
    [data-testid="stMetric"] {background: rgba(16,185,129,.07); padding: 14px; border-radius: 12px;}
    div[data-testid="stForm"] {border: 1px solid rgba(120,120,120,.22); border-radius: 12px; padding: 16px;}
</style>
""", unsafe_allow_html=True)

st.title("🍱 Mess2Meal")
st.caption("Rescue surplus food · Find suitable recipients · Coordinate responsible handovers")

try:
    health = requests.get(f"{API}/health", timeout=3)
    health.raise_for_status()
    st.sidebar.success("Backend connected")
except requests.RequestException:
    st.sidebar.error("Backend offline")
    st.error("Start the API in another terminal: `uvicorn app.api.main:app --reload`")
    st.stop()

st.sidebar.markdown("### About this prototype")
st.sidebar.info("Suggestions support coordinator review. They do not certify food safety or confirm a physical handover.")
st.sidebar.caption("Demo CSV records are synthetic and are not real impact evidence.")

food_tab, recipient_tab, listings_tab, impact_tab, data_tab = st.tabs(
    ["🥘 Add food", "🤝 Register recipient", "📦 Manage listings", "📊 Impact", "🗂️ Demo data"]
)

def show_api_error(response):
    try:
        detail = response.json().get("detail", response.text)
    except ValueError:
        detail = response.text
    st.error(f"Request failed ({response.status_code}): {detail}")

with food_tab:
    st.subheader("Create a surplus-food listing")
    with st.form("food_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        food_name = c1.text_input("Food name", placeholder="Vegetable pulao")
        category = c2.selectbox("Category", ["Vegetarian", "Vegan", "Non-vegetarian", "Bread", "Other"])
        quantity = c1.number_input("Quantity (kg)", min_value=0.1, max_value=10000.0, value=5.0, step=0.5)
        location = c2.text_input("Pickup location", placeholder="Campus gate / collection point")
        prepared_date = c1.date_input("Prepared date", value=datetime.now().date())
        prepared_time = c2.time_input("Prepared time", value=datetime.now().time().replace(second=0, microsecond=0))
        expiry_default = datetime.now() + timedelta(hours=4)
        expiry_date = c1.date_input("Best-before date", value=expiry_default.date(), key="expiry_date")
        expiry_time = c2.time_input("Best-before time", value=expiry_default.time().replace(second=0, microsecond=0))
        storage = st.text_input("Reported storage condition", placeholder="Covered container; kept hot")
        notes = st.text_area("Additional notes", max_chars=500)
        submitted = st.form_submit_button("Publish listing", type="primary", use_container_width=True)
    if submitted:
        if not food_name.strip() or not location.strip() or not storage.strip():
            st.warning("Food name, pickup location and storage description are required.")
        else:
            prepared = datetime.combine(prepared_date, prepared_time).astimezone()
            best_before = datetime.combine(expiry_date, expiry_time).astimezone()
            if best_before <= prepared:
                st.warning("Best-before time must be later than preparation time.")
            else:
                payload = {
                    "food_name": food_name.strip(), "category": category, "quantity_kg": quantity,
                    "prepared_at": prepared.isoformat(), "best_before": best_before.isoformat(),
                    "storage_condition": storage.strip(), "pickup_location": location.strip(), "notes": notes.strip(),
                }
                try:
                    response = requests.post(f"{API}/food", json=payload, timeout=8)
                    if response.ok:
                        st.success(f"Listing #{response.json()['id']} created.")
                    else:
                        show_api_error(response)
                except requests.RequestException as exc:
                    st.error(f"Could not reach the API: {exc}")

with recipient_tab:
    st.subheader("Register an organisation or recipient group")
    with st.form("recipient_form"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Organisation / group name")
        recipient_type = c2.selectbox("Type", ["NGO", "Shelter", "Community kitchen", "Other"])
        contact = c1.text_input("Contact person")
        phone = c2.text_input("Contact phone")
        recipient_location = c1.text_input("Location / area")
        distance = c2.number_input("Estimated distance from donor (km)", min_value=0.0, max_value=10000.0, value=0.0, step=0.5,
                                   help="Coordinator-entered estimate; no GPS or route calculation is performed.")
        categories = st.multiselect("Food categories accepted", ["Vegetarian", "Vegan", "Non-vegetarian", "Bread", "Other", "All"])
        capacity = st.number_input("Maximum capacity (kg)", min_value=0.1, max_value=10000.0, value=10.0)
        urgency = st.slider("Current urgency", 1, 5, 3)
        active = st.checkbox("Currently accepting food", value=True)
        saved = st.form_submit_button("Register recipient", type="primary", use_container_width=True)
    if saved:
        if not all(value.strip() for value in [name, contact, phone, recipient_location]) or not categories:
            st.warning("Complete all contact/location fields and select at least one accepted category.")
        else:
            payload = {
                "name": name.strip(), "recipient_type": recipient_type, "contact_person": contact.strip(),
                "contact_phone": phone.strip(), "location": recipient_location.strip(),
                "preferred_categories": categories, "capacity_kg": capacity, "urgency": urgency,
                "distance_km": distance, "is_active": active,
            }
            try:
                response = requests.post(f"{API}/recipients", json=payload, timeout=8)
                if response.ok:
                    st.success(f"Recipient #{response.json()['id']} registered.")
                else:
                    show_api_error(response)
            except requests.RequestException as exc:
                st.error(f"Could not reach the API: {exc}")

with listings_tab:
    st.subheader("Review listings, matches and status history")
    try:
        response = requests.get(f"{API}/food", timeout=8)
        response.raise_for_status()
        listings = response.json()
    except (requests.RequestException, ValueError) as exc:
        listings = []
        st.error(f"Could not load listings: {exc}")

    if listings:
        frame = pd.DataFrame(listings)
        st.dataframe(frame, use_container_width=True, hide_index=True)
        ids = [item["id"] for item in listings]
        selected = st.selectbox("Select listing", ids, format_func=lambda value: f"#{value} — {next(x['food_name'] for x in listings if x['id'] == value)}")
        selected_food = next(item for item in listings if item["id"] == selected)
        st.caption(f"Current status: **{selected_food['status']}**")
        left, right = st.columns(2)
        with left:
            if st.button("Find suitable recipients", type="primary", use_container_width=True):
                try:
                    match_response = requests.get(f"{API}/food/{selected}/matches", timeout=8)
                    match_response.raise_for_status()
                    matches = match_response.json()["matches"]
                    if matches:
                        st.dataframe(pd.DataFrame(matches), use_container_width=True, hide_index=True)
                    else:
                        st.info("No eligible matches. Review expiry, storage description, category, capacity and recipient availability.")
                except requests.RequestException as exc:
                    st.error(f"Matching request failed: {exc}")
        with right:
            transitions = {
                "available": ["matched", "cancelled"],
                "matched": ["accepted", "available", "cancelled"],
                "accepted": ["picked_up", "cancelled"],
                "picked_up": ["delivered"],
                "delivered": [],
                "cancelled": [],
            }
            allowed = transitions.get(selected_food["status"], [])
            if allowed:
                next_status = st.selectbox("Next status", allowed)
                status_note = st.text_input("Status note", placeholder="Coordinator note (optional)")
                if st.button("Update status", use_container_width=True):
                    try:
                        update = requests.patch(
                            f"{API}/food/{selected}/status",
                            json={"status": next_status, "note": status_note},
                            timeout=8,
                        )
                        if update.ok:
                            st.success(f"Status updated to {next_status}. Refresh the page to see the latest listing.")
                        else:
                            show_api_error(update)
                    except requests.RequestException as exc:
                        st.error(f"Status update failed: {exc}")
            else:
                st.info("This listing has reached a final status.")
        try:
            history_response = requests.get(f"{API}/food/{selected}/history", timeout=8)
            history_response.raise_for_status()
            with st.expander("View status history"):
                st.dataframe(pd.DataFrame(history_response.json()["history"]), use_container_width=True, hide_index=True)
        except requests.RequestException as exc:
            st.warning(f"Could not load status history: {exc}")
        st.caption("A coordinator must verify food safety, recipient suitability and physical handover. Status updates are manual records.")
    else:
        st.info("No food listings yet. Add a surplus listing to begin.")

with impact_tab:
    st.subheader("Confirmed delivery impact")
    try:
        response = requests.get(f"{API}/impact", timeout=8)
        response.raise_for_status()
        impact = response.json()
        c1, c2 = st.columns(2)
        c1.metric("Delivered listings", impact["delivered_listings"])
        c2.metric("Food delivered", f"{impact['delivered_kg']:.2f} kg")
        st.caption("Only records manually moved to delivered are counted. Test records must not be presented as real-world impact.")
    except requests.RequestException as exc:
        st.error(f"Could not load impact totals: {exc}")

with data_tab:
    st.subheader("CSV demonstration data")
    st.caption("The CSV is loaded from data/data.csv. Check data_origin before interpreting any row.")
    if DATA_FILE.exists():
        try:
            observations = pd.read_csv(DATA_FILE)
            c1, c2 = st.columns(2)
            c1.metric("CSV rows", len(observations))
            if "data_origin" in observations.columns:
                synthetic_count = int((observations["data_origin"] == "SYNTHETIC_DEMO_ONLY").sum())
                c2.metric("Synthetic demo rows", synthetic_count)
                if synthetic_count:
                    st.warning(f"{synthetic_count} records are fictional examples for software testing, not fieldwork or actual food rescued.")
            st.dataframe(observations, use_container_width=True, hide_index=True)
            if "source_type" in observations.columns:
                st.subheader("Records by source category")
                st.bar_chart(observations["source_type"].fillna("Not recorded").value_counts())
            if {"food_name", "quantity_kg"}.issubset(observations.columns):
                chart_data = observations.copy()
                chart_data["quantity_kg"] = pd.to_numeric(chart_data["quantity_kg"], errors="coerce")
                st.subheader("Illustrative quantity by food item")
                st.bar_chart(chart_data.groupby("food_name")["quantity_kg"].sum().sort_values(ascending=False))
            st.caption("Charts describe the CSV only. Synthetic quantities are not measured waste or delivered impact.")
        except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as exc:
            st.error(f"Could not read data.csv: {exc}")
    else:
        st.warning("data/data.csv was not found.")
