# Import libraries
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
avocado = pd.read_csv('avocado-updated-2020.csv')

# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=avocado['geography'].unique(),
                            value='New York')

app.layout = html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    geo_dropdown,
    dcc.Graph(id='pie-graph'),
    dcc.Graph(id='histogram-graph')
])


# Set up the callback function for pie graph
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_pie_graph(selected_geography):
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    pie_fig = px.pie(filtered_avocado,
                     names='type',
                     values='total_volume',
                     title=f'Avocado Distribution by Type in {selected_geography}')
    return pie_fig


# Set up the callback function for histogram graph
@app.callback(
    Output(component_id='histogram-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_histogram_graph(selected_geography):
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    hist_fig = px.histogram(filtered_avocado,
                            x='date', y='total_bags',
                            color='small_bags',
                            title=f'Avocado Prices in {selected_geography}')
    return hist_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
