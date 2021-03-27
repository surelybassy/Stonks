# Import Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas_datareader as web
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

todays_date = datetime.today().strftime('%Y-%m-%d')

# Pull in Data
aapl = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end=todays_date)
amc = web.DataReader('AMC', data_source='yahoo', start='2012-01-01', end=todays_date)
TSLA = web.DataReader('TSLA', data_source='yahoo', start='2012-01-01', end=todays_date)

appl_close = aapl['Close'].to_frame().reset_index()
amc_close = amc['Close'].to_frame().reset_index()
tsla_close = TSLA['Close'].to_frame().reset_index()

apple_latest = round(appl_close.iloc[[-1]]['Close'],4)
amc_latest = round(amc_close.iloc[[-1]]['Close'],4)
tsla_latest = round(tsla_close.iloc[[-1]]['Close'],4)


tsla_percentchange = TSLA['Close'].pct_change().to_frame().reset_index()

# Build Graphs
fig = go.Figure([go.Scatter(x=appl_close['Date'], y=appl_close['Close'], line=dict(color="#53354a"))])
fig2 = go.Figure([go.Scatter(x=amc_close['Date'], y=amc_close['Close'], line=dict(color="#2b2e4a"))])
fig3 = go.Figure([go.Scatter(x=tsla_close['Date'], y=tsla_close['Close'], line=dict(color="#903749"))])
fig4 = go.Figure([go.Scatter(x=tsla_percentchange['Date'], y=tsla_percentchange['Close'], line=dict(color="#903749"))])

fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
fig2.update_layout(margin=dict(l=0, r=0, t=0, b=0))
fig3.update_layout(margin=dict(l=0, r=0, t=0, b=0))
fig4.update_layout(margin=dict(l=0, r=0, t=0, b=0))

# App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Stock Market Tracker Prototype', className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.Div(className="grid-container", children=[
                html.Div(className="kpibox KPI1", children=[
                    html.H2('Apple Last Close'),html.H3(apple_latest, className="stockprice")]),
                html.Div(className="kpibox KPI2", children=[
                    html.H2('AMC Last Close'),html.H3(amc_latest, className="stockprice")]),
                html.Div(className="kpibox KPI3", children=[
                    html.H2('Tesla Last Close'),html.H3(tsla_latest, className="stockprice")]),


                html.Div(className="featurebox Graph1", children=[
                    html.H1('Apple Stock - Close Price'),
                    html.Div([
                        dcc.Graph(
                    id='apple-graph',
                    figure=fig)])
                    ]),
                html.Div(className="featurebox Graph2", children=[
                    html.H1('AMC Stock - Close Price'),
                    html.Div([
                        dcc.Graph(
                    id='amc-graph',
                    figure=fig2)])
                    ]),

                html.Div(className="featurebox Graph3", children=[
                    html.H1('Tesla Stock - Close Price'),
                    html.Div([
                        dcc.Graph(
                    id='tesla-graph',
                    figure=fig3)])
                    ]),
                html.Div(className="featurebox Graph4", children=[
                    html.H1('Tesla Stock - Percentage Change'),
                    html.Div([
                        dcc.Graph(
                    id='tesla-percent-graph',
                    figure=fig4)])
                    ]),
            ])
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
