

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from controllers.generale_controller import Generale, GrapheProducteur, GrapheSexe
from pages.analyse_de_fichier import decoupage

st.markdown("### Importer un fichier ")

upload_file=st.file_uploader(label="uploader un ficher",type=['xlsx'])


#nettoyage des données
def nettoyage(df):
    df = df.drop_duplicates(subset=['Code Surface'],keep='last')
    df[['Quantité vendu en 2021(en Tonne)','Age de la plantation','Nombre de plants']]=df[['Quantité vendu en 2021(en Tonne)','Age de la plantation','Nombre de plants']].fillna(0)
    df[['Quantité vendu en 2021(en Tonne)','Age de la plantation','Nombre de plants']]=df[['Quantité vendu en 2021(en Tonne)','Age de la plantation','Nombre de plants']].replace(to_replace='.*', value=0, regex=True)

if upload_file:
    df=pd.read_excel(upload_file)
    
    select_zone=st.sidebar.selectbox(label="sélectionner une zone",options=Generale.liste_zone(df))
    select_cooperative=st.sidebar.selectbox(label="sélectionner une coopérative",options=Generale.liste_cooperative(df,select_zone))
    
    graphe_sexe = GrapheSexe(df)
    st.markdown("### Répartition démographique par sexe dans la zone "+select_zone)
    chart_sexe = graphe_sexe.graph_sexe(select_zone,select_cooperative)
    
    graphe_producteur= GrapheProducteur(df)
    st.markdown("### Répartition des producteurs par zone dans la coopérative "+select_cooperative) 
    chart_producteur=graphe_producteur.graph_producteur_zone(select_cooperative) 
    st.dataframe(df)