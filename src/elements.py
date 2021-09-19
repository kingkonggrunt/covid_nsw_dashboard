from dash import dcc
from dash import html

from src import assets

class Banner:
    def __init__(self):
        pass

    def build(self):
        return html.Div(
            id="banner",
            className="banner",
            children=[
                self._title,
                self._button
            ]
        )

    @property
    def _title(self):
        return html.Div(
            id="banner-title",
            children=[
                html.H5("COVID NSW DASHBOARD"),
                html.H6("by DCC")
            ]
        )

    @property
    def _button(self):
        return html.Div(
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
