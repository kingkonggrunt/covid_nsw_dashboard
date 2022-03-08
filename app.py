import os

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from src import assets
from src import elements
from src.buttons import TabButtons
from src import data
from src.content import Postcode

import pandas as pd
import src.processing

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions=True
server = app.server

# ===== Data Object =====
data = data.CovidData(update=None)

# =====             =====

# ===== Dashboard Layout =====
banner = elements.Banner()
# tab_buttons = TabButtons()

app.layout = html.Div(
    id="covid_nsw_dashboard",
    children=[
    banner.build(),
    html.Div(
        id="dashboard-container",
        children=[
            TabButtons.build(),
            html.Div(id="tab-content"),
        ]
    )
    ]
)

@app.callback(
    [Output("tab-content", "children")],
    [Input("dashboard-tabs", "value")],
)
def render_tab_content(tab):
    """
    Selecting a Tab (changing `dashboard-tabs` value), changes the
    `tab-content` child to be rendered
    """
    return TabButtons.tab_button_to_tab_content()[tab]()

# ===== CALLBACKS =====

# == POSTCODE ==
@app.callback(
    Output("postcode-total-string", "children"),
    Input("postcode_selector", "value")
)
def return_postcode_total(postcode):
    return Postcode.number_postcode_total(postcode=postcode, callback_mode=True)

@app.callback(
    Output("postcode_overtime", "figure"),
    Input("postcode_selector", "value")
)
def return_line_postcode_overtime(postcode):
    return Postcode.line_postcode_overtime(postcode=postcode, callback_mode=True)

@app.callback(
    Output("postcode_overtime_cumsum", "figure"),
    Input("postcode_selector", "value")
)
def return_line_postcode_overtime_cumsum(postcode):
    return Postcode.line_postcode_overtime_cumsum(postcode=postcode, callback_mode=True)

# == Postcode ==

# ===== Callbacks =====

if __name__ == '__main__':
    data.update(type=None)
    app.run_server(debug=True, host='0.0.0.0', port=8080)
