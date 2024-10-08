import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'thulai9.csv'
df = pd.read_csv(file_path)

# Define a function to assign scores based on event participation
def assign_score(event_id):
    return 1 if pd.notna(event_id) else 0

# Apply the 'assign_score' function to the 'event_id' column
df['event_id'] = df['event_id'].apply(assign_score)

# Select only the relevant columns
selected_columns = df[['company', 'funding amount', 'job', 'event_id', 'size', 'Label']]

# Remove duplicate rows (if any)
selected_columns.drop_duplicates(inplace=True)

# Filter out rows where 'event_id' is missing
filtered_df = selected_columns.dropna(subset=['event_id'])

# Group by 'company' and aggregate the data
hiring = filtered_df.groupby('company').agg({
    'funding amount': 'sum',  # Summing up the funding amount
    'job': 'count',           # Counting the number of jobs
    'event_id': 'max',      # Taking the maximum value of 'event_id' (0 or 1)
    'size': 'max',
   
}).reset_index()

# Rename the 'job' column to 'hiring' for clarity
hiring.rename(columns={'job': 'hiring'}, inplace=True)
hiring['score'] = (hiring['hiring'] * 0.6) + (hiring['funding amount'] * 0.3) + hiring['event_id']

# Sort the results by 'score' for better readability
hiring = hiring.sort_values(by='score', ascending=False)

results = 'output.xlsx'
hiring.to_excel(results, index = False)

print(f"Data has been exported to {results}")
