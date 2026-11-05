
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
df = pd.read_csv("dataset_part_2.csv")
app = Dash(__name__)
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Launch Dashboard"),
    dcc.Graph(figure=px.pie(df, names="Class", title="Launch Success Distribution")),
    dcc.Graph(figure=px.scatter(df, x="PayloadMass", y="Class", color="LaunchSite",
                                hover_data=["FlightNumber"], title="Payload vs Landing Outcome")),
    dcc.Graph(figure=px.bar(df.groupby("LaunchSite", as_index=False).size(),
                            x="LaunchSite", y="size", title="Launches by Site"))
])
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
