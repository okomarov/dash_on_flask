import dash_core_components as dcc
import dash_html_components as html

from .get_data import save_sp500_stocks_info, save_self_stocks_info

layout = html.Div([
    html.H1('Value Investing'),
        # First let users choose stocks
    html.H2('Choose a stock ticker'),
    dcc.Dropdown(
        id='my-dropdown',
        options=save_sp500_stocks_info()+save_self_stocks_info(),
        value='coke'
    ),
    html.H2('5 years stocks price graph'),
    dcc.Graph(id='my-graph'),
    html.P('')
], style={'width': '50%', 'margin-left': '25%'})
