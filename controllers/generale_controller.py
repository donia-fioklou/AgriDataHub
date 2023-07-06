
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pages.analyse_de_fichier import decoupage

class Generale():
    #liste des zones 
    def liste_zone(df):
        liste_zone=df['Zone'].unique()
        liste_zone = np.insert(liste_zone, 0, "Tous")
        return liste_zone
    #liste de cooperative
    def liste_cooperative(df,zone):
        df=df.loc[df['Zone']==zone]
        liste_cooperative=df['Union'].unique()
        liste_cooperative = np.insert(liste_cooperative, 0, "Tous")
        return liste_cooperative

# Graphe pour la répartition par sexe
class GrapheSexe():
    def __init__(self,df):
        self.df=df
    #graphique pour le sexe
    def graph_sexe(self,zone,union):
        forms=decoupage(self.df)
        df=forms[0]
        df=df.drop_duplicates(subset=['code'],keep='last')
        if zone=="Tous" and union=="Tous":
            df=df.groupby('Sexe').size().reset_index()
        elif zone=="Tous" and union!="Tous":
            df=df.loc[df['Union']==union]
            df=df.groupby('Sexe').size().reset_index()
        elif zone!="Tous" and union=="Tous":
            df=df.loc[df['Zone']==zone]
            df=df.groupby('Sexe').size().reset_index()
        else:
            df=df.loc[df['Zone']==zone]
            df=df.loc[df['Union']==union]
            df=df.groupby('Sexe').size().reset_index()
        
        
        df.columns=['Sexe','Nombre']
        sexe=df['Sexe']
        nombre=df['Nombre']
        bar_colors=['tab:red','tab:blue']
        fig, ax = plt.subplots()
        ax.bar(height=nombre, x=sexe,color=bar_colors)
        
        chart_sexe=st.pyplot(fig)
        
        return chart_sexe
#graphe pour la repartition des producteurs par zone    
class GrapheProducteur():
    def __init__(self,df):
        self.df=df
    
    #nombre de producteur par zone
    def graph_producteur_zone(self,union):
        forms=decoupage(self.df)
        df=forms[0]
        df=df.drop_duplicates(subset=['code'],keep='last')
        if union=="Tous":
            df=df.groupby('Zone').size().reset_index()
        else:
            df=df.loc[df['Union']==union]
            df=df.groupby('Zone').size().reset_index()
        df.columns=['Zone','nombre']
        df.sort_values('nombre',ascending=False,inplace=True)
        nombre=df['nombre']
        zone=df['Zone']
        
        fig, ax = plt.subplots()
        ax.bar(height=nombre, x=zone)
        ax.tick_params(axis='x', rotation=45)
        
        chart_zone=st.pyplot(fig)
        return chart_zone,df
     


    