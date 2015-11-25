from SPARQLWrapper import SPARQLWrapper, JSON
import pickle

cachepays = {}
fileName = "cachepays.cachepays"

def isInCachePays(requete):
	keys = cachepays.keys()
	if(requete in keys):
		print("Already in cache")
		return True
	return False

def saveInFilePays():
	Fichier = open('datapays.txt','wb')
	pickle.dump(cachepays,Fichier)  
	Fichier.close()
	
def loadFromFilePays():
	Fichier = open('datapays.txt','rb')
	ret = pickle.load(Fichier)
	Fichier.close()
	return ret

def lancerRequetePays(motcle):
	global cachepays
	try:
		cachepays = loadFromFilepays()
	except:
		print ('No cache data found.')	
	if(isInCachePays(motcle) == True):
		dicFinal = cachepays[motcle]
	else:
		requete = genererrequete(motcle)
		sparql = SPARQLWrapper("http://dbpedia.org/sparql")
		sparql.setQuery(requete)
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		dicFinal = {}
		for result in results["results"]["bindings"]:
			predicat = result["p"]["value"]
			objet = result["o"]["value"]
			dicFinal[predicat] = objet
		print("Ajout pays au cache...")
		cachepays[motcle] = dicFinal
		saveInFilePays()
		print("Ajoute pays au cache.")
	
	return dicFinal

def genererrequete(motcle):
	requete = """
	SELECT ?p ?o
	WHERE { ?s ?p ?o. 
        ?s rdf:type <http://schema.org/Country>.
	FILTER(?s in (<http://dbpedia.org/resource/"""
	requete += motcle.title().replace(' ', '_')
	requete += """>))
        FILTER ((regex(?p, rdfs:label) && langMatches(lang(?o), "en"))  || 
	(regex(?p, rdfs:comment) && langMatches(lang(?o), "en")) || 
	regex(?p, <http://dbpedia.org/ontology/PopulatedPlace/areaTotal>) || 
	regex(?p, <http://xmlns.com/foaf/0.1/depiction>) || 
	regex(?p, <http://dbpedia.org/property/englishmotto>) || 
	(regex(?p, <http://dbpedia.org/property/languages>) && langMatches(lang(?o), "en")) ||
        regex(?p, <http://dbpedia.org/property/populationEstimate>) ||
        regex(?p, <http://dbpedia.org/property/capital>)
	)} """
	return requete
