import csv
import requests
from src.helpers.TimeHelper import TimeHelper
import json
from os import path, makedirs

import pandas as pd

makedirs("data/data", exist_ok=True)
makedirs("data/metadata", exist_ok=True)

def text_manager(string):
    return string.decode('utf-8-sig', 'ignore')\
    .replace('\u200b', '')\
    .split(",")

def download_data(url, filename):
    with requests.Session() as s:
        response = s.get(url)

        if url.endswith(".csv"):
            with open(f"{filename}.csv", 'w') as f:
                writer = csv.writer(f)
                for line in response.iter_lines():
                    writer.writerow(text_manager(line))

        elif url.endswith(".json"):
            with open(f"{filename}.json", 'w') as f:
                json.dump(response.json(), f)

def update_last_updated():
    # TODO:
    pass

class CovidData:
    """
    Class to handle data from NSW Covid Data
    """
    def __init__ (self, update=None):
        self._data = "data/data" # Data dir

        self._urls = {
            "Cases (Date,Location,Source)":[
                "light","https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv"
            ],
            "Cases (Age Range)":[
                "light","https://data.nsw.gov.au/data/dataset/3dc5dc39-40b4-4ee9-8ec6-2d862a916dcf/resource/24b34cb5-8b01-4008-9d93-d14cf5518aec/download/confirmed_cases_table2_age_group.csv"
            ],
            "Cases (Source)":[
                "light","https://data.nsw.gov.au/data/dataset/c647a815-5eb7-4df6-8c88-f9c537a4f21e/resource/2f1ba0f3-8c21-4a86-acaf-444be4401a6d/download/confirmed_cases_table3_likely_source.csv"
            ],
            "Cases (Location)":[
                "light","https://data.nsw.gov.au/data/dataset/aefcde60-3b0c-4bc0-9af1-6fe652944ec2/resource/21304414-1ff1-4243-a5d2-f52778048b29/download/confirmed_cases_table1_location.csv"
            ],
            "Tests (Location)":[
                "heavy","https://data.nsw.gov.au/data/dataset/60616720-3c60-4c52-b499-751f31e3b132/resource/fb95de01-ad82-4716-ab9a-e15cf2c78556/download/pcr_testing_table1_location_agg.csv"
            ],
            "Tests (Age Range)":[
                "light","https://data.nsw.gov.au/data/dataset/793ac07d-a5f4-4851-835c-3f7158c19d15/resource/28730d42-675b-4573-ad71-8156313c73a1/download/pcr_testing_table2_age_group_agg.csv"
            ],
            "Clinics":[
                "light","https://data.nsw.gov.au/data/dataset/21c72b00-0834-464d-80f1-75fec38454ce/resource/85da884f-a9f5-4cb3-95e8-d6b81b0d2e3a/download/nsw-health-covid-19-test-clinics-20210920-1630.csv"
            ],
            "Case Locations":[
                "light","https://data.nsw.gov.au/data/dataset/0a52e6c1-bc0b-48af-8b45-d791a6d8e289/resource/f3a28eed-8c2a-437b-8ac1-2dab3cf760f9/download/covid-case-locations-20210921-1400.json"
            ],
            "Case Public Transport Routes":[
                "light","https://data.nsw.gov.au/data/dataset/033c84bd-e702-46aa-be17-60e46754c0de/resource/954de47e-959d-495f-a85e-23fe66aea395/download/nsw-covid-19-public-transport-route-20210915.csv"
            ],
            "Case Flights":[
                "light","https://data.nsw.gov.au/data/dataset/cae32b18-0156-401c-b4f4-15bcb29ef7bc/resource/3289ecee-7ca3-4638-8b9a-05c6009ee76a/download/nsw-covid-19-flights-20210725.csv.csv"
            ],
            # "COVID Safe Venues":[
                # "heavy","https://data.nsw.gov.au/data/dataset/80b88e79-79b1-4f2f-b961-a90591fc377d/resource/4a26e0f0-71e1-43bb-96a8-e1434bbce9d8/download/covidsafe-v3.csv"
            # ]
        }
        self.update(type=update)

    def update(self, type=None):
        if type in ['light', 'heavy']:
            for filename, metadata in self._urls.items():
                if metadata[0] == type:
                    print(f"{type.capitalize()} Updating: {filename}")
                    download_data(metadata[1], path.join(self._data,filename))
        elif type == "all":
            for filename, metadata in self._urls.items():
                download_data(metadata[1], path.join(self._data, filename))

        self._update_log(type=type)

    def _update_log(self, type=None):
        TH = TimeHelper()
        TH.set_timezone(tz="Australia/Sydney")
        TH._fmt = "%Y-%m-%d %H:%M:%S %Z%z"
        update_logs = {
            "all": "data/metadata/update_all.log",
            "light": "data/metadata/update_light.log",
            "heavy": "data/metadata/update_heavy.log",
        }

        if type in update_logs:
            with open(update_logs[type], "w") as f:
                f.write(TH.time_now_str)

    def load_csv(self, filename, **kwargs):
        """
        Requires the .csv file extension at the end
        """
        df = pd.read_csv(path.join(self._data,filename), **kwargs)
        return df
