import pandas as pd
import requests
# Downloading Fed rate dataset
fed_rate_url = 'https://markets.newyorkfed.org/read?productCode=50&eventCodes=500&limit=25&startPosition=0&sort=postDt:-1&format=xlsx'
response = requests.get(fed_rate_url)
with open('fed_rate.xlsx', 'wb') as f:
    f.write(response.content)
fed_rate = pd.read_excel('fed_rate.xlsx', sheet_name='Results', skiprows=1)
fed_rate.to_csv('fed_rate.csv', index=False)



# Downloading National house price dataset
# Downloading Building permit dataset
national_house_price_url = 'https://www.fhfa.gov/DataTools/Downloads/Documents/HPI/HPI_PO_monthly_hist.xls'
response = requests.get(national_house_price_url)
with open('national_house_price.xls', 'wb') as f:
    f.write(response.content)
national_house_price = pd.read_excel('national_house_price.xls', sheet_name='Downloadable--Series to91--FLAT', header=1)
national_house_price.to_csv('national_house_price.csv', index=False)


# Downloading Building permit dataset
building_permit_url = 'https://www.census.gov/construction/nrc/xls/starts_cust.xls'
response = requests.get(building_permit_url)
with open('building_permit.xls', 'wb') as f:
    f.write(response.content)
building_permit = pd.read_excel('building_permit.xls', sheet_name='StartsAnn', skiprows=2)
building_permit.to_csv('building_permit.csv', index=False)



import pandas as pd

# Load the data from the CSV file into a pandas DataFrame
data = pd.read_csv('fed_rate.csv', header=None)

# Drop the first row
data = data.drop(0)

# Extract the first, third, and tenth columns and save them to a new DataFrame
new_data = data.iloc[:, [0, 2, 9]]

# Rename the columns to 'Date', 'RealRate', and 'TargetRate'
new_data.columns = ['Date', 'RealRate', 'TargetRate']

# Save the new DataFrame to a new CSV file
new_data.to_csv('new_fed_rate.csv', index=False)


import pandas as pd

# Load the data from the CSV file into a pandas DataFrame
data = pd.read_csv('building_permit.csv')

# Drop the first 7 rows
data = data.iloc[7:]

# Extract the first two columns and save them to a new DataFrame
new_data = data.iloc[:, :2]

# Rename the columns to 'year' and 'volume'
new_data.columns = ['year', 'volume']

# Save the new DataFrame to a new CSV file
new_data.to_csv('new_data_file.csv', index=False)


import pandas as pd

# Read in the CSV file
df = pd.read_csv('national_house_price.csv')

# Remove the first two rows
df = df.iloc[2:]
# Extract the first column as the Date column
df['Date'] = pd.to_datetime(df.iloc[:, 0])

# Extract the 21st column as the Price column
df['Price'] = df.iloc[:, 20]

# Keep only the Date and Price columns
df = df[['Date', 'Price']]

# Save the result to a new CSV file
df.to_csv('new_national_house_price.csv', index=False)
