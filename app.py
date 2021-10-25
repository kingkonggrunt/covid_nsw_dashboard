import os

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from src import assets
from src import elements
from src.tabs import content as TabContent
from src.tabs import tabs as Tabs
from src import data
from src.graph.GraphBuilder import GraphBuilder


import pandas as pd
from src.processing import processing

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions=True
server = app.server

# ===== Data Object =====
data = data.CovidData(update=None)

# =====             =====

# ===== Dashboard Layout =====
banner = elements.Banner()
tabs = Tabs.Tabs()

tab_0 = TabContent.Tab0Homepage()
tab_1 = TabContent.Tab1()
tab_cases_postcode = TabContent.TabCasesPostCode()
tab_active_routes = TabContent.TabActiveRoutes()

app.layout = html.Div(
    id="covid_nsw_dashboard",
    children=[
    banner.build(),
    html.Div(
        id="dashboard-container",
        children=[
            tabs.build(),
            html.Div(id="tab-content"),
        ]
    )
    ]
)

@app.callback(
    [Output("tab-content", "children")],
    [Input("dashboard-tabs", "value")],
)
def render_tab_content(tab_switch):

    tab_to_content = {
        "tab0":tab_0.build_child,
        "tab1":tab_1.build_child,
        "tab_cases_postcode":tab_cases_postcode.build_child,
        "tab_active_routes":tab_active_routes.build_child,
    }

    return tab_to_content[tab_switch]()


@app.callback(
    Output("postcode-total-string", "children"),
    Input("postcode_selector", "value")
)
def _return_postcode_total(postcode):
    df = data.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
    _postcode_totals = df['postcode'].value_counts().rename_axis("postcode").to_frame("count")

    total = _postcode_totals.loc[postcode]['count']
    return f"Total for {postcode}: {total}"

# =====                  =====

if __name__ == '__main__':
    data.update(type=None)
    app.run_server(debug=True)
