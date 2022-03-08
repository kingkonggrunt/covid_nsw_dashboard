from dash import dcc
from dash import html

from src.content import Homepage, AgeGroup, LGA, Postcode

class TabButtons:
    """class that managers the rendering of the tab buttons across the page"""

    _tabs = [
            dcc.Tab(
                id="Homepage",
                label="Homepage",
                value="tab_home",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"
            ),
            dcc.Tab(
                id="Case Locations",
                label="Cases (Age Group)",
                value="tab_age_group",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected",
            ),
            dcc.Tab(
                id="Postcode",
                label="Cases (Postcode)",
                value="tab_cases_postcode",
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"
            ),
            dcc.Tab(
                id="LGA",
                label="Cases (LGA)",
                value='tab_cases_lga',
                className="dashboard-tabs",
                selected_className="dashboard-tabs--selected"
            ),
            # dcc.Tab(
            #     id="Active Flight and Public Transport Routes",
            #     label='Active Flight/Public Transport Routes',
            #     value="tab_active_routes",
            #     className="dashboard-tabs",
            #     selected_className="dashboard-tabs--selected"
            # )
        ]

    def __init__(self):
        pass
    
    @staticmethod
    def tab_button_to_tab_content():
        """Links table values with their content classes"""
        return {
            "tab_home":Homepage.build_child,
            "tab_age_group": AgeGroup.build_child,
            "tab_cases_postcode":Postcode.build_child,
            "tab_cases_lga":LGA.build_child,
            # "tab_active_routes":tab_active_routes.build_child,
    }

    @classmethod
    def build(cls):
        """renders the tab buttons that run across the dashboard"""
        return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
            id="dashboard-tabs",
            value="tab_home",
            className="dashboard-tabs",
            children=cls._tabs
            )
        ]
        )
