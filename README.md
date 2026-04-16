# 🎯 Projet 11 – Système RAG de recommandation d’événements

## 📌 Objectif du projet

Dans le cadre de ce projet, j’ai développé un système de recommandation d’événements culturels et scientifiques basé sur une architecture RAG (Retrieval-Augmented Generation).

L’objectif est de permettre à un utilisateur de poser une question en langage naturel (ex : “Je cherche une exposition artistique à Paris”) et d’obtenir une réponse pertinente, structurée et contextualisée à partir de données réelles.

---

## 🧠 Principe du système RAG

Le système repose sur deux briques principales :

- Retrieval (recherche) : récupération des documents pertinents via un moteur vectoriel (FAISS)
- Generation (génération) : création d’une réponse en langage naturel avec un modèle Mistral

---

## 🔄 Schéma global du RAG

Utilisateur
   ↓
Question en langage naturel
   ↓
Transformation en embedding
   ↓
Recherche vectorielle (FAISS)
   ↓
Top K documents pertinents
   ↓
Injection dans le prompt
   ↓
Modèle Mistral (LLM)
   ↓
Réponse générée

---

## 📊 Sources de données

J’ai utilisé les sources suivantes :

- API OpenAgenda
- Dataset OpenDataSoft : événements publics OpenAgenda

Ces données contiennent :
- titre
- description
- dates
- lieu
- ville
- mots-clés

---

## ⚙️ Stack technique

- Python 3.13
- Pandas (traitement des données)
- FAISS (vector store)
- Mistral AI (génération)
- LangChain (orchestration RAG)
- Requests (API)

---

## 📁 Structure du projet

projet_11_rag_events/
│
├── data/
│   ├── raw/            # données brutes (JSON)
│   ├── processed/      # données nettoyées (CSV)
│   ├── vectorstore/    # index FAISS
│   └── test/           # jeux de test RAG
│
├── src/
│   ├── ingestion_openagenda_api.py
│   ├── preprocessing.py
│   ├── prepare_documents.py
│   ├── vectorstore.py
│   ├── rag.py
│   ├── chatbot.py
│   ├── evaluate_rag.py
│   └── test_data_quality.py
│
├── requirements.txt
├── README.md
└── .env.example

---

## 🔄 Pipeline complet du projet

[1] Ingestion
    ↓
Récupération API OpenAgenda
    ↓
Stockage JSON (data/raw)

[2] Préprocessing
    ↓
Nettoyage des données
Filtrage temporel et géographique
    ↓
CSV propre (data/processed)

[3] Préparation des documents
    ↓
Transformation en texte structuré
    ↓
Documents exploitables RAG

[4] Vectorisation
    ↓
Embeddings des documents
    ↓
Stockage FAISS (vectorstore)

[5] Retrieval
    ↓
Recherche des documents pertinents

[6] Génération
    ↓
Prompt + Mistral
    ↓
Réponse utilisateur

---

## 🔧 Étapes d’exécution

1. Ingestion des données
python src/ingestion_openagenda_api.py

2. Prétraitement
python src/preprocessing.py

3. Préparation des documents
python src/prepare_documents.py

4. Vectorisation
python src/vectorstore.py

5. Test du système RAG
python src/rag.py

6. Lancement du chatbot
python src/chatbot.py

7. Évaluation
python src/evaluate_rag.py

---

## 🧪 Tests

pytest

---

## 📈 Exemple de fonctionnement

Question utilisateur :
Je cherche une conférence scientifique

Réponse générée :
- Titre : Science à la coque – rôle du synchrotron
- Date : 16 avril 2026
- Lieu : Gif-sur-Yvette

---

## ✅ Résultats

Le système permet :

- de retrouver des événements pertinents
- de répondre à des requêtes en langage naturel
- de générer des réponses structurées (titre, date, lieu)

---

## ⚠️ Limites

- dépendance au dataset (volume limité)
- absence de métriques quantitatives avancées
- pas de chunking des documents
- gestion limitée des requêtes temporelles

---

## 🚀 Axes d’amélioration

- augmentation du dataset
- amélioration du retrieval
- ajout de filtres avancés (date, localisation)
- déploiement API (FastAPI)
- interface web utilisateur

---

## 👤 Auteur

Samir Belasri  
Projet Data Engineering – 2026

---

