import pandas as pd
import numpy as np

num_rows = 10000  
campaigns = ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D']
dates = pd.date_range(start="2023-01-01", end="2024-12-31")

data = {
    "Campaign Name": np.random.choice(campaigns, size=num_rows),
    "Date": np.random.choice(dates, size=num_rows),
    "Impressions": np.random.randint(1000, 100000, size=num_rows),
    "Clicks": np.random.randint(100, 10000, size=num_rows),
    "Spend": np.round(np.random.uniform(50, 5000, size=num_rows), 2),
    "Conversions": np.random.randint(1, 500, size=num_rows),
    "Revenue": np.round(np.random.uniform(100, 10000, size=num_rows), 2),
}

# Create DataFrame
mock_data = pd.DataFrame(data)

# Save to CSV
file_path = 'data.csv'
mock_data.to_csv(file_path, index=False)

file_path
