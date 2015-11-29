#TP-WebSem
TP Web Sémantique - 4IF Insa Lyon  
\#H4203 \#2015
#CACTUS
« CACTUS Agrège Calmement Tout l'Univers Sémantique »

Basé sur les résultats du méta-moteur Searx, CACTUS interroge DBPedia. Le programme est réalisée en Python, et utilise le framework Django.

### Installation

**Pré-requis :** 
 - Python 2.7 (installé par défaut sur la plupart des distros grand public)
 - Django : `pip install Django==1.8.6`


**Mise en route :**
 - Ouvrir le fichier *cactus/cactus/settings.py*
 - Modifier la ligne `STATICFILES_DIRS` avec votre chemin absolu local
 - Dans *cactus/cactus_search/results.py* : remplacer le 1er chemin d'accès par le vôtre
 - Ouvrir un terminal à la racine *cactus/*
 - `python manage.py runserver`

Le résultat est disponible à l'adresse [localhost:8000/cactus_search/search](http://localhost:8000/cactus_search/search).
