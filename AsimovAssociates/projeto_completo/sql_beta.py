import sqlite3
import pandas as pd

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('sistema.db')
    c = conn.cursor()

    # Criando a tabela de processos
    c.execute("""CREATE TABLE IF NOT EXISTS processos (
                'No Processo' INTEGER PRIMARY KEY,
                Empresa TEXT,
                Tipo TEXT,
                Ação TEXT,
                'Data Inicial' TEXT,
                'Data Final' TEXT,
                'Processo Concluído' INTEGER,
                'Processo Vencido' INTEGER,
                Advogados TEXT,
                Cliente TEXT,
                'Descrição' TEXT)""")

    # Recriando a tabela de advogados apenas com a coluna 'Advogado'
    c.execute("DROP TABLE IF EXISTS advogados")
    c.execute("""CREATE TABLE advogados (
                Advogado TEXT)""")

    conn.commit()
    conn.close()

# Inicializando o banco de dados
init_db()

# Carregando os dados do banco de dados usando pandas
def load_data():
    conn = sqlite3.connect('sistema.db')
    df_adv = pd.read_sql("SELECT * FROM advogados", conn)
    df_proc = pd.read_sql("SELECT * FROM processos", conn)
    conn.close()
    return df_adv, df_proc

df_adv, df_proc = load_data()