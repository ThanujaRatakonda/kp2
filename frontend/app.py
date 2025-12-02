import streamlit as st
import requests

API_URL = "http://backend:5000"

st.title("User Management App")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")

if st.button("Add User"):
    requests.post(f"{API_URL}/add", json={"name": name, "email": email})
    st.success("User added!")

st.subheader("All Users")
users = requests.get(f"{API_URL}/users").json()
for u in users:
    st.write(f"{u['name']} - {u['email']}")
