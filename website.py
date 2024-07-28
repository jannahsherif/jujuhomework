import streamlit as st 
st.set_page_config(page_title="Jannah Webpage", layout= "wide")

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
