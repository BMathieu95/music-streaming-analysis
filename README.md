# Top 100 Musique — France & USA (1990 → présent)

Analyse de l’évolution de l’industrie musicale, avec focus sur le **Top 100 titres par décennie** et l’impact du **streaming** sur la consommation.

## Objectifs

-  Comparer les **Top 100 titres** France vs USA par décennie  
-  Simuler les **streams cumulés**  
-  Mesurer la **diversité des artistes** et la **concentration du marché (HHI)**  
-  Mettre en évidence la montée de la **longue traîne**  
-  Montrer les limites du modèle actuel basé sur quelques artistes dominants

##  Structure du projet

File_music_project/
│
├─ data/ # CSV sources
├─ exports/ # CSV générés par le notebook
├─ notebooks/ # Notebook principal
│ └─ top100_decennies_musique_fr_usa.ipynb
├─ scripts/ # Scripts Python (optionnel)
└─ README.md

##  Notebook

- Nettoyage et normalisation des données  
- Agrégation des streams par décennie et par pays  
- Visualisations : Top 20, longue traîne vs Top 10, HHI  
- Export CSV pour analyses ultérieures  

##  Installation rapide

```bash
git clone https://github.com/BMathieu95/music-streaming-analysis.git
pip install pandas numpy matplotlib
# Pour visualisations interactives
pip install plotly
## Usage
Ouvrir le notebook dans VS Code ou Jupyter

Exécuter toutes les cellules

Les exports apparaissent dans exports/

Remarques
Données simulées ou agrégées, pas de fichiers propriétaires

Conçu pour être agnostique de la source, avec colonnes clés : track_name, artist_name, date, streams, country

👤 Auteur
B. Mathieu — Projet personnel sur l’évolution de l’industrie musicale


---








