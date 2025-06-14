import pandas as pd

# Load the original dataset
df = pd.read_csv(
    'C:/Users/jacse/OneDrive/Documents/nyc-taxi-data-warehouse/data/SampleSuperstore.csv',
    encoding='ISO-8859-1'
)

# Select relevant columns for the fact table
fact_sales = df[[
    'Order ID',
    'Order Date',
    'Ship Date',
    'Ship Mode',
    'Customer ID',
    'Product ID',
    'Sales',
    'Quantity',
    'Discount',
    'Profit'
]].copy()

# Rename columns to snake_case
fact_sales.rename(columns={
    'Order ID': 'order_id',
    'Order Date': 'order_date',
    'Ship Date': 'ship_date',
    'Ship Mode': 'ship_mode',
    'Customer ID': 'customer_id',
    'Product ID': 'product_id'
}, inplace=True)

# Convert date columns to datetime format for easier analysis later
fact_sales['order_date'] = pd.to_datetime(fact_sales['order_date'])
fact_sales['ship_date'] = pd.to_datetime(fact_sales['ship_date'])

# Save fact table as CSV
fact_sales.to_csv('data/fact_sales.csv', index=False)

print("fact_sales table created with", len(fact_sales), "rows")
print(fact_sales.head())
