from dash import dcc
from dash import html
import plotly.express as px

from src.graph.figures import figures

class GraphBuilder:
    def __init__(self, id=""):
        self._id = id
        self._fig = None

    def figure(self, figure, df, **kwargs):
        self._fig = figures[figure](df, **kwargs)

    def update_traces(self, **kwargs):
        self._fig.update_trace(**kwargs)

    def build(self):
        return dcc.Graph(
            id=self._id,
            figure=self._fig
        )
