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
        
        taux_forms=[]
        for form in forms:
            taux_columns=[]
            for column in form.columns:  
                nb_cellules_remplies = form[column].count()
                nb_cellules_non_remplies = form[column].isnull().sum()
                taux_columns.append(nb_cellules_remplies/(nb_cellules_remplies+nb_cellules_non_remplies))
            #moyenne des taux_columns
            taux_forms.append(sum(taux_columns)/len(taux_columns))
        #graphique
        
        return taux_forms

        
        
                
                
        
