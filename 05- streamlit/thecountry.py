import requests
import streamlit as st

st.title("The country ")
country = st.text_input("Enter a country name: ")
search = st.button("Search")

url = f"https://countries-api.davegarvey.workers.dev/search?q={country}"

response = requests.get(url)
data = response.json()


if search:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Capital")
        st.write(data["results"][0]["capital"])
    with col2:
        st.header("Population")
        st.write(f" {data['results'][0]['population']}")
    with col3:
        st.header("Region")
        st.write(f" {data['results'][0]['region']}")
else:
    st.write("Please enter a country name and click Search.")
