import streamlit as st 
import requests
from datetime import datetime
import pandas as pd

API_URL = 'http://localhost:8000'


def analytics_tab():
    col1, col2 = st.columns(2)
    start_date = st.date_input('Start Date', datetime(2024,8,1))
    end_date = st.date_input('Start Date', datetime(2024,10,1))
    
    if st.button("Get Analytics"):
        payload = {
            
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f'{API_URL}/analytics/',json=payload)
        if response.status_code == 200:
            try:
                analytics = response.json()
            except ValueError:
                st.error("Invalid JSON in response")
                st.text(response.text)
                return
        else:
            st.error(f"Request failed with status code {response.status_code}")
            st.text(response.text)
            return  
        breakdown = analytics.get("breakdown", {})
        total_sum = analytics.get("total", 0)

        # Handle cases where breakdown is empty or missing
        if not breakdown:
            st.error("No expense breakdown found.")
            return

        data = {
            "Category": list(breakdown.keys()),
            "Total": [breakdown[cat]["total"] for cat in breakdown],
            "Percentage": [round((breakdown[cat]["total"] / total_sum) * 100, 2) if total_sum > 0 else 0 for cat in breakdown]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.bar_chart(df_sorted.set_index("Category")["Percentage"])
        st.table(df_sorted)