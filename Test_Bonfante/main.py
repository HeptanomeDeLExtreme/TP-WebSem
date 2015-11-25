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
		
def searchOnTheWeb(requete):
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
		
		
	if(isInCache(requete) == True):
		groupes = cache[requete]
	else:
		url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
		
		if(isInCacheUrl(requete) == True):
			html = cacheURL[requete]
		else:
			print("Enregistrement des pages html ...")
			html = readHTML(url)
			print("Pages HTML enregistrees.")
			cacheURL[requete] = html
			print("URL Ajoutes au cache")
			
		print("Requete DBPedia SpotLight...")
		dictionnairePur = JSONParser(html)
		print("Requete effectuee.")
		
		if(isInCacheSpot(requete) == True):
			dictionnaireEnrichi = spot[requete]
		else:
			print("Enrichissement en cours ...")
			dictionnaireEnrichi = parcoursDict(dictionnairePur)
			print("Enrichissement effectue.")
			cacheSpot[requete] = dictionnaireEnrichi
			print("dico enrichi Ajoutes au cache")
			
		print("Creation des groupes...") 
		#~ groupes = genereGroupeTest(dictionnaireEnrichi,0.0)
		#~ groupes = generer_graphe(dictionnaireEnrichi)
		graph, corres = genereFiltredGraphe2(dictionnaireEnrichi,0.06)
		CC(graph)
		groupes = createGroups(graph,corres, dictionnaireEnrichi)
		print("Groupes crees.")	
		print("Ajout au cache...")
		cache[requete] = groupes
		saveInFile()
		print("Ajoute au cache.")
		
	return groupes
	

