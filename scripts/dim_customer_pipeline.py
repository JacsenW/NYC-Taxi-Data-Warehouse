import pandas as pd
import os 


# Path to the source full dataset
source_path = 'C:/Users/jacse/OneDrive/Documents/nyc-taxi-data-warehouse/data/SampleSuperstore.csv'

# Path to your existing dim_customer table
dim_customer_path = 'data/dim_customer.csv'

# Load full dataset (with encoding to avoid errors)
source_df = pd.read_csv(
    source_path,
    encoding='ISO-8859-1'
)

#Extract relevant columns and drop duplicates
new_customer = source_df[['Customer ID', 'Customer Name', 'Segment', 'City', 'State', 'Country', 'Postal Code', 'Region']].drop_duplicates()

#Rename columns for consistency
new_customer.rename(columns={
    'Customer ID': 'customer_id',
    'Customer Name': 'customer_name',
    'Postal Code': 'postal_code'
}, inplace=True)

# Load existing dim_customer table if it exists
if os.path.exists(dim_customer_path):
    dim_customer_df = pd.read_csv(dim_customer_path)
else:
    dim_customer_df = pd.DataFrame(columns=new_customer.columns)

#Find new customers that are not already in the dim_customer table
merged = new_customer.merge(
    dim_customer_df,
    on='customer_id',
    how='left',
    indicator=True
)

#Keep only new customers not in existing dim_customer
incremental_customers = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])

# Append new customers to the existing dim_customer table
updated_dim_customer = pd.concat([dim_customer_df, incremental_customers], ignore_index=True)
# Save the updated dim_customer table
updated_dim_customer.to_csv(dim_customer_path, index=False)
print(f"Added {len(incremental_customers)} new customers. Updated dim_customer now has {len(updated_dim_customer)} rows.")

