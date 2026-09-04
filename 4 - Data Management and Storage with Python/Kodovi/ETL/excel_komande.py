import pandas as pd
# Definisemo sve operacije u funkcije
 
# Extract data
def extract_user_data(file_name):
    return pd.read_excel(file_name)
 
# Filter data
def filter_users(data):
    mask = (pd.Timestamp.today() - data['rental_date']) > pd.Timedelta(days=31)
    return data[mask]
 
# Sort data
def sort_data(data):
    return data.sort_values(by='rental_date', ascending=True)
 
# Add new column
def add_new_column(data):
    data["overdue_days"] = (pd.Timestamp.today() - data['rental_date']).dt.days - 31
    return data
 
# Remove columns
def remove_columns(data):
    data = data.drop(['address', 'gender', 'city', 'active'], axis=1)
    return data
 
# Load data
def load_data(data):
    data.to_excel("overdue_users.xlsx", index=False)