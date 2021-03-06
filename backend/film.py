from SPARQLWrapper import SPARQLWrapper, JSON
import pickle		

cachefilm = {}
fileName = "cachefilm.cachefilm"

def isInCacheFilm(requete):
	keys = cachefilm.keys()
	if(requete in keys):
		print("Already in cache")
		return True
	return False

def saveInFileFilm():
	Fichier = open('datafilm.txt','wb')
	pickle.dump(cachefilm,Fichier)  
	Fichier.close()
	
def loadFromFileFilm():
	Fichier = open('datafilm.txt','rb')
	ret = pickle.load(Fichier)
	Fichier.close()
	return ret
	
def lanceRequeteFilm(motCle):
	global cachefilm
	try:
		cachefilm = loadFromFileFilm()
	except:
		print ('No cache data found.')	
	if(isInCacheFilm(motCle) == True):
		dic = cachefilm[motCle]
	else:
		sparql = SPARQLWrapper("http://dbpedia.org/sparql")
		requete = creeRequeteFilm(motCle)
		sparql.setQuery(requete)
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		dic = {}
		for result in results["results"]["bindings"]:
			temp = (result["film_title"]["value"])
			temp2 = (result["film_abstract"]["value"])
			lastIndex = temp.rfind("/")+1
			cle = temp[lastIndex:]
			dic[cle] = temp2
		print("Ajout film au cache...")
		cachefilm[motCle] = dic
		saveInFileFilm()
		print("Ajoute film au cache.")
	return dic

# On trie pour recuperer les predicats qui ont la valeur
# urlType:type
# pour ne recuperer que des URI au niveau des objets retournes		
def creeRequeteFilm(motCle):
	requete = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?film_title ?film_abstract
WHERE {
?film_title rdf:type <http://dbpedia.org/ontology/Film> .
?film_title rdfs:comment ?film_abstract 
FILTER regex(str(?film_title), \""""+motCle.title()+"""\").
 FILTER (langMatches(lang(?film_abstract),"en")) 
} LIMIT 3
"""	
	return requete
