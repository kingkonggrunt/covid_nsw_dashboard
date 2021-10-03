from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px

from src.data import CovidData
from src.pandas import processing

class Tab0Homepage:
    def __init__(self):

        self._title = html.Div(
            id="tab0-title",
            children=html.P(
                "Heading for Tab0: Homepage"
            )
        )

    def build_child(self):
        return [
            self._title
        ]

class Tab1:
    def __init__(self):

        self._data = CovidData()
        self._title = html.P("Age Groups Data")

    # ===== Graph Building
    def _bar_total(self):
        df = self._data.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.value_counts_to_df(df, "age_group", "cases")

        df.sort_index(ascending=True, inplace=True)
        df.reset_index(inplace=True)

        df['age_group'] = df['age_group'].apply(lambda x: x.replace("AgeGroup_", ""))

        fig = px.bar(df, x="age_group", y="cases",
            title="Total Cases by Age Group"
        )
        graph = dcc.Graph(
            id="age_group_total",
            figure=fig
        )
        return graph

    def _bar_total_normalize(self):
        df = self._data.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.value_counts_to_df(df, "age_group", "percent", normalize=True)

        df.sort_index(ascending=True, inplace=True)
        df.reset_index(inplace=True)

        df['percent'] = df['percent'].apply(lambda x: x*100)
        df['age_group'] = df['age_group'].apply(lambda x: x.replace("AgeGroup_", ""))

        fig = px.pie(df, names="age_group", values="percent",
            title="Total Cases by Age Group"
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        graph = dcc.Graph(
            id="age_group_total_normalize",
            figure=fig
        )
        return graph


    def build_child(self):
        return [
            html.Div(
                id="tab1",
                children=[
                    self._title,
                    self._bar_total(),
                    self._bar_total_normalize()
                ]
            )
        ]

class TabActiveRoutes:
    def __init__(self):

        self._data = CovidData()
        self._title = html.P("Active Flight and Public Transport Routes")

    # ===== This is the hard coded stuff for the generation of relavent data
    def _data_table_flight(self):
        df = self._data.load_csv("Case Flights.csv")
        table = dash_table.DataTable(
            id='flights_table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records')
        )
        return table

    def _data_table_public_transport(self):
        df = self._data.load_csv("Case Public Transport Routes.csv")
        table = dash_table.DataTable(
            id='public_transport_table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records')
        )
        return table
    # =====

    def build_child(self):
        return [
            html.Div(
            id="tab_active_routes_children",
            children=[
                self._title,
                html.P("Active Flight Routes"),
                self._data_table_flight(),
                html.P("Active Public Transport Routes"),
                self._data_table_public_transport()
            ]
            )
            #self._build_public_transport_data_table()
        ]
