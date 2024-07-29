import streamlit as st
import webbrowser

st.set_page_config(page_title="Jannah Webpage", layout="wide")

st.subheader("Welcome to Jannah's Web")
st.title("Demo website")
st.write("This is for integration project")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("link to sherkety")
        st.write("###")
        st.write("[Sherkety >](https://sherkety.net/)")

# Login Section
st.write("---")
st.header("Login to Facebook")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Redirect to Facebook
    # Display username and password
    st.write(f"Username: {username}")
    st.write(f"Password: {password}")
