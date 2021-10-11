from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px

from src.data import CovidData
from src.pandas import processing

from src.graph.GraphBuilder import GraphBuilder as GB


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

        self._data = CovidData()
        self._title = html.H3("Age Groups Data")
        self._paragraph = html.P("Age Group Data was tracked from the 29 June 2021 onwards")

    # ===== Graph Building
    def _bar_total(self):
        df = self._data.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.value_counts_to_df(df, "age_group", "cases")

        df.sort_index(ascending=True, inplace=True)
        df.reset_index(inplace=True)

        df['age_group'] = df['age_group'].apply(lambda x: x.replace("AgeGroup_", ""))

        graph = GB(id="age_group_total")
        graph.figure("bar", df,
            x="age_group", y="cases", title="Total Cases by Age Group"
        )
        return graph.build()

    def _bar_total_normalize(self):
        df = self._data.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.value_counts_to_df(df, "age_group", "percent", normalize=True)

        df.sort_index(ascending=True, inplace=True)
        df.reset_index(inplace=True)

        df['percent'] = df['percent'].apply(lambda x: x*100)
        df['age_group'] = df['age_group'].apply(lambda x: x.replace("AgeGroup_", ""))

        graph = GB("age_group_total_normalize")
        graph.figure("pie", df,
            names="age_group", values="percent", title="Total Cases by Age Group"
        )
        graph.update_traces(textposition="inside", textinfo="percent+label")
        return graph.build()

    def _line_group_overtime(self):
        df = self._data.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.sort_column_value_counts_by_group(df, 'notification_date', 'age_group')

        df.rename(columns={x: x.replace("AgeGroup_", "") for x in df.columns}, inplace=True)
        df.rename_axis(index="Notification Date",columns="Age Groups", inplace=True)

        graph = GB("age_group_overtime")
        graph.figure("line", df,
            x=df.index, y=df.columns, title="Cases Overtime (Age Group)"
        )
        return graph.build()

    def _line_group_overtime_cumsum(self):
        df = self._data.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.sort_column_value_counts_by_group(df, 'notification_date', 'age_group')
        df = df.cumsum()

        df.rename(columns={x: x.replace("AgeGroup_", "") for x in df.columns}, inplace=True)
        df.rename_axis(index="Notification Date",columns="Age Groups", inplace=True)

        graph = GB(id="age_group_overtime_cumsum")
        graph.figure("line", df,
            x=df.index, y=df.columns, title="Cases Overtime (Age Group) Cumulative"
        )
        return graph.build()

    def build_child(self):
        return [
            html.Div(
                id="tab1",
                children=[
                    self._title,
                    self._paragraph,
                    self._bar_total(),
                    self._bar_total_normalize(),
                    self._line_group_overtime(),
                    self._line_group_overtime_cumsum()
                ]
            )
        ]


class TabCasesPostCode():
    def __init__(self):

        self._data = CovidData()
        self._title = html.H3("Cases by Postcode")

    def _dropdown_postcode(self):
        df = self._data.load_csv("Cases (Location).csv", parse_dates=['notification_date'])
        _dcc = dcc.Dropdown(
            id="postcode_selector",
            options=[
                {"label": postcode, "value": postcode} for postcode in sorted(df['postcode'].unique())
            ],
            value="2000"
        )

        return _dcc

    def _number_postcode_total(self):
        out = html.Div(
            id='postcode-total-string',
            children='Test string that should dissapear with callbacks working'
        )

        # @app.callback(
        #     Output("postcode-total-string", "children"),
        #     Input("postcode_selector", "value")
        # )
        # def _return_postcode_total(postcode):
        #     total = _postcode_totals.loc[postcode]['count']
        #     return f"Total for {postcode}: {total}"

        return out

    def build_child(self):
        return [
            html.Div(
                id="tab_cases_postcode",
                children=[
                    self._title,
                    self._dropdown_postcode(),
                    self._number_postcode_total(),
                ]
            )
        ]


class TabActiveRoutes:
    def __init__(self):

        self._data = CovidData()
        self._title = html.P("Active Flight and Public Transport Routes")

    # ===== This is the hard coded stuff for the generation of relavent data
    def _data_table_flight(self):
        df = self._data.load_csv("Case Flights.csv")
        table = dash_table.DataTable(
            id='flights_table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records')
        )
        return table

    def _data_table_public_transport(self):
        df = self._data.load_csv("Case Public Transport Routes.csv")
        table = dash_table.DataTable(
            id='public_transport_table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records')
        )
        return table
    # =====

    def build_child(self):
        return [
            html.Div(
            id="tab_active_routes_children",
            children=[
                self._title,
                html.P("Active Flight Routes"),
                self._data_table_flight(),
                html.P("Active Public Transport Routes"),
                self._data_table_public_transport()
            ]
            )
            #self._build_public_transport_data_table()
        ]
