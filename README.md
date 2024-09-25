# Customer Segmentation Project

## Overview

This project applies clustering techniques to segment customers based on their purchasing behavior. We utilize Python for data preprocessing and clustering, PostgreSQL for storing customer data, and Streamlit for a web-based dashboard. A Power BI dashboard is provided for additional visualization.

## Technologies

- **Python**: Data cleaning, clustering (KMeans, PCA).
- **Streamlit**: Dashboard for interactive visualization.
- **PostgreSQL**: Database to store customer segmentation results.
- **Power BI**: Data visualization dashboard.

## Project Structure
├── data
│   ├── raw               # Raw data files
│   └── processed         # Processed data
├── notebooks             # Jupyter notebooks for EDA
│   └── exploratory_data_analysis.ipynb
├── reports               # Generated reports and visualizations
│   ├── report.md
│   └── powerbi_dashboard.pbix
├── src                   # Source code for data processing, modeling, and Streamlit app
│   ├── data_processing.py
│   ├── clustering_model.py
│   └── streamlit_app.py
├── sql                   # SQL scripts for database setup
│   └── create_tables.sql
├── README.md             # Project overview and instructions
└── requirements.txt      # List of dependencies
Installation
Clone this repository:
bash
Copy code
git clone <repo-url>
Install the required libraries:
bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy code
streamlit run src/streamlit_app.py
Usage
Upload the customer transaction CSV file via the Streamlit app.
Explore the segmented customer data and download the results.
View additional insights through the Power BI dashboard.
yaml
Copy code

---

### Final Notes

- You can customize this further with specific visualizations, add
