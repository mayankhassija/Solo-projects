import streamlit as st
st.set_page_config(
    page_title = "AI Memory OS",
    page_icon = "🧠",
    layout = "wide"
)

st.title("🧠AI Memory OS")
st.write("Version 0.1")
st.divider()
st.subheader("Notes")
st.info("No notes.")

if st.button("Create First Note"):
    st.success("Button works!")
