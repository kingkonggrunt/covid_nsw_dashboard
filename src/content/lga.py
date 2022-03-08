from dash import dcc
from dash import html
from src.data import CovidData
from src.processing import processing
from src.graph import GraphBuilder as GB

CovidData = CovidData()

class LGA:
    """Content for LGA graphs"""
    
    _title = html.P("Cases by LGA")
    
    def __init__(self):
        pass

    @staticmethod
    def dropdown_lga():
        """Dropdown to select LGA"""
        df = CovidData.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        _dcc = dcc.Dropdown(
            id="lga_selector",
            options=[
                {"label": lga, "value": lga} for lga in sorted(df['lga_name19'].unique().astype(str))
            ], # nan values are typed as integers couldn't be sorted with strings
            value="Sydney (C)"
        )

        return _dcc

    @staticmethod
    def number_lga_total(lga='Sydney', callback_mode=False):
        """Return total number for cases for an lga"""
        df = CovidData.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        lga_totals = processing.value_counts_to_df(df, "lga_name19", "count")
        total = lga_totals.loc[lga]['count']

        if callback_mode:
            return f'Total for {lga}: {total}'

        return html.Div(
            id='postcode-total-string',
            children=f'Total for {lga}: {total}'
        )

    @classmethod
    def build_child(cls):
        """Builds the html child (interactive elements"""
        return [
            html.Div(
                id="tabs_cases_lga",
                children=[
                    cls._title,
                    cls.dropdown_lga(),
                ]
            )
        ]