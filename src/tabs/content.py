from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px

from src.data import CovidData

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

        self._title = html.Div(
            id="tab1",
            children=html.P(
                "Heading for Tab1: Something"
            )
        )

    def build_child(self):
        return [
            self._title
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
