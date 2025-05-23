#!/bin/bash

# Installation des dépendances
echo "🚀 Installation des dépendances..."
pip install -r requirements.txt

# Création du dossier de configuration Streamlit
mkdir -p ~/.streamlit/

# Configuration Streamlit
echo "\n⚙️ Configuration de Streamlit..."
echo "\n[server]\n\
headless = true\n\
port = \$PORT\n\
enableCORS = false\n\
\n[browser]\n\
serverAddress = \"0.0.0.0\"\n\
serverPort = \$PORT" > ~/.streamlit/config.toml

# Message de fin
echo "\n✅ Configuration terminée !"
echo "Pour lancer l'application en local :"
echo "streamlit run app.py"

echo "\n🌐 Pour déployer sur Streamlit Cloud :"
echo "1. Créez un nouveau dépôt GitHub"
echo "2. Poussez ce dossier sur GitHub"
echo "3. Connectez-le à Streamlit Cloud"
echo "4. Sélectionnez app.py comme fichier principal"
