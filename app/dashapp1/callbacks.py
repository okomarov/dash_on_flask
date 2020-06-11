from datetime import datetime as dt
from pandas_datareader import data as web
from dash.dependencies import Input
from dash.dependencies import Output

# Set up global variables
stockpricedf = 0

def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        global stockpricedf # Needed to modify global copy of stockpricedf
        stockpricedf = web.DataReader(
            selected_dropdown_value.strip(), data_source='yahoo',
            start=dt(2013, 1, 1), end=dt.now())
        return {
            'data': [{
                'x': stockpricedf.index,
                'y': stockpricedf.Close
            }]
        }
