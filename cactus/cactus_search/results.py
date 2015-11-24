#-*- coding: utf-8 -*-
import sys

sys.path.insert(0, '/home/nicolas/IF/COURS_4IF/WS/projet/gh2/TP-WebSem/Test_Bonfante')
import main
import film
import apropos


# Class representing a URL associated with a list of URI
class EnrichedURL:
    def __init__(self,url,uris):
        self.url = url
        # List of URIs
        self.uris = uris

# Class representing the structured results
class Result:
    def __init__(self,title,enriched_urls):
        self.title = title
        # List of enriched URLs
        self.enriched_urls = enriched_urls

# Class for movies-related results
class Movie:
    def __init__(self,title,content):
        self.title = title
        self.content = content

# Class for countries results
class CountryInfo:
    def __init__(self,prefix,info):
        self.prefix = prefix
        self.info = info


# Classic results
def getResults(keywords):
    
    groups = main.searchOnTheWeb(keywords)
    list_results = []
    
    for gr in groups.keys():
        list_rich_urls = []
        # groups[gr] represents the list of urls associated to key 'gr'
        for rich_url in groups[gr]:
            list_uris = []
            # groups[gr][rich_url] represents the list of uris assoc to key 'url'
            for uri in groups[gr][rich_url]:
                uri_key=uri[uri.rfind('/')+1:]
                list_uris.append(uri_key)
                
            list_rich_urls.append(EnrichedURL(rich_url,list_uris))
            
        list_results.append(Result(gr,list_rich_urls))

            
    return list_results


# Movies-related results
def getMovies(keywords):

    movies_results = film.lanceRequeteFilm(keywords)
    list_movies = []

    for m in movies_results.keys():
        list_movies.append(Movie(m,movies_results[m]))
    
    return list_movies


# Countries results
def getCountry(keywords):

    country_results = apropos.lancerRequetePays(keywords)
    list_infos = []

    # Loop on information prefixes
    for p in country_results:
        list_infos.append(CountryInfo(p,country_results[p]))

    print "Country "
    print list_infos
    return list_infos
