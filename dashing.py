from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.io as pio
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# print(pio.templates)
df = pd.read_csv("precious_metals_prices_2018_2021.csv")
columns = df.columns.values.tolist()
# print(columns)
col_name = columns.pop(0)

app = Dash(__name__)
server=app.server
app.layout = html.Div(id="container-id", children=[
    html.H1("Graph Interface with Dropdown"),
    html.P("Graph with Metal"),
    dcc.Dropdown(options=[
        {"label": metal, "value": metal} for metal in columns
    ], id="dropdown",value="Gold"),
    dcc.Graph(id='graph-court')
])


@app.callback(
    Output('graph-court', 'figure'),
    Input('dropdown', 'value'))
def update_picture(value):
    print(value)
    data = px.line(df, x="DateTime", y=value)
    fig = go.Figure(data=data)
    fig.update_layout(template="plotly_dark")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
