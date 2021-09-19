import csv
import requests
import datetime
from os import path, makedirs

import pandas as pd

makedirs("data", exist_ok=True)
makedirs("data/metadata", exist_ok=True)

def download_csv(url, filename):
    with requests.Session() as s:
        response = s.get(url)

        with open(f"{filename}.csv", 'w') as f:
            writer = csv.writer(f)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))

def update_last_updated():
    # TODO:
    pass

class CovidData:
    """
    Class to handle data from NSW Covid Data
    """
    def __init__ (self, update=None):
        self._data = "data" # Data dir

        if update == "light":
            urls = {
                "Cases (Date,Location,Source)":"https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv",
                "Cases (Age Range)":"https://data.nsw.gov.au/data/dataset/3dc5dc39-40b4-4ee9-8ec6-2d862a916dcf/resource/24b34cb5-8b01-4008-9d93-d14cf5518aec/download/confirmed_cases_table2_age_group.csv",
                "Cases (Source)":"https://data.nsw.gov.au/data/dataset/c647a815-5eb7-4df6-8c88-f9c537a4f21e/resource/2f1ba0f3-8c21-4a86-acaf-444be4401a6d/download/confirmed_cases_table3_likely_source.csv",
                "Cases (Location)": "https://data.nsw.gov.au/data/dataset/aefcde60-3b0c-4bc0-9af1-6fe652944ec2/resource/21304414-1ff1-4243-a5d2-f52778048b29/download/confirmed_cases_table1_location.csv",
            }

            for f,u in urls.items():
                download_csv(u, path.join(self._data,f))
        elif update == "all":
            pass
        elif update == "heavy":
            pass
        else:
            pass

    def load_csv(self, filename):
        """
        Requires the .csv file extensions at the end
        """
        data="data"
        df = pd.load_csv(path.join(data,filename))
        return df
