import dash
import dash_bootstrap_components as dbc
from flask import Flask

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", dbc.themes.LUX]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=estilos + [dbc_css])

app.config.suppress_callback_exceptions = True
app.scripts.config.serve_locally = True
