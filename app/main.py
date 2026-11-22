import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Mess2Meal", page_icon="🍱", layout="wide")
st.title("🍱 Mess2Meal")
st.caption("Rescue surplus food. Connect it to people who need it.")

try:
    health = requests.get(f"{API}/health", timeout=2)
    health.raise_for_status()
    st.success("Backend connected")
except requests.RequestException:
    st.error("Backend is offline. Start it with: uvicorn app.api.main:app --reload")
    st.stop()

food_tab, recipient_tab, listings_tab, impact_tab = st.tabs(
    ["🥘 Add surplus food", "🤝 Register recipient", "📦 Listings & matches", "📊 Impact"]
)

with food_tab:
    st.subheader("Register a food donation")
    with st.form("food_form"):
        food_name = st.text_input("Food name", placeholder="e.g. Vegetable pulao")
        category = st.selectbox("Category", ["Vegetarian", "Vegan", "Non-vegetarian", "Bread", "Other"])
        quantity = st.number_input("Quantity (kg)", min_value=0.1, value=5.0, step=0.5)
        prepared = st.datetime_input("Prepared at", value=datetime.now())
        best_before = st.datetime_input("Best before", value=datetime.now() + timedelta(hours=4))
        storage = st.text_input("Storage condition", placeholder="e.g. Covered, kept hot")
        location = st.text_input("Pickup location")
        notes = st.text_area("Additional notes")
        submitted = st.form_submit_button("Publish food listing", type="primary")
    if submitted:
        payload = {
            "food_name": food_name, "category": category, "quantity_kg": quantity,
            "prepared_at": prepared.isoformat(), "best_before": best_before.isoformat(),
            "storage_condition": storage, "pickup_location": location, "notes": notes,
        }
        response = requests.post(f"{API}/food", json=payload, timeout=5)
        if response.ok:
            st.success(f"Listing #{response.json()['id']} created")
        else:
            st.error(response.text)

with recipient_tab:
    st.subheader("Register an NGO or recipient group")
    with st.form("recipient_form"):
        name = st.text_input("Organisation / group name")
        recipient_type = st.selectbox("Type", ["NGO", "Shelter", "Community kitchen", "Other"])
        contact = st.text_input("Contact person")
        phone = st.text_input("Contact phone")
        recipient_location = st.text_input("Location")
        categories = st.multiselect("Food categories accepted", ["Vegetarian", "Vegan", "Non-vegetarian", "Bread", "Other", "All"])
        capacity = st.number_input("Capacity (kg)", min_value=0.1, value=10.0)
        urgency = st.slider("Urgency", 1, 5, 3)
        active = st.checkbox("Currently accepting food", value=True)
        saved = st.form_submit_button("Register recipient", type="primary")
    if saved:
        payload = {
            "name": name, "recipient_type": recipient_type, "contact_person": contact,
            "contact_phone": phone, "location": recipient_location,
            "preferred_categories": categories, "capacity_kg": capacity,
            "urgency": urgency, "is_active": active,
        }
        response = requests.post(f"{API}/recipients", json=payload, timeout=5)
        if response.ok:
            st.success(f"Recipient #{response.json()['id']} registered")
        else:
            st.error(response.text)

with listings_tab:
    st.subheader("Available food")
    if st.button("Refresh listings"):
        st.rerun()
    listings = requests.get(f"{API}/food", timeout=5).json()
    if listings:
        st.dataframe(pd.DataFrame(listings), use_container_width=True, hide_index=True)
        selected = st.selectbox("Find matches for listing", [x["id"] for x in listings])
        if st.button("Find suitable recipients"):
            matches = requests.get(f"{API}/food/{selected}/matches", timeout=5).json()["matches"]
            if matches:
                st.dataframe(pd.DataFrame(matches), use_container_width=True, hide_index=True)
            else:
                st.info("No eligible match found. Check expiry, storage condition, category and capacity.")
    else:
        st.info("No food listings yet. Add the first surplus listing.")

with impact_tab:
    st.subheader("Confirmed delivery impact")
    impact = requests.get(f"{API}/impact", timeout=5).json()
    c1, c2 = st.columns(2)
    c1.metric("Delivered listings", impact["delivered_listings"])
    c2.metric("Food delivered (kg)", round(impact["delivered_kg"], 2))
    st.caption("Only listings manually marked delivered are counted.")
