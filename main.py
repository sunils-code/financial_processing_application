import streamlit as st
import app
import Extra_Credit_Task

# Set page title
st.set_page_config(page_title='Black Rock Take Home Exercise')

# Sidebar menu
selection = st.sidebar.radio(
    "Menu", ['Main Exercise Tasks', 'Extra Credit Tasks'])

# Routing based on selection
if selection == 'Main Exercise Tasks':
    app.main()
elif selection == 'Extra Credit Tasks':
    Extra_Credit_Task.main()
