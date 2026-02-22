import streamlit as st

pages = st.navigation([
    st.Page("avocado_front.py", title="🥑 Avocado Price Prediction"),
    st.Page("diabetes_front.py", title="🩺 Diabetes Prediction"),
    st.Page("loanfront.py", title="💰 Loan Approval"),
    st.Page("mushrooms_front.py", title="🍄 Mushroom Classification"),
    st.Page("titanic-front.py", title="🚢 Titanic Survival"),
])

pages.run()