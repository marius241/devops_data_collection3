PAGE_STYLES = """
<style>
/* Style pour agrandir la police */
.big-font {
    font-size:5em;
}
.titre_page {
    color: white;
    font-size:3.1em;
    margin-top:-10%;
    text-align: center;
    margin-bottom: 20px;
    text-align: justify;
}
/* Style pour le texte */
.titre_application {
    font-size:1.1em;
    margin-top:-12%;
    text-align: justify;
    white-space: nowrap;
    overflow: hidden;
    animation: scroll 2s linear infinite;
}

@keyframes scroll {
    0% {
        transform: translateX(0%);
    }
    50% {
        transform: translateX(5%);
    }
    100% {
        transform: translateX(0%);
    }
}
/* Style pour le texte */
.text {
    font-size:1.7em;
    text-align: justify;
}
/*Appliquer le CSS au bloc de texte Markdown*/
st.markdown(
    .markdown-text-container {
    }

/* Style pour le DataFrame */
.dataframe {
    width: 900%;
    background-color: #f1f1f1;
    color: blue;
}
"""