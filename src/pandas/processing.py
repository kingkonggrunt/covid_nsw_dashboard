import pandas as pd
import datetime

# ===== Lockdown Date 2021
date_lockdown = datetime.datetime(2021,6,11,0,0)


# sort_group_value_counts_by_date

def sort_column_value_counts_by_group(df, column, group):
    dates = df[column].unique()
    df_out = pd.DataFrame(index=dates) # create a new df for output

    for g in df[group].unique(): # finds the value counts of each date, for each group
        temp = df[df[group] == g][column]\
        .value_counts().rename_axis(column).to_frame(g)
        df_out = pd.concat([df_out, temp], axis=1)

    return df_out

def value_counts_to_df(df, col, count_name):
    return df[col].value_counts().rename_axis(col).to_frame(count_name)

# ===== Cases (Age Range)
df = pd.read_csv("data/c19/Cases (Age Range).csv", parse_dates=['notification_date'])
df_age_overtime = sort_column_value_counts_by_group(df, column='notifcation_date', group='age_group')

# ===== Cases (Location)
df = pd.read_csv('data/c19/Cases (Location).csv', parse_dates=['notification_date'])

total_cases = df['notification_date'].value_counts().rename_axis("notification_date").to_frame("count")
total_postcode = df['postcode'].value_counts().rename_axis("postcode").to_frame("count")
total_lhd = df['lhd_2010_name'].value_counts().rename_axis("local health district").to_frame("count")
total_lga = df['lga_name19'].value_counts().rename_axis("local government area").to_frame("count")

postcode_overtime = sort_column_value_counts_by_group(df, 'notification_date', 'postcode')
lga_overtime = sort_column_value_counts_by_group(df, 'notification_date', 'lga_name19')
lhd_overtime = sort_column_value_counts_by_group(df, 'notifcation_date', 'lhd_2010_name')

# ===== Cases (Source)
df = pd.read_csv('data/c19/Cases (Source).csv', parse_dates=['notification_date'])

source_overtime = sort_column_value_counts_by_group(df, 'notification_date', 'likely_source_of_infection')
total_source = value_counts_to_df(df, "likely_source_of_infection", "count")

# ===== Cases (Date,Location,Source)
df = pd.read_csv('data/c19/Cases (Date,Location,Source).csv', parse_dates=['notification_date'])

source_postcode = sort_column_value_counts_by_group(df, 'likely_source_of_infection', 'postcode')
source_lhd = sort_column_value_counts_by_group(df, 'likely_source_of_infection', 'lhd_2010_name')
source_lga = sort_column_value_counts_by_group(df, 'likely_source_of_infection', "lga_name19")
