# COVID-19 DATAVIZ 2 — Analyse mondiale de la pandémie

**Projet réalisé par Fatoumata Batouly BA, Aissatou Diop et Hawa Doucouré**  
**EPSI Paris — BTS SIO SLAM**

---

## Présentation du projet

Ce projet a été réalisé en groupe dans le cadre du BTS SIO option SLAM.

L'objectif est de créer un pipeline ETL permettant de récupérer des données Open Data sur le COVID-19, de les nettoyer, puis de les utiliser dans une application web de visualisation.

L'application permet de comparer et d'interpréter différents indicateurs liés à la pandémie grâce à des graphiques interactifs.

---

## Problématique

Comment exploiter des données Open Data sur le COVID-19 afin de faciliter leur analyse et leur compréhension grâce à une interface web interactive ?

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

Les données proviennent de sources Open Data :

- Our World In Data (OWID)
- Organisation Mondiale de la Santé (OMS)

Les données sont récupérées au format CSV puis préparées pour l'affichage des graphiques.

---

## Pipeline ETL

### 1. Extract

- Récupération des données depuis des sources publiques.
- Import des données au format CSV.
- Centralisation des données pour le traitement.

### 2. Transform

- Tri des données selon les dates, les pays et les indicateurs.
- Nettoyage des valeurs manquantes.
- Structuration des données.
- Calcul d'indicateurs utiles pour l'analyse.

### 3. Load

- Génération de fichiers CSV propres.
- Organisation des données selon les besoins des graphiques.
- Utilisation des fichiers par l'application web.

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
       structuration)
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

- de visualiser l'évolution mondiale du COVID-19 ;
- de comparer les pays selon plusieurs indicateurs ;
- d'analyser le lien entre vaccination et mortalité ;
- d'afficher des graphiques interactifs avec Chart.js.

---

## Productions réalisées

- Application web de data visualisation.
- Graphiques interactifs.
- Jeux de données structurés au format CSV.
- Pipeline ETL automatisé pour l'extraction, la transformation et le chargement des données.

---

## Structure du projet

```text
Projet-Dataviz

etl_covid.py

index.html
comparaison.html
evolution.html
vaccination.html
conclusion.html

utils.js
style.css

data/
└── transformed/
    └── fichiers CSV générés automatiquement
```

---

## Lancement du projet

### 1. Générer les fichiers CSV

```bash
python etl_covid.py
```

### 2. Lancer le site en local

```bash
python -m http.server 8000
```

### 3. Ouvrir le site

```text
http://localhost:8000
```

Les fichiers CSV ne sont pas stockés directement dans le dépôt GitHub. Ils sont générés automatiquement par le pipeline ETL.
