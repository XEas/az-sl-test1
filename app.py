import streamlit as st

# Title of the app
st.title('Hello, Streamlit!')

# Display a simple text
st.write('Welcome to your first Streamlit app!')

# Display a button and show a message when clicked
if st.button('Click me'):
    st.write('Button clicked!')
