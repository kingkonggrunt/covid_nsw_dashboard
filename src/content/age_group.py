from dash import html

from src.graph import GraphBuilder as GB
from src import processing
from src.data import CovidData

CovidData = CovidData()

class AgeGroup:
    """
    Renders Graphs related to the Age Group Data. Only supports
    rendering all at once (in one location)
    """

    _title = html.H3("Age Group Data")
    _paragraph = html.P("Age Group Data was tracked from the 29 June 2021 onwards")

    def __init__(self):
        pass

    @staticmethod
    def bar_total():
        """Bar graph for display age group totals"""
        df = CovidData.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.value_counts_to_df(df, "age_group", "cases")

        df.sort_index(ascending=True, inplace=True)
        df.reset_index(inplace=True)

        df['age_group'] = df['age_group'].apply(lambda x: x.replace("AgeGroup_", ""))

        graph = GB(id="age_group_total")
        graph.figure("bar", df,
            x="age_group", y="cases", title="Total Cases by Age Group"
        )
        return graph.build()

    @staticmethod
    def bar_total_normalize():
        """Pie chart of total cases by age group"""
        df = CovidData.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
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
    
    @staticmethod
    def line_group_overtime():
        """Line graph for cases overtime"""
        df = CovidData.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.sort_column_value_counts_by_group(df, 'notification_date', 'age_group')

        df.rename(columns={x: x.replace("AgeGroup_", "") for x in df.columns}, inplace=True)
        df.rename_axis(index="Notification Date",columns="Age Groups", inplace=True)

        graph = GB("age_group_overtime")
        graph.figure("line", df,
            x=df.index, y=df.columns, title="Cases Overtime (Age Group)"
        )
        return graph.build()
    
    @staticmethod
    def line_group_overtime_cumsum():
        """Cumulative sum of cases for each age group."""
        df = CovidData.load_csv("Cases (Age Range).csv", parse_dates=['notification_date'])
        df = processing.sort_column_value_counts_by_group(df, 'notification_date', 'age_group')
        df = df.cumsum()

        df.rename(columns={x: x.replace("AgeGroup_", "") for x in df.columns}, inplace=True)
        df.rename_axis(index="Notification Date",columns="Age Groups", inplace=True)

        graph = GB(id="age_group_overtime_cumsum")
        graph.figure("line", df,
            x=df.index, y=df.columns, title="Cases Overtime (Age Group) Cumulative"
        )
        return graph.build()
    
    @classmethod
    def build_child(cls):
        """Build html child (interactive elements)"""
        return [
            html.Div(
                id="tab1",
                children=[
                    cls._title,
                    cls._paragraph,
                    cls.bar_total(),
                    cls.bar_total_normalize(),
                    cls.line_group_overtime(),
                    cls.line_group_overtime_cumsum()
                ]
            )
        ]