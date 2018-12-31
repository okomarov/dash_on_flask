from datetime import datetime as dt

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader as pdr

from app import create_app

app, dashapp = create_app()


dashapp.layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
])


@dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }]
    }

