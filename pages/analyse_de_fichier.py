import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt





# decoupage du dataframe apres chaque colonne Fin

def delete_additionnel_col(df):
    cols_to_delete = ['Formulaire', 'Type formualaire', 'Unnamed']
    cols_to_drop = [col for col in df.columns if any(keyword in col for keyword in cols_to_delete)]
    df.drop(cols_to_drop, axis=1, inplace=True)
    return df

    
    
def decoupage(df):
    df=delete_additionnel_col(df)
    forms=[]
    col_name=[]
    
    for col in df.columns:
        col_name.append(col)
        if 'Fin'in col:
            forms.append(df.loc[:,col_name])
            col_name=[]
    return forms

#liste de form concatener avec l'id
def concat_id(df):
    forms=decoupage(df)
    forms_with_id=[]
    for form in forms:  
        if not form.equals(forms[0]):     
            forms_with_id.append(pd.concat([forms[0],form],axis=1))
    return forms_with_id

#analyse des incoherences
def analyse_incoherence(form):
    resultat=[]
    for row in form.itterows():
        colonne_non_remplis=[]
        nombre_de_col_non_remplis=0
        for col in form.columns:
            if row[col]=='':
                nombre_de_col_non_remplis+=1
                colonne_non_remplis.append(col)
        resultat.append({'nombre_de_col_non_remplis': nombre_de_col_non_remplis, 'colonne_non_remplis': colonne_non_remplis})
    resultat_df=pd.DataFrame(resultat)
    return resultat_df
    
        
        
    


        
            
            
      
        
        



