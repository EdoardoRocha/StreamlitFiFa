import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.markdown("# FIFA2023 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [EDOARDO ROCHA PAZ](https://instagram.com/@edoardopazz)")
btn = st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
        O conjunto de dados...
    """
)