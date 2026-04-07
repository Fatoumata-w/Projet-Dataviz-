import pandas as pd
import numpy as np
import os


# =========================
# 1. EXTRACT
# =========================

url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
print("⏳ Téléchargement des données OWID...")
df = pd.read_csv(url, low_memory=False)
print(f"✅ Dataset chargé : {len(df)} lignes, {len(df.columns)} colonnes")
print("Colonnes disponibles :", df.columns.tolist())

# =========================
# 2. CLEAN
# =========================

# Détection dynamique de la colonne pays
if 'location' in df.columns:
    loc_col = 'location'
elif 'entity' in df.columns:
    loc_col = 'entity'
elif 'Country' in df.columns:
    loc_col = 'Country'
elif 'country' in df.columns:
    loc_col = 'country'
else:
    raise KeyError("Impossible de trouver une colonne correspondant au nom du pays (location/entity/Country/country).")

# Colonnes essentielles à garder si elles existent
needed_cols = {
    'location': loc_col,
    'continent': 'continent',
    'date': 'date',
    'population': 'population',
    'new_cases': 'new_cases',
    'new_deaths': 'new_deaths',
    'total_cases': 'total_cases',
    'total_deaths': 'total_deaths',
    'people_fully_vaccinated_per_hundred': 'people_fully_vaccinated_per_hundred',
    'code': 'code'
}

cols = [col for col in needed_cols.values() if col in df.columns]
df = df[cols].copy()

# Harmoniser le nom "location"
df = df.rename(columns={loc_col: 'location'})

# Conversion date en datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Supprimer lignes sans continent ou population
if 'continent' in df.columns:
    df = df[df['continent'].notna()]
df = df[df['population'].notna()]

# Remplacer NaN dans les compteurs par 0
for metric in ['new_cases','new_deaths','total_cases','total_deaths']:
    if metric in df.columns:
        df[metric] = df[metric].fillna(0)

print(f"✅ Après nettoyage : {df['location'].nunique()} entités, {df['date'].min().date()} → {df['date'].max().date()}")

# =========================
# 3. TRANSFORM
# =========================

# ──────────────────────────
# 3.1 evolution_mondiale.csv
# ──────────────────────────
evolution = (
    df.groupby('date')
    .agg(
        new_cases=('new_cases', 'sum'),
        new_deaths=('new_deaths', 'sum'),
        cumulative_cases=('total_cases', 'sum'),
        cumulative_deaths=('total_deaths', 'sum'),
    )
    .reset_index()
)

evolution = evolution[evolution['date'] <= '2023-12-31']
evolution['date'] = evolution['date'].dt.strftime('%Y-%m-%d')

# ──────────────────────────
# 3.2 stats_pays.csv
# ──────────────────────────
latest = df.sort_values('date').groupby('location').tail(1).copy()

# Mapping continent → WHO region
continent_to_who = {
    'Africa':        'AFRO',
    'Asia':          'SEARO',
    'Europe':        'EURO',
    'North America': 'AMRO',
    'South America': 'AMRO',
    'Oceania':       'WPRO',
}

if 'continent' in latest.columns:
    latest['WHO_region'] = latest['continent'].map(continent_to_who).fillna('OTHER')
else:
    latest['WHO_region'] = 'OTHER'

# Calculs sécurisés
latest['deaths_per_million'] = (latest['total_deaths'] / latest['population'] * 1e6).round(2)
latest['cases_per_million'] = (latest['total_cases'] / latest['population'] * 1e6).round(2)
latest['mortality_rate'] = (
    (latest['total_deaths'] / latest['total_cases'].replace(0, np.nan) * 100)
    .fillna(0)
    .round(2)
)

stats_pays = latest[[
    'location', 'WHO_region',
    'deaths_per_million', 'cases_per_million', 'mortality_rate'
]].rename(columns={'location': 'Country'})

# ──────────────────────────
# 3.3 stats_continents.csv
# ──────────────────────────
if 'continent' in latest.columns:
    stats_continents = (
        latest.groupby('continent')
        .agg(
            total_cases=('total_cases', 'sum'),
            total_deaths=('total_deaths', 'sum'),
        )
        .reset_index()
    )

    stats_continents['continent'] = stats_continents['continent'].map(continent_to_who).fillna('OTHER')

    stats_continents = (
        stats_continents.groupby('continent')
        .agg(total_cases=('total_cases', 'sum'), total_deaths=('total_deaths', 'sum'))
        .reset_index()
    )
else:
    stats_continents = pd.DataFrame()

# ──────────────────────────
# 3.4 vaccination.csv
# ──────────────────────────
vaccination = pd.DataFrame()
if 'people_fully_vaccinated_per_hundred' in df.columns:
    vacc_max = (
        df.groupby('location')['people_fully_vaccinated_per_hundred']
        .max()
        .reset_index()
    )

    vaccination = latest[['location','population','total_deaths']].merge(
        vacc_max, on='location', how='left'
    )

    vaccination['total_deaths_per_million'] = (vaccination['total_deaths'] / vaccination['population'] * 1e6).round(2)

    vaccination = vaccination[[
        'location',
        'people_fully_vaccinated_per_hundred',
        'total_deaths_per_million'
    ]].rename(columns={'location': 'country'})

# Supprimer les pays sans données de vaccination
vaccination = vaccination[vaccination['people_fully_vaccinated_per_hundred'].notna()]

# =========================
# 4. LOAD
# =========================
os.makedirs("data/transformed", exist_ok=True)

evolution.to_csv("data/transformed/evolution_mondiale.csv", index=False)
stats_pays.to_csv("data/transformed/stats_pays.csv", index=False)
stats_continents.to_csv("data/transformed/stats_continents.csv", index=False)
vaccination.to_csv("data/transformed/vaccination.csv", index=False)

print("\nETL terminé avec succès !")
print(f"   evolution_mondiale.csv : {len(evolution)} lignes")
print(f"   stats_pays.csv         : {len(stats_pays)} pays")
print(f"   stats_continents.csv   : {len(stats_continents)} continents")
print(f"   vaccination.csv        : {len(vaccination)} pays")
print("\n Fichiers dans : data/transformed/")