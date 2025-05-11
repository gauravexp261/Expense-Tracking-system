import streamlit as st 
from edit_tab import edit_tab
from analytics_tab import analytics_tab

st.title('Expense Tracking system')

tab1, tab2 = st.tabs(['Add/Update', 'Analytics'])

with tab1:
    edit_tab()
with tab2:
    analytics_tab()