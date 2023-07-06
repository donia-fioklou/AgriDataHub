import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.markdown("### Importer un fichier et resortir les incohérences")

file_upload=st.file_uploader(label="uploader un ficher",type=['xlsx'])

# decoupage du dataframe apres chaque colonne Fin

def decoupage(df):
    forms=[]
    col_name=[]
    for col in df.columns:
        col_name.append(col)
        if 'Fin' in col:
            forms.append(df.loc[:,col_name])
            col_name=[]
    return forms

#liste de form concatener avec l'id
def concat_id():
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
    
        
        
    

if file_upload: 
    df= pd.read_excel(file_upload)
    st.dataframe(df)
    forms=decoupage(df)
    forms_with_id=concat_id()    
    st.dataframe(forms[0]) 
        
    for form in forms_with_id:
        st.dataframe(form) 
        #incoherence=analyse_incoherence(form)
        st.write('-------------------')
        
            
            
      
        
        



