
import pandas as pd
import streamlit as st

def show_history(history):

    if history:

        history_df = pd.DataFrame(history)

        st.dataframe(history_df)

        csv = history_df.to_csv(index=False)

        st.download_button(
            label="📥 Download Analytics CSV",
            data=csv,
            file_name="analytics_history.csv",
            mime="text/csv"
        )

