import pandas as pd
import datetime

# ===== Lockdown Date 2021
date_lockdown = datetime.datetime(2021,6,11,0,0)


# sort_group_value_counts_by_date

def sort_date_value_counts_by_group(df, date, group):
    df[date] = pd.to_datetime(df[date]) #convert date col to datetime

    dates = df[date].unique()
    df_out = pd.DataFrame(index=dates) # create a new df for output

    for g in df[group].unique(): # finds the value counts of each date, for each group
        temp = df[df[group] == g][date]\
        .value_counts().rename_axis(date).to_frame(g)
        df_out = pd.concat([df_out, temp], axis=1)

    return df_out

# ===== Cases (Age Range)
df = pd.read_csv("data/c19/Cases (Age Range).csv")
df_age_overtime = sort_date_value_counts_by_group(df, date='notifcation_date', group='age_group')
