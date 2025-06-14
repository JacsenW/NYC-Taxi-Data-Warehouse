import pandas as pd

# Load the dataset again
df = pd.read_csv(
    'C:/Users/jacse/OneDrive/Documents/nyc-taxi-data-warehouse/data/SampleSuperstore.csv',
    encoding='ISO-8859-1'
)

# Extract product-related columns and remove duplicates
dim_product = df[['Product ID', 'Category', 'Sub-Category', 'Product Name']].drop_duplicates().reset_index(drop=True)

# Rename columns to snake_case
dim_product.rename(columns={
    'Product ID': 'product_id',
    'Product Name': 'product_name',
    'Sub-Category': 'sub_category'
}, inplace=True)

# Save to CSV
dim_product.to_csv('data/dim_product.csv', index=False)

print("dim_product table created with", len(dim_product), "rows")
print(dim_product.head())
