# COVID-19 DATAVIZ 2 — Analyse mondiale de la pandémie

**Projet réalisé par Fatoumata Batouly BA, Aissatou Diop et Hawa Doucouré**  
**EPSI Paris — BTS SIO SLAM**

---

## Présentation du projet

Dans le cadre du BTS SIO option SLAM, ce projet a été réalisé en groupe afin de mettre en œuvre un pipeline ETL complet permettant d'exploiter des données ouvertes relatives à la pandémie de COVID-19.

L'objectif est de récupérer des données issues de sources Open Data, de les transformer afin de les rendre exploitables puis de les afficher dans une application web interactive proposant plusieurs visualisations graphiques.

---

## Problématique

Comment exploiter des données Open Data sur le COVID-19 afin de faciliter leur analyse et leur compréhension grâce à une interface web de visualisation interactive ?

---

## Objectifs du projet

- Définir une problématique autour d'un jeu de données.
- Concevoir un pipeline ETL automatisé.
- Extraire, transformer et charger des données issues de sources Open Data.
- Développer une interface web de visualisation.
- Analyser et interpréter les données à travers différents graphiques.

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

Les données utilisées proviennent de sources Open Data publiques :

- Our World In Data (OWID)
- Organisation Mondiale de la Santé (OMS)

Les données sont récupérées au format CSV puis préparées afin d'être exploitées par l'application web.

---

## Pipeline ETL

### 1. Extract

Cette étape consiste à récupérer les données depuis des sources Open Data.

Actions réalisées :

- Récupération des données COVID-19 depuis OWID et l'OMS.
- Import des fichiers au format CSV.
- Centralisation des données pour leur traitement.

### 2. Transform

Cette étape permet de préparer les données pour l'analyse.

Actions réalisées :

- Tri des données selon différents critères (dates, pays, indicateurs).
- Nettoyage des données manquantes ou incohérentes.
- Structuration et normalisation des informations.
- Agrégation des données afin de faciliter les analyses statistiques.

### 3. Load

Cette étape consiste à préparer les données pour l'application.

Actions réalisées :

- Génération de fichiers CSV structurés.
- Organisation des données selon les besoins des visualisations.
- Mise à disposition des données pour l'application web.

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
       (génération CSV)
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

- La visualisation des données liées au COVID-19.
- La comparaison entre différents pays.
- L'analyse de l'évolution de la pandémie.
- L'étude des campagnes de vaccination.
- L'affichage de graphiques interactifs.
- L'interprétation des données grâce à plusieurs tableaux de bord.

---

## Productions réalisées

- Application web de data visualisation.
- Graphiques interactifs réalisés avec Chart.js.
- Jeux de données structurés au format CSV.
- Pipeline ETL automatisé pour l'extraction, la transformation et le chargement des données.

---

## Structure du projet

```text
Projet-Dataviz

etl_covid.py

data/
└── (fichiers CSV générés automatiquement)

index.html
comparaison.html
vaccination.html
conclusion.html

utils.js
style.css
```

---

## Exécution du projet

### 1. Exécuter le pipeline ETL

```bash
python etl_covid.py
```

Cette étape permet :

- de récupérer les données depuis les sources Open Data ;
- de transformer les données ;
- de générer automatiquement les fichiers CSV nécessaires à l'application.

### 2. Lancer l'application

Ouvrir le fichier :

```text
index.html
```

Puis naviguer entre les différentes pages afin de consulter les visualisations et les analyses proposées.

---

## Résultat attendu

Le projet fournit un outil d'analyse visuelle permettant :

- d'explorer les données COVID-19 ;
- de comparer différents pays et indicateurs ;
- d'interpréter les évolutions observées grâce à des graphiques interactifs.

Les fichiers CSV utilisés par l'application sont générés automatiquement par le pipeline ETL et ne sont pas stockés dans le dépôt GitHub.
