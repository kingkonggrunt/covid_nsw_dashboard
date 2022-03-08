from dash import html
from dash import dcc
from src.data import CovidData
from src.graph import GraphBuilder as GB
from  src.processing import processing

CovidData = CovidData()


class Postcode():
    """Content class for postcode related data"""
    _title = html.H3("Cases by Postcode")
    
    def __init__(self):
        pass
        # CovidData = CovidData()

    @staticmethod
    def dropdown_postcode():
        """Interactive dropdown to select postcode"""
        df = CovidData.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        _dcc = dcc.Dropdown(
            id="postcode_selector",
            options=[
                {"label": postcode, "value": postcode} for postcode in sorted(df['postcode'].unique())
            ],
            value="2000"
        )

        return _dcc

    @staticmethod
    def number_postcode_total(postcode='2000', callback_mode=False):
        """Total cases for a postcode"""
        df = CovidData.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        _postcode_totals = processing.value_counts_to_df(df, "postcode", "count")
        total = _postcode_totals.loc[postcode]['count']


        if callback_mode:
            return f'Total for {postcode}: {total}'

        return html.Div(
            id='postcode-total-string',
            children=f'Total for {postcode}: {total}'
        )

    @staticmethod
    def line_postcode_overtime(postcode='2000', callback_mode=False):
        """Cases overtime for a postcode"""
        df = CovidData.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        df = processing.sort_column_value_counts_by_group(df, 'notification_date', 'postcode')
        graph = GB("postcode_overtime")
        graph.figure("line", df[postcode])

        if callback_mode:
            return graph.return_figure()

        return graph.build()

    @staticmethod
    def line_postcode_overtime_cumsum(postcode='2000', callback_mode=False):
        """Cumsum of cases for a postcode"""
        df = CovidData.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        df = processing.sort_column_value_counts_by_group(df, 'notification_date', 'postcode')
        df = df.cumsum()

        graph = GB(id="postcode_overtime_cumsum")
        graph.figure("line", df[postcode])

        if callback_mode:
            return graph.return_figure()

        return graph.build()

    @classmethod
    def build_child(cls):
        """Builds the html child (interactive elements)"""
        return [
            html.Div(
                id="tab_cases_postcode",
                children=[
                    cls._title,
                    cls.dropdown_postcode(),
                    cls.number_postcode_total(),
                    cls.line_postcode_overtime(),
                    cls.line_postcode_overtime_cumsum(),
                ]
            )
        ]