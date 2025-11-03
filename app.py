import streamlit as st

st.title("Basic Streamlit Form Example")

with st.form(key="user_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    subscribe = st.checkbox("Subscribe to newsletter")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.success("Form Submitted Successfully!")
    st.write("### User Details:")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Subscribed:** {'Yes' if subscribe else 'No'}")
