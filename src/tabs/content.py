from dash import dcc
from dash import html

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

        self._title = html.Div(
            id="tab1",
            children=html.P(
                "Heading for Tab1: Something"
            )
        )

    def build_child(self):
        return [
            self._title
        ]

class TabActiveRoutes:
    def __init__(self):

        self._title = html.Div(
            id="tab1",
            children=html.P(
                "Active Flight and Public Transport Routes"
            )
        )

    def build_child(self):
        return [
            self._title
        ]
