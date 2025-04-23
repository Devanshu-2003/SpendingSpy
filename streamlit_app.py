import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from spending_spy import (
    process_csv,
    plot_category_summary,
    plot_bar_chart,
    analyze_monthly_spending,
    top_merchants,
    cumulative_spending_trend,
    cluster_transactions
)

st.set_page_config(page_title="SpendingSpy", layout="wide")
st.title("💸 SpendingSpy: Personal Finance Analyzer")

st.markdown("Upload your bank/exported CSV and we'll auto-categorize, visualize, and cluster your transactions!")

uploaded_file = st.file_uploader("Upload your transaction CSV", type=["csv"])

if uploaded_file:
    uploaded_file.seek(0)  # Reset file pointer
    df = process_csv(uploaded_file)
    df = cluster_transactions(df)

    st.subheader("📋 Categorized Transactions")
    st.dataframe(df[['date', 'description', 'amount', 'category', 'cluster']], use_container_width=True)

    st.subheader("📊 Spending Visualizations")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Spending by Category (Pie)**")
        fig1 = plot_category_summary(df)
        st.pyplot(fig1)

    with col2:
        st.markdown("**Spending by Category (Bar)**")
        fig2 = plot_bar_chart(df)
        st.pyplot(fig2)

    st.markdown("### 📆 Monthly Spending Breakdown")
    fig3 = analyze_monthly_spending(df)
    st.pyplot(fig3)

    st.markdown("### 📈 Cumulative Spending Over Time")
    fig4 = cumulative_spending_trend(df)
    st.pyplot(fig4)

    st.markdown("### 🏪 Top Merchants by Spend")
    fig5 = top_merchants(df)
    st.pyplot(fig5)

    # Download cleaned CSV
    st.markdown("### 📥 Download Cleaned CSV")
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Categorized CSV",
        data=csv_data,
        file_name="categorized_output.csv",
        mime="text/csv"
    )
