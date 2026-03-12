import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")
if st.button("Click me"):
    st.write("Button clicked!")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected: {number}")
if st.checkbox("Show more options"):
    st.write("Here are some more options...")
    st.write("- Option 1")
    st.write("- Option 2")
    st.write("- Option 3")
st.write("Thank you for using the app!")