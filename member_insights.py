# FMCC Member Insights Dashboard - Built by Innovative Electronics and Devices
# Streamlit app for AI-driven member analytics with predictive trends.
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
import logging

logging.basicConfig(filename='fmcc_insights.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

data = {
    'Month': ['Jan-25', 'Feb-25', 'Mar-25', 'Apr-25', 'May-25', 'Jun-25', 'Jul-25', 'Aug-25'],
    'Members': [1200, 1220, 1250, 1230, 1280, 1300, 1320, 1350],
    'Event_Attendance': [300, 320, 350, 340, 360, 380, 400, 420],
    'Membership_Renewals': [100, 110, 105, 115, 120, 125, 130, 140]
}
df = pd.DataFrame(data)

def predict_trend(data, column):
    X = np.arange(len(data)).reshape(-1, 1)
    y = data[column].values
    model = LinearRegression()
    model.fit(X, y)
    future = np.array([[len(data)]])
    return model.predict(future)[0]

st.set_page_config(page_title="FMCC Member Insights", layout="wide")
st.markdown("""
    <style>
    .main {background-color: #f5f5f5;}
    .stButton>button {background-color: #0066cc; color: white;}
    </style>
    """, unsafe_allow_html=True)

st.image("https://via.placeholder.com/200x50?text=Innovative+Electronics+Logo", width=200)  # Replace with your logo
st.image("https://via.placeholder.com/200x50?text=FMCC+Logo", width=200)  # Replace with FMCC logo
st.title("FMCC Member Insights Dashboard by Innovative Electronics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Members", df['Members'].iloc[-1], f"+{df['Members'].iloc[-1] - df['Members'].iloc[-2]}")
col2.metric("Event Attendance", df['Event_Attendance'].iloc[-1], f"+{df['Event_Attendance'].iloc[-1] - df['Event_Attendance'].iloc[-2]}")
col3.metric("Renewals", df['Membership_Renewals'].iloc[-1], f"+{df['Membership_Renewals'].iloc[-1] - df['Membership_Renewals'].iloc[-2]}")

st.subheader("AI-Predicted Trends for Sep-25")
members_pred = round(predict_trend(df, 'Members'), 0)
attendance_pred = round(predict_trend(df, 'Event_Attendance'), 0)
renewals_pred = round(predict_trend(df, 'Membership_Renewals'), 0)
col4, col5, col6 = st.columns(3)
col4.metric("Predicted Members", members_pred, f"+{members_pred - df['Members'].iloc[-1]}")
col5.metric("Predicted Attendance", attendance_pred, f"+{attendance_pred - df['Event_Attendance'].iloc[-1]}")
col6.metric("Predicted Renewals", renewals_pred, f"+{renewals_pred - df['Membership_Renewals'].iloc[-1]}")

st.subheader("Membership Trends")
chart_data = df.melt(id_vars='Month', value_vars=['Members', 'Event_Attendance', 'Membership_Renewals'])
st.line_chart(chart_data.pivot_table(index='Month', columns='variable', values='value'))

logger.info(f"Dashboard accessed at {datetime.now()}")