import pandas as pd

# Load CSV with proper encoding
df = pd.read_csv(
    'C:/Users/jacse/OneDrive/Documents/nyc-taxi-data-warehouse/data/SampleSuperstore.csv',
    encoding='ISO-8859-1'
)

# Show the first 5 rows
print("\n📌 Sample data:")
print(df.head())

# Show basic info
print("\n📌 Dataset info:")
print(df.info())

# Check for duplicates
print("\n📌 Duplicate rows:")
print(df.duplicated().sum())

# Check for null values
print("\n📌 Missing values:")
print(df.isnull().sum())

# Show column names
print("\n📌 Columns:")
print(df.columns.tolist())

# Check unique values in 'Order Date' (first 10)
print("\n📌 Unique order dates (first 10):")
print(df['Order Date'].unique()[:10])


#Convert 'Order Date' and Ship Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
print(df.dtypes[['Order Date', 'Ship Date']])

df.drop(columns=['Row ID'], inplace=True)

date_df = df[['Order Date']].copy()
date_df['Year'] = date_df['Order Date'].dt.year
date_df['Month'] = date_df['Order Date'].dt.month
date_df['Day'] = date_df['Order Date'].dt.day
date_df['Week'] = date_df['Order Date'].dt.isocalendar().week
date_df['Quarter'] = date_df['Order Date'].dt.quarter
date_df = date_df.drop_duplicates().reset_index(drop=True)

df.to_csv('data/cleaned_superstore.csv', index=False)
date_df.to_csv('data/dim_date.csv', index=False)

