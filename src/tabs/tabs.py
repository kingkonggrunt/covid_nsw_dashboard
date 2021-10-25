from dash import dcc
from dash import html

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
                label="Cases (Age Group)",
                value="tab1",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected",
            ),
            dcc.Tab(
                id="Postcode",
                label="Cases (Postcode)",
                value="tab_cases_postcode",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"
            ),
            dcc.Tab(
                id="LGA",
                label="Cases (LGA)",
                value='tab_cases_lga',
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"
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
