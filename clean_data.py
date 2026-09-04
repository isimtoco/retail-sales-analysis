import pandas as pd

df = pd.read_csv('data/retail_store_sales.csv')

# Check missing values
print(df.isnull().sum())

# Fill missing Total Spent when price and quantity are available
mask = (
    df['Total Spent'].isnull()
    & df['Price Per Unit'].notnull()
    & df['Quantity'].notnull()
)

df.loc[mask, 'Total Spent'] = (
    df.loc[mask, 'Price Per Unit']
    * df.loc[mask, 'Quantity']
)

# Fill missing Quantity when total spent and price are available
mask = (
    df['Quantity'].isnull()
    & df['Total Spent'].notnull()
    & df['Price Per Unit'].notnull()
)
df.loc[mask, 'Quantity'] = (
    df.loc[mask, 'Total Spent']
    / df.loc[mask, 'Price Per Unit']
)

# Fill missing Price Per Unit when total spent and quantity are available
mask = (
    df['Price Per Unit'].isnull()
    & df['Total Spent'].notnull()
    & df['Quantity'].notnull()
)
df.loc[mask, 'Price Per Unit'] = (
    df.loc[mask, 'Total Spent']
    / df.loc[mask, 'Quantity']
)

# Fill missing item names
df['Item'] = df['Item'].fillna('Unknown')

# Convert date
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Create month column
df['Order_Month'] = df['Transaction Date'].dt.to_period('M')

# Flag repeat customers (first purchase date per customer)
df['First_Purchase'] = df.groupby('Customer ID')['Transaction Date'].transform('min')
df['Is_Repeat'] = df['Transaction Date'] > df['First_Purchase']

# Label discount status (NaN means unrecorded, not "no discount")
df['Discount_Status'] = df['Discount Applied'].map({True: 'Discounted', False: 'Full Price'}).fillna('Unknown')

# Remove rows where sales amount still cannot be determined
df = df.dropna(subset=['Total Spent'])

# Save cleaned data
df.to_csv('data/cleaned_retail_sales.csv', index=False)