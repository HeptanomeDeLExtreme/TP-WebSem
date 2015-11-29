from htmlReader import *
from enrichissement import *
from jaccard2 import *
import pickle

cache = {}
fileName = "cache.cache"
cacheSpot = {}
cacheURL = {}

def main():
	requete = raw_input("Entrez votre requete : ")
	print('')
	(searchOnTheWeb(requete))
	
def isInCache(requete):
	keys = cache.keys()
	if(requete in keys):
		print("Already in cache")
		return True
	return False
	
def isInCacheSpot(requete):
	keys = cacheSpot.keys()
	if(requete in keys):
		print("Already in cache")
		return True
	return False
	
def isInCacheUrl(requete):
	keys = cacheURL.keys()
	if(requete in keys):
		print("Already in cache")
		return True
	return False

def saveInFile():
	Fichier = open('data.txt','wb')
	pickle.dump(cache,Fichier)  
	Fichier.close()
	
def loadFromFile():
	Fichier = open('data.txt','rb')
	ret = pickle.load(Fichier)    
	Fichier.close()
	return ret
	
def saveInFileCache():
	FichierCache = open('cache.txt','wb')
	pickle.dump(cache,Fichier)  
	FichierCache.close()
	
def loadFromFileCache():
	FichierCache = open('cache.txt','rb')
	ret = pickle.load(Fichier)    
	FichierCache.close()
	return ret
	
def saveInFileURL():
	FichierURL = open('url.txt','wb')
	pickle.dump(cache,Fichier)  
	FichierURL.close()
	
def loadFromFileURL():
	FichierURL = open('url.txt','rb')
	ret = pickle.load(Fichier)    
	FichierURL.close()
	return ret
		
def searchOnTheWeb(requete,jaccard_index):
	global cache
	global cacheURL
	global cacheSpot
	
	try:
		cache = loadFromFile()
	except:
		print ('No cache data found.')	
	try:
		cacheSpot = loadFromFileSpot()
	except:
		print("No cache found for spolight")
	try:
		cacheURL = loadFromFileUrl()
	except:
		print("No cache found for url")
	
	# Tuple is the key of the cache
	tuple = (requete,jaccard_index)
		
	if(isInCache(tuple) == True):
		groupes = cache[tuple]
	else:
		url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
		
		if(isInCacheUrl(tuple) == True):
			html = cacheURL[tuple]
		else:
			print("Enregistrement des pages html ...")
			html = readHTML(url)
			print("Pages HTML enregistrees.")
			cacheURL[requete] = html
			print("URL Ajoutes au cache")
			
		print("Requete DBPedia SpotLight...")
		dictionnairePur = JSONParser(html)
		print("Requete effectuee.")
		
		if(isInCacheSpot(tuple) == True):
			dictionnaireEnrichi = spot[tuple]
		else:
			print("Enrichissement en cours ...")
			dictionnaireEnrichi = parcoursDict(dictionnairePur)
			print("Enrichissement effectue.")
			cacheSpot[requete] = dictionnaireEnrichi
			print("Dico enrichi ajoute au cache")
			
		print("Creation des groupes...") 
		graph, corres = genereFiltredGraphe2(dictionnaireEnrichi,jaccard_index)
		CC(graph)
		groupes = createGroups(graph,corres, dictionnaireEnrichi)
		print("Groupes crees.")	
		print("Ajout au cache...")
		cache[tuple] = groupes
		saveInFile()
		print("Ajoute au cache.")
		
	return groupes
	

