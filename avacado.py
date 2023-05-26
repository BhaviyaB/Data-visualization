import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("avocado.csv")
    .query("type == 'conventional' and geography == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["date"], format="%Y-%m-%d"))
    .sort_values(by="date")
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics"),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["average_price"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["total_volume"],
                        "type": "line",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)