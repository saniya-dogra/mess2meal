import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
from pathlib import Path

API = "http://127.0.0.1:8000"
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "data.csv"

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

food_tab, recipient_tab, listings_tab, impact_tab, data_tab = st.tabs(
    ["🥘 Add surplus food", "🤝 Register recipient", "📦 Listings & matches", "📊 Impact", "🗂️ Field data"]
)

with food_tab:
    st.subheader("Register a food donation")
    with st.form("food_form"):
        food_name = st.text_input("Food name", placeholder="e.g. Vegetable pulao")
        category = st.selectbox("Category", ["Vegetarian", "Vegan", "Non-vegetarian", "Bread", "Other"])
        quantity = st.number_input("Quantity (kg)", min_value=0.1, value=5.0, step=0.5)
        prepared_date = st.date_input("Prepared date", value=datetime.now().date())
        prepared_time = st.time_input("Prepared time", value=datetime.now().time().replace(second=0, microsecond=0))
        expiry_date = st.date_input("Best-before date", value=(datetime.now() + timedelta(hours=4)).date())
        expiry_time = st.time_input("Best-before time", value=(datetime.now() + timedelta(hours=4)).time().replace(second=0, microsecond=0))
        storage = st.text_input("Storage condition", placeholder="e.g. Covered, kept hot")
        location = st.text_input("Pickup location")
        notes = st.text_area("Additional notes")
        submitted = st.form_submit_button("Publish food listing", type="primary")
    if submitted:
        prepared = datetime.combine(prepared_date, prepared_time).astimezone()
        best_before = datetime.combine(expiry_date, expiry_time).astimezone()
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
    st.subheader("Food listings")
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
        st.caption("A coordinator must verify food safety and recipient details before any handover.")
    else:
        st.info("No food listings yet. Add the first surplus listing.")

with impact_tab:
    st.subheader("Confirmed delivery impact")
    impact = requests.get(f"{API}/impact", timeout=5).json()
    c1, c2 = st.columns(2)
    c1.metric("Delivered listings", impact["delivered_listings"])
    c2.metric("Food delivered (kg)", round(impact["delivered_kg"], 2))
    st.caption("Only listings manually marked delivered are counted.")

with data_tab:
    st.subheader("Locally collected observations")
    st.caption("Switch between your own field observations and clearly labeled synthetic demo records. Never report demo rows as fieldwork.")
    demo_file = DATA_FILE.with_name("demo_data.csv")
    dataset_choice = st.radio(
        "Choose dataset",
        ["My real field observations", "Synthetic demo data (not fieldwork)"],
        horizontal=True,
    )
    selected_file = DATA_FILE if dataset_choice == "My real field observations" else demo_file
    if selected_file.exists():
        try:
            observations = pd.read_csv(selected_file)
            if dataset_choice == "Synthetic demo data (not fieldwork)":
                st.warning("DEMO DATA ONLY — fictional example locations, contacts, quantities and timestamps. These rows do not satisfy the assignment's fieldwork requirement.")
            st.metric("Rows in selected file", len(observations))
            if observations.empty:
                st.info("No field observations recorded yet. The CSV currently contains headers only.")
            else:
                st.dataframe(observations, use_container_width=True, hide_index=True)
                if "food_name" in observations.columns:
                    st.write("Observations by food item")
                    st.bar_chart(observations["food_name"].fillna("Not recorded").value_counts())
        except (pd.errors.ParserError, UnicodeDecodeError) as exc:
            st.error(f"Could not read data.csv: {exc}")
    else:
        st.warning(f"{selected_file.name} was not found.")
