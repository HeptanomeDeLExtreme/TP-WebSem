from SPARQLWrapper import SPARQLWrapper, JSON

dictionnaire = {}
dictionnaire["http://mcgruff.org/"] = ["http://dbpedia.org/resource/Monster_Jam","http://dbpedia.org/resource/1930s"]

def parcoursDict(dic):
	dicFinal = {}
	for cle in dic:
		listeTemp = []
		for value in dic[cle]:
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
		
def creeRequete(uri):
	requete = """
SELECT * 
WHERE { ?s ?p ?o. FILTER(?s in ("""
	requete += '<'+uri+'>'
	requete += """)) } 
LIMIT 10 """
	return requete

#~ print(lanceRequete("http://dbpedia.org/resource/Michelle_Obama"))
print(parcoursDict(dictionnaire))
