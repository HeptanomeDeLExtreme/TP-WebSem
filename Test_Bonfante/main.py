from htmlReader import *
from enrichissement import *
from jaccard2 import *
import pickle

cache = {}
fileName = "cache.cache"

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

def saveInFile():
	Fichier = open('data.txt','wb')
	pickle.dump(cache,Fichier)  
	Fichier.close()
	
def loadFromFile():
	Fichier = open('data.txt','rb')
	ret = pickle.load(Fichier)    
	Fichier.close()
	return ret
		
def searchOnTheWeb(requete):
	global cache
	try:
		cache = loadFromFile()
	except:
		print ('No cache data found.')	
	if(isInCache(requete) == True):
		groupes = cache[requete]
	else:
		url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
		print("Enregistrement des pages html ...")
		html = readHTML(url)
		print("Pages HTML enregistrees.")
		print("Requete DBPedia SpotLight...")
		dictionnairePur = JSONParser(html)
		print("Requete effectuee.")
		print("Enrichissement en cours ...")
		dictionnaireEnrichi = parcoursDict(dictionnairePur)
		print("Enrichissement effectue.")
		print("Creation des groupes...") 
		#~ groupes = genereGroupeTest(dictionnaireEnrichi,0.0)
		#~ groupes = generer_graphe(dictionnaireEnrichi)
		graph, corres = genereFiltredGraphe2(dictionnaireEnrichi,0.05)
		CC(graph)
		groupes = createGroups(graph,corres, dictionnaireEnrichi)
		print("Groupes crees.")	
		print("Ajout au cache...")
		cache[requete] = groupes
		saveInFile()
		print("Ajoute au cache.")
		
	return groupes
	

