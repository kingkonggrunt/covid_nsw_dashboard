from dash import dcc
from dash import html
import plotly.express as px

from src.graph.figures import figures

class GraphBuilder:
    """
    ## GraphBuilder

    Wrapper for the construction of plotly express figures into dcc.Graph
    dash_core_components

    `id` : css id for the Graph dash_core_components

    .figure(figure, df, **kwargs)
        `figure` : plotly express figure
        `df` : pandas DataFrame
        `**kwargs` : key word arguments that are passed into the px.figure

    """
    def __init__(self, id=""):
        self._id = id
        self._fig = None

    def figure(self, figure, df, **kwargs):
        self._fig = figures[figure](df, **kwargs)


    def update_traces(self, **kwargs):
        self._fig.update_traces(**kwargs)

    def return_figure(self):
        return self._fig

    def build(self):
        return dcc.Graph(
            id=self._id,
            figure=self._fig
        )
