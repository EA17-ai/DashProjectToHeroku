from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.io as pio

#print(pio.templates)

df = pd.read_csv("D://DashVisualizations\data-vis-python-dash-3009706/02_03/precious_metals_prices_2018_2021.csv",
                 usecols=["DateTime", "Platinum", "Gold", "Silver", "Palladium", "Rhodium", "Iridium", "Ruthenium"])
fig = px.line(df, x="DateTime", y=["Platinum", "Gold", "Silver", "Palladium", "Rhodium", "Iridium", "Ruthenium"],
              title="Metals over years")

#fig.update_layout(template="plotly_dark")

app = Dash(__name__)

app.layout = html.Div(id="app-container",
                      children=[
                          html.H1("Precious Price Metal Data"),
                          html.P("Results"),
                          dcc.Graph(figure=fig)
                      ])

if __name__ == "__main__":
    app.run_server(debug=True)
