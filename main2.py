import pandas as pd
import matplotlib.pyplot as plt

file_path = 'demo_test1.csv'

df = pd.read_csv(file_path)

df['funding_date'] = pd.to_datetime(df['funding_date'])

job_counts = df['company_name'].value_counts().head(5)
funding_info = df.drop_duplicates(subset=['company_name'])

# Kết hợp thông tin số lượng job và số tiền funding
top_5_jobs = pd.DataFrame({
    'Job Count': job_counts,
    'Funding Amount': funding_info.set_index('company_name').loc[job_counts.index, 'funding_amount']
})

top_5_funding = df.groupby('company_name')['funding_amount'].sum().nlargest(5)

recent_funding_unique = df.sort_values(by='funding_date', ascending=False).drop_duplicates(subset='company_name').head(5)

print(top_5_jobs)
print(\n5 công ty mới được funding gần đây nhất:)
print(recent_funding_unique[['company_name', 'funding_amount', 'funding_date']])
print(\n5 công ty có funding cao nhất:)
print(top_5_funding)


companies_jobs = set(top_5_jobs.index)
companies_funding = set(top_5_funding.index)
companies_recent = set(recent_funding_unique['company_name'])

# Bước 3: Tìm công ty xuất hiện ở ít nhất 2 trong 3 bảng
companies_2_of_3 = (companies_jobs & companies_funding) | (companies_jobs & companies_recent) | (companies_funding & companies_recent)

print(\nCác công ty nên hợp tác:)
print(companies_2_of_3)

# Vẽ biểu đồ với hai trục y
fig, ax1 = plt.subplots(figsize=(12, 6))

# Vẽ biểu đồ số lượng job
ax1.bar(top_5_jobs.index, top_5_jobs['Job Count'], color='skyblue', label='Số lượng job')
ax1.set_xlabel('Tên công ty')
ax1.set_ylabel('Số lượng job', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Tạo trục y thứ hai
ax2 = ax1.twinx()
ax2.plot(top_5_jobs.index, top_5_jobs['Funding Amount'], color='red', marker='o', label='Số tiền funding')
ax2.set_ylabel('Số tiền funding (đơn vị tiền tệ)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Thiết lập tiêu đề
plt.title('Top 5 Công ty tuyển nhiều job nhất và Số tiền funding')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
