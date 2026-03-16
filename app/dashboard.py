import streamlit as st
import sqlite3
import pandas as pd
import threading

from file_ingestor import tail_log
from processor import process_log


LOG_FILE = "logs/sample_logs.log"


def start_pipeline():

    for log in tail_log(LOG_FILE):

        process_log(log)


# Start pipeline only once
if "pipeline_started" not in st.session_state:

    thread = threading.Thread(target=start_pipeline, daemon=True)
    thread.start()

    st.session_state.pipeline_started = True


st.title("AI SOC Dashboard")

conn = sqlite3.connect("logs.db")

df = pd.read_sql("SELECT * FROM logs", conn)


if df.empty:

    st.warning("No logs processed yet")

else:

    st.dataframe(df)

    if "classification" in df.columns:

        chart = df["classification"].value_counts()

        st.bar_chart(chart)