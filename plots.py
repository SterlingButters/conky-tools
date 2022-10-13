import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_rangeslider_visible=False,
    width=1000,
    height=1000
)

fig.update_xaxes(
    range=(datetime(year=2016, month=10, day=1) - timedelta(days=20), datetime(year=2016, month=10, day=1)),
    constrain='domain'
)

fig.write_image('fig.png') # or svg