import streamlit as st

st.set_page_config(page_title="UnicornOffers - Leads by Zone", layout="wide")

with open("pages/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="UnicornOffers - Leads by Zone", layout="wide")

st.markdown("<h1 class='custom-title'>UnicornOffers - Leads by Zone</h1>", unsafe_allow_html=True)
st.markdown("<p class='custom-text'>Sign up to receive exclusive offers from hair salons and beauty centers in your area.</p>", unsafe_allow_html=True)

with st.form("form_leads_by_zone"):
    st.markdown("<div class='custom-form'>", unsafe_allow_html=True)
    name = st.text_input("Name")
    email = st.text_input("Email")
    city = st.selectbox("City", ["Madrid", "Barcelona", "Valencia", "Sevilla"])
    postal_code = st.text_input("Postal Code")
    accept_privacy = st.checkbox("I accept the privacy policy (GDPR)")
    if st.form_submit_button("Get Offers!", key="btn_leads", help="Submit to receive offers"):
        st.markdown("</div>", unsafe_allow_html=True)
        if accept_privacy:
            st.markdown("<p class='custom-success'>Thank you! Your data has been registered. Centers will contact you soon.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='custom-error'>You must accept the privacy policy.</p>", unsafe_allow_html=True)