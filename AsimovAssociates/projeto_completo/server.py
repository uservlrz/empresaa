from app import server, app
from components import sidebar

app.layout = sidebar.layout

# Importar callbacks
from components import homeC
from components import advogadoC
from components import novoAdvogado
from components import novoProcesso
from components import sidebarC

if __name__ == "__main__":
    app.run_server(debug=True)
