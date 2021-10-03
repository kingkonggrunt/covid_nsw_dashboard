from dash import dcc
from dash import html

from src import assets

class Banner:
    def __init__(self):

        self._title = html.Div(
            id="banner-title",
            children=[
                html.H5("COVID NSW DASHBOARD"),
                html.H6("by DCC")
            ]
        )

        self._button = html.Div(
            id="banner-buttons",
            children=[
                html.A(
                    children=html.Button("NSW COVID-19 DATA"),
                    href="https://data.nsw.gov.au/nsw-covid-19-data"
                ),
                html.A(
                    html.Img(id="nsw_gov_logo", src=assets.get_asset_url("nsw_government_logo.jpg")
                        , width=60, height=50
                    ),
                    href="https://www.nsw.gov.au/"
                )
            ]
        )

    def build(self):
        return html.Div(
            id="banner",
            className="banner",
            children=[
                self._title,
                self._button
            ]
        )

class Tabs:
    def __init__(self):

        self._tabs = [
            dcc.Tab(
                id="Homepage",
                label="Homepage",
                value="tab0",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"
            ),
            dcc.Tab(
                id="Case Locations",
                label="Covid Case Locations",
                value="tab1",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected",
            ),
            dcc.Tab(
                id="Active Flight and Public Transport Routes",
                label='Active Flight/Public Transport Routes',
                value="tab_active_routes",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"

            )
        ]


    def build(self):
        return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
            id="dashboard-tabs",
            value="tab0",
            className="dashboard-tabs",
            children=self._tabs
            )
        ]
        )

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

        self._title = html.Div(
            id="tab1",
            children=html.P(
                "Active Flight and Public Transport Routes"
            )
        )

    def build_child(self):
        return [
            self._title
        ]
