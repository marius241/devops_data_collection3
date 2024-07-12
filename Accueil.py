import streamlit as st
from css.style_accueil import CSS_STYLES
from css.style_frame import CSS_LIEN

# Page principale qui appelle les autres pages
def main():
    
    # Ajouter du CSS personnalisé
    st.markdown(CSS_STYLES, unsafe_allow_html=True)
    
    # Afficher les titres et le texte avec les classes CSS personnalisées
    st.markdown('<h1 class="titre">BIENVENUE SUR <h1 class="aevd">AEVD</h1></h1>', unsafe_allow_html=True)
    st.markdown("""<h2 class="subtitle">Application d'Extraction et de Visualisation<br>
                de Données<br>
                 Avec  Web Scraper et BeautifulSoup.</h2>""", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
        Nous sommes ravis de vous aider à extraire des données à partir du site Dakar-Vente.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="source">Source : </div>', unsafe_allow_html=True)
    
    # Afficher le lien avec le style CSS
    st.markdown("""
        [DAKAR VENTE](https://dakarvente.com)
        """, unsafe_allow_html=True)
    # Appliquer le style CSS
    st.markdown(f"<style>{CSS_LIEN}</style>", unsafe_allow_html=True)
    
                
    # Récupérer l'URL du lien
    url = "https://dakarvente.com"
    
    # Afficher le lien dans un iframe
    st.markdown(f'<iframe src="{url}" class=iframe_accueil></iframe>', unsafe_allow_html=True)
    # Personnaliser la largeur de la barre latérale
    st.markdown(
        """
        <style>
        .title {
            margin-left:35%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            width:5%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
# Exécutez l'application
if __name__ == "__main__":
    main()