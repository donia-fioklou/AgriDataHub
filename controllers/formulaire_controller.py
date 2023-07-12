#taux de remplissage  des formulaires

from turtle import st
from matplotlib import pyplot as plt
from pages.analyse_de_fichier import decoupage


class TauxRemplissage():
    def __init__(self,df):
        self.df=df
    #nombre de formulaire
    def nombre_form(self):
        return len(decoupage(self.df))
    
    #liste des formulaires
    def liste_form(self):
        return decoupage(self.df)
    
    #taux de remplissage des formulaires
    def taux_remplissage(self):
        forms=decoupage(self.df)
        taux_remplissage_forms=[]
        for form in forms:
            taux_remplissage_columns=[]
            for column in form.columns: 
                #nombre de cellules remplies 
                nb_cellules_remplies= form[column].count()
                #nombre de cellules non remplies
                nb_cellules_non_remplies = form[column].isnull().sum()
                #taux de remplissage de la colonne
                taux_remplissage_colonne=nb_cellules_remplies/(nb_cellules_remplies+nb_cellules_non_remplies)
                taux_remplissage_columns.append(taux_remplissage_colonne)
            #taux de remplissage du formulaire
            taux_remplissage_forms.append(round((sum(taux_remplissage_columns)/len(taux_remplissage_columns))*100,2))
        
        return taux_remplissage_forms

        
        
                
                
        
