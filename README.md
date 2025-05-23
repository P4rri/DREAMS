# DreamsEcho - Journal de Rêves

Application web pour enregistrer et suivre vos rêves, développée avec Streamlit.

## 🌟 Fonctionnalités

- ✨ Ajouter des rêves avec titre, description, humeur et qualité du sommeil
- 📚 Consulter l'historique de vos rêves
- 📊 Visualiser des statistiques sur vos habitudes de sommeil
- 🎨 Interface simple et intuitive

## 🚀 Installation

1. **Cloner le dépôt**
   ```bash
   git clone [URL_DU_DEPOT]
   cd [NOM_DU_DEPOT]
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Sur Windows
   source venv/bin/activate  # Sur macOS/Linux
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Lancement

```bash
streamlit run app.py
```

L'application sera disponible à l'adresse : http://localhost:8501

## 📁 Structure des fichiers

- `app.py` - Code source principal de l'application
- `requirements.txt` - Dépendances Python
- `dreams.db` - Base de données SQLite (créée automatiquement)
- `README.md` - Ce fichier d'instructions

## 🌐 Déploiement

### Sur Streamlit Cloud
1. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)
2. Connectez votre compte GitHub
3. Sélectionnez le dépôt et la branche
4. Spécifiez `app.py` comme fichier principal
5. Cliquez sur "Deploy"

## 📝 Notes

- La base de données est stockée localement dans le fichier `dreams.db`
- Aucune donnée personnelle n'est collectée
- Pour réinitialiser l'application, supprimez simplement le fichier `dreams.db`

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Ce projet est sous licence MIT.
