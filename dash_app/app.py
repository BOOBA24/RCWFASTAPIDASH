import dash
from dash import html, dcc, Output, Input
import requests

# App Dash
app = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')
server = app.server

# Layout
app.layout = html.Div([
    html.Div([
        html.A('Accueil', href='/'),
        " | ",
        html.A("Logout", href="/logout")
    ], style={'marginTop': 25, 'marginBottom': 20}),

    html.Div(id='weather-info'),  # Bloc météo vide au départ

    dcc.Interval(id='interval-weather', interval=30 * 1000, n_intervals=0),  # 30 sec

    html.H1("Example de Dashboard"),

    html.H2("*** Bar Graph *** "),
    dcc.Graph(
        id="exm1",
        figure={
            "data": [
                {"x": [5, 7, 12], "y": [10, 16, 11], "type": "bar", "name": "exmple1"},
                {"x": [8, 18, 22], "y": [5, 8, 3], "type": "bar", "name": "exmple2"}
            ]
        }
    ),

    html.H2("*** Line Graph *** "),
    dcc.Graph(
        id="exm2",
        figure={
            "data": [
                {"x": [1, 3, 5], "y": [10, 12, 14], "type": "line", "name": "exmple3"},
                {"x": [2, 4, 6], "y": [13, 15, 17], "type": "line", "name": "exmple4"}
            ]
        }
    ),

    html.H2("*** Scatter Plot Graph *** "),
    dcc.Graph(
        id="exm3",
        figure={
            "data": [
                {"x": [1, 3, 5, 7], "y": [10, 12, 14, 16], "type": "scatter", "mode": "markers", "name": "scatter exmpl1"},
                {"x": [2, 4, 6, 8], "y": [13, 15, 17, 19], "type": "scatter", "mode": "markers", "name": "scatter exmpl2"}
            ]
        }
    ),

    html.H2("*** Pie Chart Graph *** "),
    dcc.Graph(
        id="exm4",
        figure={
            "data": [
                {"labels": ["A", "B", "C"], "values": [10, 12, 14], "type": "pie", "name": "pie chart expl1"},
            ],
            "layout": {"title": "pie chart example"}
        }
    ),
])

# Callback météo dynamique
@app.callback(
    Output("weather-info", "children"),
    Input("interval-weather", "n_intervals")
)
def update_weather(n):
    try:
        response = requests.get("https://watherapi-hdcgfeakfwd9frcy.canadacentral-01.azurewebsites.net/info", timeout=5)
        data = response.json()
        return html.Div([
            html.H2("🌤️ Météo Actuelle"),
            html.P(f"Ville : {data['weather']['city']}"),
            html.P(f"Température : {data['weather']['temperature']} °C"),
            html.P(f"Dernière mise à jour : {data['date']} à {data['time']}")
        ], style={
            'border': '2px solid #ccc',
            'padding': '10px',
            'marginBottom': '30px',
            'backgroundColor': '#f5f5f5',
            'borderRadius': '8px'
        })
    except Exception as e:
        return html.Div([
            html.H2("🌤️ Météo Actuelle"),
            html.P("Erreur de récupération des données météo."),
            html.P(str(e))
        ], style={
            'border': '2px solid red',
            'padding': '10px',
            'marginBottom': '30px',
            'backgroundColor': '#ffe5e5',
            'borderRadius': '8px'
        })
