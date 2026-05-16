
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# ENTERPRISE ANALYTICS
# =========================================

def show_advanced_analytics(history):

    st.write("## 📊 Enterprise Analytics")

    if not history:

        st.warning(
            "No analytics data available."
        )

        return

    history_df = pd.DataFrame(history)

    # =========================================
    # KPI CARDS
    # =========================================

    total_docs = len(history_df)

    avg_confidence = round(
        history_df["Confidence"].mean(),
        2
    )

    top_category = (
        history_df["Category"]
        .value_counts()
        .idxmax()
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Documents",
            total_docs
        )

    with col2:

        st.metric(
            "🎯 Avg Confidence",
            f"{avg_confidence}%"
        )

    with col3:

        st.metric(
            "🏆 Top Category",
            top_category
        )

    # =========================================
    # BAR CHART
    # =========================================

    st.write("## 📈 Confidence Scores")

    bar_fig = px.bar(

        history_df,

        x="Category",

        y="Confidence",

        color="Category",

        text="Confidence"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

    # =========================================
    # PIE CHART
    # =========================================

    st.write("## 🥧 Category Distribution")

    pie_fig = px.pie(

        history_df,

        names="Category",

        title="Document Categories"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    # =========================================
    # LINE CHART
    # =========================================

    st.write("## 📉 Confidence Trends")

    history_df["Index"] = range(
        1,
        len(history_df) + 1
    )

    line_fig = px.line(

        history_df,

        x="Index",

        y="Confidence",

        markers=True
    )

    st.plotly_chart(
        line_fig,
        use_container_width=True
    )

    # =========================================
    # TABLE
    # =========================================

    st.write("## 📋 Analytics Table")

    st.dataframe(
        history_df,
        use_container_width=True
    )

    # =========================================
    # EXPORT CSV
    # =========================================

    csv = history_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Analytics CSV",
        data=csv,
        file_name="analytics.csv",
        mime="text/csv"
    )

