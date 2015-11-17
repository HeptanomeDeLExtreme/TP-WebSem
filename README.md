#TP-WebSem
#CACTUS
« CACTUS Aggège Calmement Tout l'Univers Sémantique »

Basé sur les résultats du méta-moteur Searx, CACTUS interroge DBPedia. Le programme est réalisée en Python, et utilise le framework Django.

### Installation

**Pré-requis :** Python 2.7 (installé par défaut sur la plupart des distros grand public)

**Installation :**
 - Django : installer *pip*, puis exécuter `pip install Django==1.8.6`
 - Ouvrir le fichier *cactus/cactus/settings.py*
 - Modifier la ligne `STATICFILES_DIRS` avec votre chemin absolu local
 - Ouvrir un terminal à la racine *cactus/*
 - `python manage.py runserver`

Le résultat est disponible à l'adresse [localhost:8000/cactus_search/search](http://localhost:8000/cactus_search/search).
