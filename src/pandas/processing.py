import pandas as pd
import datetime

# ===== Lockdown Date 2021
date_lockdown = datetime.datetime(2021,6,11,0,0)

# ===== Cases (Age Range)
df = pd.read_csv("data/c19/Cases (Age Range).csv")
df['datetime'] = df['notification_date'].apply(datetime.datetime.fromisoformat)

notification_dates = df['datetime'].unique()
df_sorted = pd.DataFrame(index=notification_dates)

for group in df['age_group'].unique():
    temp_df = df[df['age_group'] == group]['datetime'].value_counts()\
    .rename_axis("notifcation_date").to_frame(group)
    df_sorted = pd.concat([df_sorted,temp_df], axis=1)
