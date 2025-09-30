import streamlit as st

st.set_page_config(page_title="UnicornServices", layout="wide")

pages = {
    "Leads by Zone": "leads-zone",
    "Last-Minute Appointments": "last-minute-appointments"
}

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose an option", options=list(pages.values()))

if page in pages:
    st.switch_page(pages[page])