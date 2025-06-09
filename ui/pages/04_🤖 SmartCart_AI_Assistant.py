import streamlit as st
import requests
import re
from utils.api_helpers import call_api
from utils.session_helpers import require_login
from utils.logo_helper import inject_sidebar_logo

# --------------------- Έλεγχος login ---------------------
require_login()

# --------------------- Ρυθμίσεις ---------------------
st.set_page_config(page_title="SmartCart AI", page_icon="🤖")

# --------------------- Sidebar ---------------------
inject_sidebar_logo()

# --------------------- Τίτλος και περιγραφή ---------------------
st.markdown("""
    <div style='text-align: center; margin-top: 1rem;'>
        <h1 style='font-size: 2.5rem;'>🤖 SmartCart AI Assistant</h1>
        <p style='font-size: 1.1rem; color: #555;'>Κάνε την ερώτησή σου για υγεία, συνταγές, καθαριότητα ή αγορές</p>
    </div>
""", unsafe_allow_html=True)

# --------------------- Ερώτηση Χρήστη ---------------------
st.subheader("🔍 Η ερώτησή σου")

question = st.text_input("", placeholder="Π.χ. Τι να μαγειρέψω σήμερα;")
ask_btn = st.button("🤖 Ρώτα το SmartCart")

# --------------------- Αποθήκευση προηγούμενης απάντησης ---------------------
if "ai_last_response" not in st.session_state:
    st.session_state.ai_last_response = None
if "ai_last_question" not in st.session_state:
    st.session_state.ai_last_question = None

# --------------------- Κλήση AI Backend ---------------------
if ask_btn and question:
    with st.spinner("🤖 Σκέφτομαι την καλύτερη απάντηση για σένα..."):
        res = call_api("/ai/ask", method="post", json={
            "question": question,
            "user_id": st.session_state.get("user_id")
        })
        if res and res.status_code == 200:
            data = res.json()
            st.session_state.ai_last_question = question
            st.session_state.ai_last_response = data.get("response")
        else:
            st.session_state.ai_last_response = "⚠️ Σφάλμα κατά την επεξεργασία. Δοκίμασε ξανά."
        # Καθαρισμός cache και επανεκκίνηση
        st.cache_data.clear()
        st.rerun()

# --------------------- Εμφάνιση Απάντησης ---------------------
if st.session_state.ai_last_response:
    st.markdown(f"""
    <div class="assistant-bubble">
        <strong>🤖 SmartCart AI:</strong><br><br>
        {st.session_state.ai_last_response}
    </div>
    """, unsafe_allow_html=True)

