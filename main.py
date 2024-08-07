import pandas as pd
import matplotlib.pyplot as plt

file_path = 'demo_test1.json'

df = pd.read_json(file_path)

# Chuyển đổi cột 'funding_date' thành kiểu datetime
df['funding_date'] = pd.to_datetime(df['funding_date'])

# 1. 5 công ty tuyển nhiều job nhất
top_5_companies_jobs = df['company_name'].value_counts().head(5)
print(
5
công
ty
tuyển
nhiều
job
nhất:)
print(top_5_companies_jobs)

# 2. 5 công ty có funding cao nhất
top_5_companies_funding = df.groupby('company_name')['funding_amount'].sum().sort_values(ascending=False).head(5)
print(\n5
công
ty
có
funding
cao
nhất:)
print(top_5_companies_funding)

# 3. 5 công ty có funding gần đây nhất
top_5_recent_funding = df.sort_values(by='funding_date', ascending=False).drop_duplicates('company_name').head(5)
print(\n5
công
ty
có
funding
gần
đây
nhất:)
print(top_5_recent_funding[['company_name', 'funding_amount','funding_date']])

# Vẽ biểu đồ
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Biểu đồ 5 công ty tuyển nhiều job nhất
top_5_companies_jobs.plot(kind='bar', ax=axes[0], color='skyblue')
axes[0].set_title('Top 5 Companies with Most Job Listings')
axes[0].set_xlabel('Company Name')
axes[0].set_ylabel('Number of Job Listings')

# Biểu đồ 5 công ty có funding cao nhất
top_5_companies_funding.plot(kind='bar', ax=axes[1], color='lightgreen')
axes[1].set_title('Top 5 Companies with Highest Funding')
axes[1].set_xlabel('Company Name')
axes[1].set_ylabel('Total Funding Amount')

# Biểu đồ 5 công ty có funding gần đây nhất
recent_funding_data = top_5_recent_funding.set_index
