CSS_STYLES = """
<style>
/* Style pour les titres */
.titre{
    font-size:5em;
    margin-left:-40%;
}

/* Style pour le sous titres */
.subtitle {
    color: white;
    font-size:3.1em;
    margin-left:-40%;
    text-align: center;
    margin-bottom: 20px;
    text-align: justify;
}

/* Style pour le texte */
.text {
    font-size:1.7em;
    margin-left:-35%;
    text-align: justify;
    white-space: nowrap;
    overflow: hidden;
    animation: scroll 30s linear infinite;
}

@keyframes scroll {
    0% {
        transform: translateX(50%);
    }
    100% {
        transform: translateX(-4.5%);
    }
}

/* Style pour le texte */
.source {
    font-size:1.5em;
    margin-left:-40%;
    margin-bottom:1%;
    text-align: justify;
}

/* Style pour le iframe de la page d'accueil */
.iframe_accueil {
    width:180%;
    height:600px;
    padding: 10px;
    margin-left:-40%;
    border: 2px solid gold;
}
.aevd{
    font-size:5em;
    margin-left:42%;
    margin-top:-18.7%;
    color:red;
}
"""