import streamlit as st

st.set_page_config(page_title="UnicornOffers - Last-Minute Appointments", layout="wide")

with open("pages/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='custom-title'>UnicornOffers - Last-Minute Appointments</h1>", unsafe_allow_html=True)
st.markdown("<p class='custom-text'>Find available last-minute appointments at hair salons and beauty centers.</p>", unsafe_allow_html=True)

with st.form("form_last_minute"):
    st.markdown("<div class='custom-form'>", unsafe_allow_html=True)
    name = st.text_input("Name")
    email = st.text_input("Email")
    accept_terms = st.checkbox("I accept flexible appointments and the privacy policy (GDPR)")
    if st.form_submit_button("Book Now!", key="btn_appointments", help="Submit to book"):
        st.markdown("</div>", unsafe_allow_html=True)
        if accept_terms:
            st.markdown("<p class='custom-success'>Great! We'll send you available appointments.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='custom-error'>You must accept the terms.</p>", unsafe_allow_html=True)