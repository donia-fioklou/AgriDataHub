import streamlit as st
import pandas as pd
from controllers.formulaire_controller import TauxRemplissage
from Generale import GeneraleOpertaion


def form_operation(df):
    nombre_formulaires=TauxRemplissage(df).nombre_form()
    st.markdown(f"### Vous avez importé un fichier contenant {nombre_formulaires} formulaires.")
    forms=TauxRemplissage(df).liste_form()
    forms_taux_remplissage=TauxRemplissage(df).taux_remplissage()

    for i in range(len(forms)):
        st.markdown(f"### Formulaire {i+1}")
        st.dataframe(forms[i])
        st.markdown(f"### Taux de remplissage du formulaire {i+1} : {round(forms_taux_remplissage[i],2)}%")

df=st.session_state.df
if df is not None:
    form_operation(df)
else:
    df=st.file_uploader(label="uploader un ficher",type=['xlsx'])
    form_operation(df)

if "df1" not in st.session_state:
    st.session_state.df1 = df
   
