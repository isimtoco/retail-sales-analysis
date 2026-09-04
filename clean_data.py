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

# Fill missing item names
df['Item'] = df['Item'].fillna('Unknown')

# Convert date
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

