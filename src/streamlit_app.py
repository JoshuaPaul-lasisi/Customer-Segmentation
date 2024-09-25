import streamlit as st
import pandas as pd
import plotly.express as px
from data_processing import process_data
from clustering_model import run_clustering

st.title("Customer Segmentation Dashboard")

# Sidebar
st.sidebar.header("Upload your data")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    # Process uploaded data
    scaled_data, customer_data = process_data(uploaded_file)
    
    # Display processed data
    st.subheader("Processed Customer Data")
    st.dataframe(customer_data.head())
    
    # Run clustering
    clusters, _ = run_clustering(scaled_data)
    
    # Add cluster labels to customer_data
    customer_data['Cluster'] = clusters
    
    # Plot cluster distribution
    st.subheader("Customer Clusters")
    fig = px.scatter(customer_data, x='TotalQuantity', y='TotalPrice', color='Cluster', title="Customer Clusters")
    st.plotly_chart(fig)

    # Download option for clustered data
    csv = customer_data.to_csv(index=False)
    st.download_button("Download Clustered Data", data=csv, file_name='customer_clusters.csv', mime='text/csv')
else:
    st.write("Upload a CSV file to get started.")
