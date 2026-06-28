
import streamlit as st
import pandas as pd
import sqlalchemy


engine = sqlalchemy.create_engine('sqlite:///database.db')

# Título da página
st.set_page_config(page_title="Lista Inteligente")

# Sub-título da página
st.markdown("# Sua lista de compras inteligente!")
st.markdown("## Importar Histórico de Compras")

# Importar arquivo CSV
abrir_arquivo = st.file_uploader("Entre com um arquivo de histórico de compras", type="csv")

if abrir_arquivo:
    df = pd.read_csv(abrir_arquivo)
    st.data_editor(df)
    
    if st.button("Registrar Dados"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")
    

