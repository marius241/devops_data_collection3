import requests
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# Chargement des fichiers de données
dataframe = pd.read_csv('data/appartements_vendre.csv')

# Vérification si les colonnes à supprimer sont présentes dans le DataFrame
columns_to_remove = ['web-scraper-order', 'web-scraper-start-url', 'liens_articles', 'liens_articles-href']
columns_to_keep = [col for col in dataframe.columns if col not in columns_to_remove]

# Sélection des colonnes à conserver dans le DataFrame
dataframe = dataframe[columns_to_keep]

# Enlever les caractères indésirables dans la colonne 'prix'
dataframe['prix'] = dataframe['prix'].str.replace('.', '').str.replace('FCFA', '').str.strip()

# Remplacer les valeurs vides par 0 dans la colonne 'prix'
dataframe['prix'].fillna(0, inplace=True)

# Changer le type de données de la colonne 'prix' en entier (int)
dataframe['prix'] = dataframe['prix'].astype(int)

# Renommer les colonnes
dataframe.rename(columns={'details': 'V1', 'prix': 'V2(FCFA)', 'adresse': 'V3', 'image-src': 'V4'}, inplace=True)

# Données des prix des appartements
appartements = dataframe['V3']
prix = dataframe['V2(FCFA)']


# Création du DataFrame
data = pd.DataFrame({'Appartements': appartements, 'Prix (en FCFA)': prix})

# Création du diagramme à barres interactif avec Streamlit
st.title("Prix des appartements")
fig = px.bar(data, x='Appartements', y='Prix (en FCFA)', color='Prix (en FCFA)', title='Prix des appartements')
st.plotly_chart(fig)