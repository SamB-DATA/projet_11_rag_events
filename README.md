# Projet 11 - Mise en place d’un système RAG avec OpenAgenda

## 1. Présentation du projet

Ce projet consiste à concevoir un assistant intelligent capable de recommander des événements culturels à partir de données réelles.

Le système repose sur une architecture **RAG (Retrieval-Augmented Generation)** :

* récupération d’informations pertinentes dans une base vectorielle
* génération de réponses via un modèle de langage (LLM)

Les données utilisées proviennent de l’API OpenAgenda.

---

## 2. Objectifs

* Collecter des données d’événements publics
* Nettoyer et structurer les données
* Créer une base vectorielle avec FAISS
* Implémenter un système RAG avec Mistral
* Développer un chatbot simple
* Garantir la qualité des données avec des tests

---

## 3. Stack technique

* Python 3.13
* Pandas
* FAISS (vector store)
* LangChain
* Mistral AI (LLM + embeddings)
* Pytest (tests unitaires)

---

## 4. Structure du projet

```text
projet_11_rag_events/
│
├── data/
│   ├── raw/                # Données brutes
│   ├── processed/          # Données nettoyées
│   └── vectorstore/        # Index FAISS
│
├── src/
│   ├── ingestion_openagenda_api.py
│   ├── preprocessing.py
│   ├── prepare_documents.py
│   ├── vectorstore.py
│   ├── retrieval_demo.py
│   ├── rag.py
│   └── chatbot.py
│
├── tests/
│   └── test_data_quality.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## 5. Installation

### 1. Créer un environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Ajouter la clé API Mistral

Créer un fichier `.env` :

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## 6. Pipeline complet

### 1. Ingestion des données

```bash
python src/ingestion_openagenda_api.py
```

### 2. Nettoyage des données

```bash
python src/preprocessing.py
```

### 3. Préparation des documents

```bash
python src/prepare_documents.py
```

### 4. Création du vector store

```bash
python src/vectorstore.py
```

---

## 7. Test du système RAG

```bash
python src/rag.py
```

---

## 8. Lancer le chatbot

```bash
python src/chatbot.py
```

Exemples de requêtes :

* Je cherche une exposition artistique
* Je veux une conférence scientifique
* Je cherche un événement autour de l’intelligence artificielle

---

## 9. Tests unitaires

Lancer les tests :

```bash
pytest
```

Objectifs des tests :

* vérifier la qualité des données
* vérifier les colonnes obligatoires
* vérifier la validité des dates
* contrôler le périmètre géographique

---

## 10. Limites du projet

* Dataset limité à certains agendas (principalement Paris-Saclay)
* Pas de filtrage avancé par date ou ville
* Pas d’interface graphique (CLI uniquement)
* Pas de monitoring du modèle en production

---

## 11. Améliorations possibles

* Ajouter une interface web (Streamlit)
* Filtrer les résultats par date / localisation
* Améliorer le nettoyage des métadonnées
* Ajouter un système d’évaluation du RAG (RAGAS)
* Déployer le modèle en production

---

## 12. Auteur

Projet réalisé par :
Samir Belasri 
