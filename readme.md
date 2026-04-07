# COVID‑19 DATAVIZ 2 — Analyse mondiale de la pandémie  
Projet réalisé par Fatoumata Batouly BA , Aissatou Diop &  Hawa Doucouré
EPSI Paris — BTS SIO SLAM — Dataviz 2

---

##  1. Objectif du projet
Ce projet a pour but de **visualiser l’évolution mondiale de la pandémie de COVID‑19** à partir de données officielles (OMS + Our World in Data).  
Nous avons construit :

- un **ETL complet** (Extraction → Transformation → Chargement)
- un **site web de datavisualisation** (HTML/CSS/JS)
- plusieurs **graphiques interactifs** (Chart.js)
- une **carte mondiale choroplèthe** (Plotly)
- une **analyse comparative** entre pays
- une **analyse de la vaccination**

---

##  2. Architecture du projet
covid-dataviz/
│
├── data/
│   ├── raw/               # Données brutes OMS / OWID
│   └── transformed/       # Données nettoyées (CSV finaux)
│
├── etl/
│   └── etl_covid.py       # Script ETL (nettoyage + fusion + calculs)
│
├── frontend/
│   ├── index.html         # Page d’accueil
│   ├── evolution.html     # Évolution mondiale (graphiques + carte)
│   ├── comparaison.html   # Comparaison des pays
│   ├── vaccination.html   # Vaccination mondiale
│   ├── conclusion.html    # Synthèse finale
│   ├── style.css          # Styles du site
│   └── utils.js           # Fonctions JS + chargement CSV + graphiques
│
└── README.md


---

##  3. Technologies utilisées

### **Frontend**
- HTML5 / CSS3
- JavaScript ES6
- Chart.js (graphiques)
- Plotly.js (carte mondiale)
- Responsive design

### **Données**
- CSV nettoyés via ETL
- Sources :
  - **OMS (WHO COVID‑19 Global Data)**
  - **Our World in Data (OWID)**

### **ETL**
- Python  
- Pandas  
- Calculs ajoutés :
  - `cases_per_million`
  - `deaths_per_million`
  - `deaths_per_1000`
  - `mortality_rate`

---

##  4. ETL — Description rapide

Le script ETL effectue :

1. **Extraction**  
   - Chargement des fichiers bruts OMS + OWID

2. **Transformation**  
   - Nettoyage des colonnes
   - Harmonisation des noms de pays
   - Gestion des valeurs manquantes
   - Calcul des indicateurs normalisés

3. **Chargement**  
   - Export en CSV dans `data/transformed/`
   - Fichiers finaux utilisés par le site :
     - `evolution_mondiale.csv`
     - `stats_pays.csv`
     - `vaccination.csv`

---

##  5. Fonctionnalités du site

### Page **Évolution**
- Graphique des **3 vagues** (barres / courbes)
- Graphique **cas vs décès** (double axe)
- **Carte mondiale** des décès pour 1000 habitants (Plotly)

### Page **Comparaison**
- Classement des pays selon :
  - décès/million
  - cas/million
  - mortalité
- Graphique horizontal interactif

### Page **Vaccination**
- Taux de vaccination par pays
- Analyse du découplage cas/décès

### Page **Conclusion**
- Synthèse des observations
- Interprétation des données

---

##  6. Lancer le projet

### Option 1 — Ouvrir directement les fichiers HTML  
Fonctionne car les données sont en CSV local.

### Option 2 — Serveur local (recommandé)
```bash
cd frontend
python -m http.server 8000

 7. Sources
OMS — WHO COVID‑19 Global Data

Our World in Data — COVID‑19 Dataset

Banque Mondiale — Indicateurs démographiques