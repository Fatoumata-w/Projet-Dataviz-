# COVID‑19 DATAVIZ 2 — Analyse mondiale de la pandémie  
Projet réalisé par Fatoumata Batouly BA , Aissatou Diop &  Hawa Doucouré
EPSI Paris — BTS SIO SLAM — Dataviz 2

---

## Présentation du projet

L'objectif du projet est de concevoir un pipeline ETL permettant d'extraire, transformer et charger des données relatives au COVID-19 afin de les exploiter dans une application web de visualisation.

L'application permet d'analyser et de comparer différents indicateurs grâce à des graphiques interactifs.

---

## Problématique

Comment exploiter des données Open Data sur le COVID-19 afin de faciliter leur analyse et leur compréhension à travers une interface web interactive ?

---

## Objectifs

- Définir une problématique autour d'un jeu de données.
- Concevoir un pipeline ETL.
- Développer une interface web de visualisation.
- Analyser et interpréter les données.

---

## Technologies utilisées

### Développement Web

- HTML
- CSS
- JavaScript

### Visualisation de données

- Chart.js

### Outils

- Visual Studio Code
- GitHub

---

## Sources de données

Les données utilisées proviennent de sources Open Data :

- Our World In Data (OWID)
- Organisation Mondiale de la Santé (OMS)

Les données sont récupérées au format CSV puis préparées pour l'affichage des graphiques.

---

## Fonctionnement du pipeline ETL

### 1. Extract

- Récupération des données depuis des sources publiques.
- Import des fichiers CSV.
- Centralisation des données pour traitement.

### 2. Transform

- Tri des données selon différents critères.
- Nettoyage des valeurs incohérentes ou manquantes.
- Structuration et normalisation des données.
- Agrégation des données pour faciliter l'analyse.

### 3. Load

- Export des données nettoyées au format CSV.
- Organisation des données selon les besoins des graphiques.
- Préparation des données pour l'application web.

---

## Schéma du pipeline ETL

```text
Sources Open Data (OWID / OMS)
                │
                ▼
            Extract
                │
                ▼
           Transform
     (tri, nettoyage,
      normalisation)
                │
                ▼
              Load
        (fichiers CSV)
                │
                ▼
      Application Web
      HTML / CSS / JS
                │
                ▼
      Graphiques Chart.js
```

---

## Fonctionnalités

L'application permet :

- La visualisation de données liées au COVID-19.
- La comparaison entre différents pays.
- L'analyse de l'évolution des indicateurs.
- L'affichage de graphiques interactifs.
- L'interprétation des données à travers différents tableaux de bord.

---

## Productions réalisées

- Application web de data visualisation.
- Graphiques interactifs.
- Jeux de données structurés (CSV).
- Pipeline ETL automatisé pour l'extraction, la transformation et le chargement des données.

---

## Structure du projet

```text
Projet-Dataviz

etl_covid.py

data/
├── evolution_mondiale.csv
├── stats_pays.csv
├── vaccination.csv
└── stats_continents.csv

index.html
comparaison.html
vaccination.html
conclusion.html

utils.js
style.css
```

---

## Lancement du projet

1. Exécuter le pipeline ETL.
2. Générer les fichiers CSV nécessaires à l'application.
3. Ouvrir le fichier `index.html`.
4. Naviguer entre les différentes pages pour consulter les graphiques.

Les fichiers CSV présents dans le projet correspondent aux données structurées produites par le pipeline ETL et utilisées pour l'affichage des visualisations.
