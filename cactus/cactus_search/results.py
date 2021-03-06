#-*- coding: utf-8 -*-
import sys

sys.path.insert(0, '/home/nicolas/IF/COURS_4IF/WS/projet/gh2/TP-WebSem/backend')
import main
import film
import apropos
import htmlReader


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
def getResults(keywords,jaccard_index):
    
    groups = main.searchOnTheWeb(keywords,jaccard_index)
    list_results = []
    
    for gr in groups.keys():
        list_rich_urls = []
        # groups[gr] represents the list of urls associated to key 'gr'
        for rich_url in groups[gr]:
            list_uris = [htmlReader.getContent(rich_url)]
            list_rich_urls.append(EnrichedURL(rich_url,list_uris))
            
        list_results.append(Result(gr,list_rich_urls))

            
    return list_results


# Movies-related results
def getMovies(keywords):

    movies_results = film.lanceRequeteFilm(keywords)
    list_movies = []

    for m in movies_results.keys():
        list_movies.append(Movie(m.replace("_"," "),movies_results[m]))
    
    return list_movies


# Countries results
def getCountry(keywords):

    country_results = apropos.lancerRequetePays(keywords)
    list_infos = []

    # Default image, to avoid bug if it's not present in DBPedia
    img = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flags_onu_geneva2.jpg/1024px-Flags_onu_geneva2.jpg"
    
    # Loop on information prefixes
    for p in country_results:
        p_key=p[p.rfind('/')+1:]
        
        if p_key=="depiction":
            img = country_results[p]
        else:
            if notInBlackList(p_key):
                p_key = replaceInfoKeyword(p_key)
                list_infos.append(CountryInfo(p_key,country_results[p]))

    return list_infos, img

# Esthetic modifications for country-related results
def replaceInfoKeyword(p_key):

    if p_key == "rdf-schema#label":
        word = "Name"
    elif p_key == "areaTotal":
        word = "Total Area"
    elif p_key == "rdf-schema#comment":
        word = "Description"
    elif p_key == "populationEstimate":
        word = "Population"
    else:
        word = p_key.title()
    
    return word

# Infos we don't want to show
def notInBlackList(p_key):
    notInBL = True
    if ((p_key == "populationEstimateYear") or (p_key == "populationEstimateRank")  or (p_key == "languagesType")):
        notInBL = False

    return notInBL
