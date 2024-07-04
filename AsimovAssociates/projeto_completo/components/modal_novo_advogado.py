import dash
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

from app import app

# ========= Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Adicione Um Usuario")),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label("Nome"),
                dbc.Input(id="adv_nome", placeholder="Nome completo do advogado...", type="text")
            ]),
        ]),
        html.H5(id='div_erro2')
    ]),
    dbc.ModalFooter([
        dbc.Button("Cancelar", id="cancel_button_novo_advogado", color="danger"),
        dbc.Button("Salvar", id="save_button_novo_advogado", color="success")
    ])
], id="modal_new_lawyer", size="lg", is_open=False)

app.layout = html.Div([
    layout,
    dcc.Store(id='store_adv', data=[]),  # Initialize the store with an empty list
])

# ======= Callbacks ======== #
@app.callback(
    Output('store_adv', 'data'),
    Output('div_erro2', 'children'),
    Output('div_erro2', 'style'),
    Input('save_button_novo_advogado', 'n_clicks'),
    State('store_adv', 'data'),
    State('adv_nome', 'value'),
)
def novo_adv(n, dataset, nome):
    erro = []
    style = {}
    
    if n:
        if not nome:  # Check if nome is None or empty
            return dataset, ["Todos dados são obrigatórios para registro!"], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
        df_adv = pd.DataFrame(dataset)

        if not df_adv.empty and nome in df_adv['Advogado'].values:
            return dataset, [f"Nome {nome} ja existe no sistema!"], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
        new_entry = pd.DataFrame([[nome]], columns=['Advogado'])
        df_adv = pd.concat([df_adv, new_entry], ignore_index=True)
        dataset = df_adv.to_dict('records')
        return dataset, ["Cadastro realizado com sucesso!"], {'margin-bottom': '15px', 'color': 'green', 'text-shadow': '2px 2px 8px #000000'}
    
    return dataset, erro, style