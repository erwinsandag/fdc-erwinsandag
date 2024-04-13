import pandas as pd

# Define the path to the input data file
input_file_path = "data/restaurant_data.xlsx"

# Read the input data into a pandas DataFrame
data = pd.read_excel(input_file_path)

# Perform data transformation tasks (e.g., cleansing, fixing typos, mapping column names)

# Drop rows where the name or ingredients are not available
data = data.dropna(subset=['Product Name', 'Ingredients on Product Page'])

# Fix any typos in the data fields (if needed)
# Example: data['Column'] = data['Column'].str.replace('typo', 'corrected_value')

# Map column names to reasonable data shape names (if needed)
# Example: data = data.rename(columns={'old_name': 'new_name'})

# Define the path to the output data file
output_file_path = "data/output_data.csv"

# Write the transformed data to a new file (e.g., CSV format)
data.to_csv(output_file_path, index=False)

print("Data transformation completed. Output saved to:", output_file_path)
