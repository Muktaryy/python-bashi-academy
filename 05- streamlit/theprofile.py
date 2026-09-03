import requests
import streamlit as st

st.title("The Profile")
username = st.text_input("Enter your GitHub username:")
search = st.button("Search")

if search:
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        user = response.json()
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(user["avatar_url"], width=150)
        with col2:
            st.write(f" {user['bio']}")
            st.write(f"Public Repos: {user['public_repos']}")
            st.write(f"Followers: {user['followers']}")
    else:
        st.error("User not found")
