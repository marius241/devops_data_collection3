import requests
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from bs4 import BeautifulSoup as bs

from css.style_page import PAGE_STYLES

# Ajouter du CSS personnalisé
st.markdown(PAGE_STYLES, unsafe_allow_html=True)

# Définir le titre de la pages
st.markdown('<h1 class="titre_application">VOUS ÊTES SUR AEVD(APPLICATION D\'EXTRACTION ET DE VISUALISATION DE DONNEES)</h1>', unsafe_allow_html=True)

# Définir le titre de la pages
st.markdown('<h1 class="titre_page">APPARTEMENTS À LOUER</h1>', unsafe_allow_html=True)
st.markdown(
        """
        <div class="text">
        Nous sommes ravis de vous aider à extraire des données à partir du site Dakar-Vente.
        </div>
        """,
        unsafe_allow_html=True
    )
# Définir quelques styles CSS liés aux boîtes
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

# Fonction de chargement des données
def load_data(dataframe, title, key):
    st.markdown(
        """<style>
            .stButton {
            text-align:left;
            }
            </style>
        """, unsafe_allow_html=True)
    
    if st.button(title, key):
        # Appliquer le style au subheader
        st.markdown(
            """
            <style>
            .subheader {
                font-size: 2em;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Appliquer le style à l'écriture de dimensions des données
        st.markdown(
            """
            <style>
            .dimensions {
                font-size: 1.5em;
                margin-top: 1%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Affichage des dimensions des données
        st.markdown('<p class="subheader"> Affichage des dimensions des données</p>',unsafe_allow_html=True)
        st.markdown('<p class="dimensions">Dimensions des données : ' + str(dataframe.shape[0]) + ' lignes et ' + str(dataframe.shape[1]) + ' colonnes.</p>', unsafe_allow_html=True)
        
        # Appliquer le style au DataFrame
        styles = [
            dict(selector="table", props=[("margin-left", "-100%")]),
            dict(selector="th", props=[("font-size", "16px")]),
            dict(selector="td", props=[("font-size", "14px")])
        ]
        styled_dataframe = dataframe.style.set_table_styles(styles)
        # Appliquer le style au DataFrame
        #styled_dataframe = dataframe.style.set_properties(**{'padding-left':'-90%','width':'1000px','background-color': '#f1f1f1', 'color': 'blue'}, unsafe_allow_html=True)
        # Afficher le DataFrame stylisé
        st.dataframe(styled_dataframe)
                    
        if st.button("Réduire"):
            st.empty()
            
choix = st.sidebar.radio("Différents type de Scrapping", ["SCRAPER BRUT","SCRAPER CLEANING","BEAUTIFUL SOUP"])
if choix == "BEAUTIFUL SOUP":
    # Ajouter du CSS pour agrandir l'espace des données
    st.markdown(
        """
        <style>
        .dataframe {
            width: 100%;
            height: 500px;
            textColor:white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    def extraire_page(selected_page):
        df = pd.DataFrame()
        for p in range(1,selected_page+1):
            url=f'https://dakarvente.com/index.php?page=annonces_categorie&id=10&sort=&nb={p}'
            res = requests.get(url)# Récupérer le code html de la page
            bsoup = bs(res.text,'html')#stocker le code html dans un objet bs
            conteneurs = bsoup.find_all('article',class_='col-xs-6 col-sm-4 col-md-6 col-lg-4 item item-product-grid-3 post')
            data=[]
            for conteneur in conteneurs:
                try:
                    link = 'https://dakarvente.com/annonces-categorie-appartements-louer-10.html' + conteneur.find('a', class_="")['href']
                    if link is not None:#Sauter lien location vente auto
                        res_c = requests.get(link)
                        bsoup_c = bs(res_c.text, 'html.parser')
                    inf_gen = conteneur.find('div', class_='item-inner mv-effect-translate-1 mv-box-shadow-gray-1').find_all('div')
                    prix = inf_gen[3].text.replace(' ', '').replace('FCFA', '').strip()
                    details = inf_gen[4].text.strip()
                    adresse = inf_gen[5].text.strip()
                    image = conteneur.find('img')['src']
                    dico = {
                        'V1': details,
                        'V2(FCFA)': prix,
                        'V3': adresse,
                        'V4': image
                    }
                    data.append(dico)
                except:
                    pass
            df1 = pd.DataFrame(data)
            df = pd.concat([df, df1],axis = 0).reset_index(drop = True)
        return df
    
    # Liste complète des pages
    pages = list(range(1, 35))
    selected_page = st.selectbox("CHOISIR LE NOMBRE DE PAGE ", pages)
    
    if selected_page in pages:
        df = extraire_page(selected_page)
        if not df.empty:
            st.title("Appartements à louer au Sénégal")
            if str(selected_page)<="1":
                st.header("Résultats pour "+ str(selected_page) + " page sélectionnée :")
            else:
                st.header("Résultats pour "+ str(selected_page) + " pages sélectionnée :")
            st.write('Dimensions des données: ' + str(df.shape[0]) + ' lignes et ' + str(df.shape[1]) + ' colonnes.')           
            st.dataframe(df)
        else:
            st.write("Aucun résultat à afficher.")
    else:
        st.write("Veuillez sélectionner une page valide.")
############################################################################""
if choix == "SCRAPER BRUT":
    # Chargement des fichiers de données
    dataframe1 = pd.read_csv('data/appartements_louer_34_27.csv')
    dataframe2 = pd.read_csv('data/appartements_louer_26_13.csv')
    dataframe3 = pd.read_csv('data/appartements_louer_12_4.csv')
    dataframe4 = pd.read_csv('data/appartements_louer_3.csv')
    dataframe5 = pd.read_csv('data/appartements_louer_2.csv')
    dataframe6 = pd.read_csv('data/appartements_louer_1.csv')

    # Liste des dataframes
    dataframes = [dataframe2, dataframe3, dataframe4, dataframe5, dataframe6]

    # Liste des compteurs de départ
    start_counters = [314, 896, 1266, 1308, 1350]

    # Boucle pour mettre à jour les valeurs de la colonne 'web-scraper-order' dans chaque dataframe
    for dataframe, start_counter in zip(dataframes, start_counters):
        counter = start_counter
        for i in range(len(dataframe)):
            if '-' in dataframe.loc[i, 'web-scraper-order']:
                dataframe.loc[i, 'web-scraper-order'] = dataframe.loc[i, 'web-scraper-order'].split('-')[0] + '-' + str(counter)
                counter += 1

    # Concaténation des fichiers de données
    concate_df = pd.concat([dataframe1] + dataframes)
    
    # Réinitialisation des index
    concate_df.reset_index(drop=True, inplace=True)
    
    # Renommer les colonnes
    concate_df.rename(columns={'details': 'V1', 'prix': 'V2', 'adresse': 'V3', 'image-src': 'V4'}, inplace=True)
    
    # Utilisation de la fonction load_data pour afficher les dimensions et les données concaténées
    load_data(concate_df, 'Afficher les données', '1')
if choix == "SCRAPER CLEANING":
    # Chargement des fichiers de données
    dataframe1 = pd.read_csv('data/appartements_louer_34_27.csv')
    dataframe2 = pd.read_csv('data/appartements_louer_26_13.csv')
    dataframe3 = pd.read_csv('data/appartements_louer_12_4.csv')
    dataframe4 = pd.read_csv('data/appartements_louer_3.csv')
    dataframe5 = pd.read_csv('data/appartements_louer_2.csv')
    dataframe6 = pd.read_csv('data/appartements_louer_1.csv')

    # Liste des dataframes
    dataframes = [dataframe2, dataframe3, dataframe4, dataframe5, dataframe6]

    # Liste des compteurs de départ
    start_counters = [314, 896, 1266, 1308, 1350]

    # Boucle pour mettre à jour les valeurs de la colonne 'web-scraper-order' dans chaque dataframe
    for dataframe, start_counter in zip(dataframes, start_counters):
        counter = start_counter
        for i in range(len(dataframe)):
            if '-' in dataframe.loc[i, 'web-scraper-order']:
                dataframe.loc[i, 'web-scraper-order'] = dataframe.loc[i, 'web-scraper-order'].split('-')[0] + '-' + str(counter)
                counter += 1

    # Concaténation des fichiers de données
    concate_df = pd.concat([dataframe1] + dataframes)
    
    # Réinitialisation des index
    concate_df.reset_index(drop=True, inplace=True)
    
    
    # Vérification si les colonnes à supprimer sont présentes dans le DataFrame
    columns_to_remove = ['web-scraper-order', 'web-scraper-start-url', 'liens_articles', 'liens_articles-href']
    columns_to_keep = [col for col in concate_df.columns if col not in columns_to_remove]

    # Sélection des colonnes à conserver dans le DataFrame
    concate_df = concate_df[columns_to_keep]
    
    # Enlever les caractères indésirables dans la colonne 'prix'
    concate_df['prix'] = concate_df['prix'].str.replace('.', '').str.replace('FCFA', '').str.strip()
    
    # Remplacer les valeurs vides par 0 dans la colonne 'prix'
    concate_df['prix'].fillna(0, inplace=True)
    
    # Changer le type de données de la colonne 'prix' en entier (int)
    concate_df['prix'] = concate_df['prix'].astype(int)
    
    # Renommer les colonnes
    concate_df.rename(columns={'details': 'V1', 'prix': 'V2(FCFA)', 'adresse': 'V3', 'image-src': 'V4'}, inplace=True)

    # Fonction pour visualiser les données
    def visualize_data(dataframe):
        st.subheader('Visualisation des données')

        # Bouton pour afficher un graphique
        if st.button('Graphique À Bulles'):
            # Comptage du nombre d'apparitions des villes
            counts = dataframe['V3'].value_counts()

            # Création du DataFrame pour le graphique
            df = pd.DataFrame({'Nombre D`Annonce(s)': counts.values, 'Adresse': counts.index})

            st.title("Nombre D'Annonce Par Adresse")
            # Création du graphique de dispersion avec Plotly
            fig = px.scatter(df, x='Nombre D`Annonce(s)', y='Adresse', size='Nombre D`Annonce(s)', hover_data=['Nombre D`Annonce(s)', 'Adresse'], size_max=50)

            # Personnalisation des étiquettes de survol des points
            fig.update_traces(hovertemplate='<b>Adresse: %{y}</b><br>Nombre D`Annonce(s): %{x}')
    
            # Affichage du graphique à l'aide de st.plotly_chart()
            st.plotly_chart(fig)
            
            #Bouton réduire
            if st.button("Réduire"):
                st.empty()
        
        # Bouton pour afficher un graphique
        if st.button('Graphique Des Prix'):
           # Données des prix des appartements
            appartements = dataframe['V3']
            prix = dataframe['V2(FCFA)']

            # Création du DataFrame
            data = pd.DataFrame({'Adresse': appartements, 'Prix(FCFA)': prix})
            
           
            data['Prix(FCFA)'] = data['Prix(FCFA)'].astype(int)
            data = data.sort_values('Prix(FCFA)', ascending=False)
            
            # Création du diagramme à barres interactif avec Streamlit
            #st.title("Prix Des Appartements")
            fig = px.bar(data, x='Adresse', y='Prix(FCFA)', color='Prix(FCFA)', title='Prix des appartements')
            st.plotly_chart(fig)
            
            #Bouton réduire
            if st.button("Réduire"):
                st.empty()
            
        # Bouton pour afficher un graphique Seaborn
        if st.button('Graphique En Planètes'):
        # Comptage du nombre d'apparitions des villes
            counts = dataframe['V3'].value_counts()

            # Création du DataFrame pour le graphique
            df = pd.DataFrame({'Annonce(s)': counts.values, 'Adresse': counts.index})

            # Création du graphique en sphère en 3D avec Plotly
            fig = go.Figure(data=go.Scatter3d(
                x=np.random.uniform(-1, 1, len(df)),  # Coordonnées x aléatoires pour la répartition des bulles
                y=np.random.uniform(-1, 1, len(df)),  # Coordonnées y aléatoires pour la répartition des bulles
                z=np.random.uniform(-1, 1, len(df)),  # Coordonnées z aléatoires pour la répartition des bulles
                mode='markers',
                marker=dict(
                    size=df['Annonce(s)'],
                    color=df['Annonce(s)'],
                    colorscale='Viridis',
                    opacity=0.8
                ),
                hovertemplate='<b>Adresse: %{text}</b><br>Annonce(s): %{marker.size}',
                text=df['Adresse']
            ))

            # Animation pour faire tourner les sphères
            frames = []
            for i in range(0, 360, 5):
                frame = go.Frame(
                    layout=dict(scene=dict(camera=dict(eye=dict(x=1.5*np.cos(np.deg2rad(i)),
                                                                y=1.5*np.sin(np.deg2rad(i)),
                                                                z=1.5))))
                )
                frames.append(frame)

            fig.frames = frames

            # Personnalisation de l'aspect du graphique en sphère en 3D
            fig.update_layout(scene=dict(
                xaxis=dict(showticklabels=False, showgrid=False, visible=False),
                yaxis=dict(showticklabels=False, showgrid=False, visible=False),
                zaxis=dict(showticklabels=False, showgrid=False, visible=False),
                aspectmode='cube'
            ))

            # Affichage du graphique à l'aide de st.plotly_chart()
            st.plotly_chart(fig)
            
            #Bouton réduire
            if st.button("Réduire"):
                st.empty()
            

    # Utilisation de la fonction load_data pour afficher les dimensions et les données concaténées
    load_data(concate_df, 'Afficher les données', '1')
         
    visualize_data(concate_df)
