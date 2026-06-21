from dash import html, dcc, Output, Input, Dash
import dash_bootstrap_components as dbc
from app_layout import create_app_layout
from callback import app_callback_functions
# Instantiate an app
app = Dash(__name__, assets_folder="web_style", external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title="Causes of Deaths Dashboard"

# Build the app layout
app.layout = create_app_layout()

# Callback functions
app_callback_functions(app)
if __name__ == "__main__":
    app.run(debug=True, port=8051)