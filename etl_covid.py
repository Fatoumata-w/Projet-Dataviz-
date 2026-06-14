import os
import pandas as pd

# ======================================
# ETL COVID-19
# Extract -> Transform -> Load
# ======================================

# Source Open Data : Our World In Data
URL = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
DOSSIER_SORTIE = "data/transformed"

print("Téléchargement des données...")

# EXTRACT : on récupère le CSV en ligne
df = pd.read_csv(URL)

# TRANSFORM : on garde seulement les colonnes utiles pour le site
colonnes = [
    "country",
    "date",
    "continent",
    "population",
    "new_cases",
    "new_deaths",
    "total_cases",
    "total_deaths",
    "people_fully_vaccinated_per_hundred"
]

df = df[colonnes]

# On garde le même nom de colonne que dans le site
df = df.rename(columns={"country": "location"})

# Nettoyage simple
df["date"] = pd.to_datetime(df["date"])
df = df.dropna(subset=["location", "date", "population"])

# Les valeurs vides sont remplacées par 0 pour éviter les erreurs de calcul
for col in ["new_cases", "new_deaths", "total_cases", "total_deaths"]:
    df[col] = df[col].fillna(0)

# On enlève les lignes qui ne correspondent pas à un pays réel
df = df[df["continent"].notna()]

# La vaccination n'est pas remplie tous les jours dans le fichier OWID.
# On reprend donc la dernière valeur connue pour chaque pays.
df = df.sort_values(["location", "date"])
df["people_fully_vaccinated_per_hundred"] = (
    df.groupby("location")["people_fully_vaccinated_per_hundred"].ffill()
)

# Création du dossier de sortie
os.makedirs(DOSSIER_SORTIE, exist_ok=True)


# ======================================
# 1. Evolution mondiale
# ======================================

evolution = df.groupby("date", as_index=False).agg({
    "new_cases": "sum",
    "new_deaths": "sum",
    "total_cases": "sum",
    "total_deaths": "sum"
})

# Le site utilise ces noms de colonnes
evolution = evolution.rename(columns={
    "total_cases": "cumulative_cases",
    "total_deaths": "cumulative_deaths"
})

evolution["date"] = evolution["date"].dt.strftime("%Y-%m-%d")
evolution.to_csv(f"{DOSSIER_SORTIE}/evolution_mondiale.csv", index=False)


# ======================================
# 2. Statistique par pays
# ======================================

# On prend la dernière ligne disponible pour chaque pays
latest = df.sort_values("date").groupby("location").tail(1).copy()

# Regroupement simple des continents en zones OMS
regions = {
    "Africa": "AFRO",
    "Europe": "EURO",
    "Asia": "SEARO",
    "North America": "AMRO",
    "South America": "AMRO",
    "Oceania": "WPRO"
}

latest["WHO_region"] = latest["continent"].map(regions).fillna("OTHER")
latest["deaths_per_million"] = (latest["total_deaths"] / latest["population"] * 1_000_000).round(2)
latest["cases_per_million"] = (latest["total_cases"] / latest["population"] * 1_000_000).round(2)
latest["mortality_rate"] = (latest["total_deaths"] / latest["total_cases"].replace(0, pd.NA) * 100).fillna(0).round(2)

stats_pays = latest[[
    "location",
    "WHO_region",
    "deaths_per_million",
    "cases_per_million",
    "mortality_rate"
]].rename(columns={"location": "Country"})

stats_pays.to_csv(f"{DOSSIER_SORTIE}/stats_pays.csv", index=False)


# ======================================
# 3. Vaccination
# ======================================

vaccination = latest[[
    "location",
    "people_fully_vaccinated_per_hundred",
    "deaths_per_million"
]].copy()

vaccination = vaccination.rename(columns={
    "location": "country",
    "deaths_per_million": "total_deaths_per_million"
})

vaccination = vaccination.dropna(subset=["people_fully_vaccinated_per_hundred"])
vaccination.to_csv(f"{DOSSIER_SORTIE}/vaccination.csv", index=False)


# ======================================
# 4. Statistiques par continent
# ======================================

stats_continents = latest.groupby("WHO_region", as_index=False).agg({
    "total_cases": "sum",
    "total_deaths": "sum"
})

stats_continents = stats_continents.rename(columns={"WHO_region": "continent"})
stats_continents.to_csv(f"{DOSSIER_SORTIE}/stats_continents.csv", index=False)

print("ETL terminé.")
print("Les fichiers CSV ont été créés dans data/transformed/")
