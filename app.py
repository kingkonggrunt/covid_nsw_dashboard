import os

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from src import assets
from src import elements
from src import data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# ===== Data Object =====
data = data.CovidData(update=None)

# =====             =====

# ===== Dashboard Layout =====
banner = elements.Banner()
tabs = elements.Tabs()

tab_0 = elements.Tab0Homepage()
tab_1 = elements.Tab1()
tab_active_routes = elements.TabActiveRoutes()

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
    if tab_switch == "tab0":
        return tab_0.build_child()
    if tab_switch == "tab1":
        return tab_1.build_child()
    if tab_switch == "tab_active_routes":
        return tab_active_routes.build_child()

# =====                  =====

if __name__ == '__main__':
    data.update(type="all")
    app.run_server(debug=True)
