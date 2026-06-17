import pandas as pd

df = pd.read_csv('saas_subscriptions.csv')

total = len(df)
active = len(df[df['Status']=='Active'])
cancelled = len(df[df['Status']=='Cancelled'])

mrr = df[df['Status']=='Active']['Monthly_Revenue'].sum()
arpu = df['Monthly_Revenue'].mean()
churn = (cancelled/total)*100

print('Total Customers:', total)
print('Active Customers:', active)
print('Cancelled Customers:', cancelled)
print('MRR:', mrr)
print('ARPU:', round(arpu,2))
print('Churn Rate:', round(churn,2), '%')

print('\nRevenue by Plan')
print(df.groupby('Plan')['Monthly_Revenue'].sum())
