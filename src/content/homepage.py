from dash import html

class Homepage:

    _title = html.Div(
        id="tab0-title",
        children=html.P(
            "Heading for Tab0: Homepage"
        )
    )
    def __init__(self):
        pass

    @classmethod
    def build_child(cls):
        return [
            cls._title
        ]