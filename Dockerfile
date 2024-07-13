# Image de base de Python 3.9
FROM python:3.9-slim

#Rep de travail
#WORKDIR nous donne le repeetoire de travail
WORKDIR /app

#copier le code source
#Avec la commande COPY TOUT LE contenue du projet vers le docker
COPY . .

#Dependances Python ====>>>> requirements.txt
#RUN exécute une commande
RUN pip install --no-cache-dir -r requirements.txt

#Exposer le port sur lequel Streamlit va déboguer
#8501 est le port par défaut de streamlit
EXPOSE 8501

#Commande pour lancer l'application
CMD ["streamlit", "run", "Accueil.py"]