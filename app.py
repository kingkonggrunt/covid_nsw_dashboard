import os

import dash
from dash import dcc
from dash import html

from src import assets

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# ===== Banner is the header of the Dashboard
def build_banner():
    title = html.Div(
        id="banner-title",
        children=[
            html.H5("COVID NSW DASHBOARD"),
            html.H6("by DCC")
        ]
    )

    buttons = html.Div(
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
    return html.Div(
        id="banner",
        className="banner",
        children=[
            title,
            buttons
        ]
    )

app.layout = html.Div(
    id="covid_nsw_dashboard",
    children=[
        build_banner(),
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
