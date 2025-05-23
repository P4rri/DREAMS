import streamlit as st
from datetime import datetime
import sqlite3
import os

# Configuration de la page
st.set_page_config(
    page_title="DreamsEcho",
    page_icon="🌙",
    layout="wide"
)

# Initialisation de la base de données
def init_db():
    conn = sqlite3.connect('dreams.db')
    c = conn.cursor()
    
    # Création de la table des rêves
    c.execute('''
        CREATE TABLE IF NOT EXISTS dreams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date TEXT NOT NULL,
            mood TEXT,
            sleep_quality INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

# Fonction pour ajouter un rêve
def add_dream(title, content, mood, sleep_quality):
    conn = sqlite3.connect('dreams.db')
    c = conn.cursor()
    
    c.execute("""
        INSERT INTO dreams (title, content, date, mood, sleep_quality)
        VALUES (?, ?, ?, ?, ?)
    """, (title, content, datetime.now().strftime("%Y-%m-%d %H:%M"), mood, sleep_quality))
    
    conn.commit()
    conn.close()
    return True

# Fonction pour récupérer tous les rêves
def get_dreams():
    conn = sqlite3.connect('dreams.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM dreams ORDER BY date DESC")
    dreams = c.fetchall()
    
    conn.close()
    return dreams

# Initialisation de la base de données
init_db()

# Interface utilisateur
st.title("🌙 DreamsEcho")
st.write("Votre journal de rêves personnel")

# Barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Menu", ["Ajouter un rêve", "Voir mes rêves", "Statistiques"])

# Page d'ajout de rêve
if page == "Ajouter un rêve":
    st.header("📝 Nouveau Rêve")
    
    with st.form("dream_form"):
        title = st.text_input("Titre du rêve")
        content = st.text_area("Décrivez votre rêve", height=200)
        
        col1, col2 = st.columns(2)
        with col1:
            mood = st.selectbox("Humeur", ["😊 Heureux", "😐 Neutre", "😔 Triste", "😨 Effrayé"])
        with col2:
            sleep_quality = st.slider("Qualité du sommeil", 1, 10, 5)
        
        submitted = st.form_submit_button("Enregistrer le rêve")
        if submitted:
            if title and content:
                if add_dream(title, content, mood, sleep_quality):
                    st.success("Rêve enregistré avec succès !")
            else:
                st.warning("Veuillez remplir tous les champs obligatoires")

# Page de visualisation des rêves
elif page == "Voir mes rêves":
    st.header("📖 Mes Rêves")
    
    dreams = get_dreams()
    
    if not dreams:
        st.info("Aucun rêve enregistré pour le moment.")
    else:
        for dream in dreams:
            with st.expander(f"{dream[1]} - {dream[3]}"):
                st.write(f"**Humeur:** {dream[4]}")
                st.write(f"**Qualité du sommeil:** {dream[5]}/10")
                st.write("---")
                st.write(dream[2])

# Page de statistiques
else:
    st.header("📊 Statistiques")
    
    dreams = get_dreams()
    
    if not dreams:
        st.info("Aucune donnée à afficher pour le moment.")
    else:
        total_dreams = len(dreams)
        avg_sleep = sum(dream[5] for dream in dreams) / total_dreams
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Nombre total de rêves", total_dreams)
        
        with col2:
            st.metric("Qualité moyenne du sommeil", f"{avg_sleep:.1f}/10")
        
        # Simple graphique de l'humeur
        moods = ["😊 Heureux", "😐 Neutre", "😔 Triste", "😨 Effrayé"]
        mood_counts = {mood: 0 for mood in moods}
        
        for dream in dreams:
            if dream[4] in mood_counts:
                mood_counts[dream[4]] += 1
        
        st.subheader("Répartition des humeurs")
        for mood, count in mood_counts.items():
            if count > 0:
                st.write(f"{mood}: {count} rêves")
