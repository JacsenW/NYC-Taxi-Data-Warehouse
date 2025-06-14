import pandas as pd

# Load the original dataset
df = pd.read_csv(
    'C:/Users/jacse/OneDrive/Documents/nyc-taxi-data-warehouse/data/SampleSuperstore.csv',
    encoding='ISO-8859-1'
)

# Extract customer-related columns, drop duplicates
dim_customer = df[['Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country', 'Postal Code', 'Region']].drop_duplicates().reset_index(drop=True)

# Rename columns for consistency and easier querying
dim_customer.rename(columns={
    'Customer ID': 'customer_id',
    'Customer Name': 'customer_name',
    'Postal Code': 'postal_code'
}, inplace=True)

# Save to CSV (this will be your dimension table)
dim_customer.to_csv('data/dim_customer.csv', index=False)

print("dim_customer table created with", len(dim_customer), "rows")
print(dim_customer.head())
