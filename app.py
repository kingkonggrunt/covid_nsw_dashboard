import os

import dash
from dash import dcc
from dash import html

from src import assets
from src import elements

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# ===== Banner is the header of the Dashboard
banner = elements.Banner()

app.layout = html.Div(
    id="covid_nsw_dashboard",
    children=[
    banner.build()
    ]
)


# app.layout = html.Div([
#     html.H2('Hello HAN!'),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
#         value='LA'
#     ),
#     html.Div(id='display-value')
# ])
#
# @app.callback(dash.dependencies.Output('display-value', 'children'),
#               [dash.dependencies.Input('dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
