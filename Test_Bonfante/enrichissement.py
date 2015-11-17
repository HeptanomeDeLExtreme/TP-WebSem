from SPARQLWrapper import SPARQLWrapper, JSON

#~ dictionnaire = {}
#~ dictionnaire["http://mcgruff.org/"] = ["http://dbpedia.org/resource/Michelle_Obama"]

def parcoursDict(dic):
	dicFinal = {}
	for cle in dic:
		listeTemp = []
		for value in dic[cle]:
			listeTemp.append(value)
			listeTemp += lanceRequete(value)
		dicFinal[cle] = listeTemp		
	return dicFinal
			
def lanceRequete(uri):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	requete = creeRequete(uri)
	sparql.setQuery(requete)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	listeFinal = []
	for result in results["results"]["bindings"]:
		temp = (result["o"]["value"])
		listeFinal.append(temp)
	return listeFinal

# On trie pour recuperer les predicats qui ont la valeur
# urlType:type
# pour ne recuperer que des URI au niveau des objets retournes		
def creeRequete(uri):
	requete = """
PREFIX urlType: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX urlSeeAlso: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?s ?o 
WHERE { ?s ?p ?o. 
	FILTER(?s in ("""
	requete += '<'+uri+'>'
	requete += """))
	FILTER ( regex(?p, urlType:type) || regex(?p, urlSeeAlso:seeAlso) || regex(?p, <http://purl.org/dc/terms/subject>) )
      } 
LIMIT 100 """
	#~ print requete
	return requete

#~ print(lanceRequete("http://dbpedia.org/resource/Michelle_Obama"))
#~ print(parcoursDict(dictionnaire))
