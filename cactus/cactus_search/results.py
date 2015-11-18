#-*- coding: utf-8 -*-
import sys

sys.path.insert(0, '/home/cedric/TP-WebSem/Test_Bonfante')
import main

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



def getResults(keywords):
    
    groups = main.searchOnTheWeb(keywords)
    list_results = []
    
    for gr in groups.keys():
        list_urls = []
        # groups[gr] represents the list of urls associated to key 'gr'
        for var in groups[gr]:
            #print("Test 1 : " + var)#ligne de test
            list_urls.append(var)
            
        list_results.append(Result(gr,list_urls))
        
    #print("Test 2 : " + str(list_results[0].title))#ligne de test
    #print("Test 3 : " + str(list_results[0].enriched_urls))#ligne de test


    #uri1="poke1"
    #uri2="poke2"
    #uri3="poke3"
    #uri4="poke4"
    #uri5="poke5"
    #url1=EnrichedURL("url1",[uri1,uri2,uri3])
    #url2=EnrichedURL("url2",[uri4,uri2,uri3])
    #url3=EnrichedURL("url3",[uri5,uri2,uri3])
    #urlstab1 = [url1,url2]
    #urlstab2 = [url2,url3]
    #gr1 = Result("Groupe 1",urlstab1)
    #gr2 = Result("Groupe 2",urlstab2)
    #list_results = [gr1,gr2]
    
    return list_results


# def getJson():
#     j = json.loads(test.json)
    
