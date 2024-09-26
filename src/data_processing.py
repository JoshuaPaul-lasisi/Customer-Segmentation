import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load raw data from CSV file."""
    return pd.read_csv(file_path, encoding='ISO-8859-1')

def clean_data(df):
    """Handle missing values, remove duplicates, and filter data."""
    # Drop rows with missing CustomerID as they are critical for segmentation
    df = df.dropna(subset=['CustomerID'])
    
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with negative or zero Quantity and UnitPrice
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    return df

def preprocess_data(df):
    """Create new features and prepare data for clustering."""
    # Create TotalPrice (Quantity * UnitPrice)
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    # Group data by CustomerID and aggregate metrics
    customer_data = df.groupby('CustomerID').agg({
        'InvoiceNo': 'count',    # Number of purchases
        'Quantity': 'sum',       # Total items purchased
        'TotalPrice': 'sum'      # Total money spent
    }).rename(columns={'InvoiceNo': 'NumPurchases', 'Quantity': 'TotalQuantity'})

    return customer_data

def scale_data(df):
    """Standardize the data using StandardScaler."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    return scaled_data

# Main function to process the raw data
def process_data(file_path):
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    customer_data = preprocess_data(cleaned_data)
    scaled_customer_data = scale_data(customer_data)
    
    return scaled_customer_data, customer_data
