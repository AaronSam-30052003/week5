import pandas as pd
import numpy as np
df = pd.read_csv("data/customer_orders_updated.csv")
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df = df.dropna(subset=['delivery_date', 'customer_id'])
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)
delay_summary = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)
delay_summary.to_csv("data/delay_summary.csv", header=["total_delays"])
print("Top 5 delayed customers:")
print(delay_summary.head(5))
