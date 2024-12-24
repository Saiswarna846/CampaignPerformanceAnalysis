import pandas as pd

file_path = 'data.csv' 
data = pd.read_csv(file_path)

data.fillna(0, inplace=True) 

data['Date'] = pd.to_datetime(data['Date'])
data['Spend'] = data['Spend'].astype(float)

data['CTR'] = (data['Clicks'] / data['Impressions']) * 100
data['ROAS'] = data['Revenue'] / data['Spend']
data['Conversion Rate'] = (data['Conversions'] / data['Clicks']) * 100

top_campaigns = data.sort_values(by='ROAS', ascending=False).head(5)
print(top_campaigns)

daily_trends = data.groupby('Date').sum()
print(daily_trends)

data.to_csv('processed_campaign_data.csv', index=False)
