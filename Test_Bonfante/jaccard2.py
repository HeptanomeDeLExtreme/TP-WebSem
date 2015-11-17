from Noeud import *

def jaccard(liste1, liste2):
	set1, set2 = set(liste1), set(liste2)
	inter = set1.intersection(set2)
	return float(len(inter))/(len(liste1) + len(liste2)-len(inter)) #fuck python2


def generer_graphe(urls):
	liste= []
	for url1 in urls.keys():
		uris = urls[url1]
		del urls[url1]
		for url2 in urls:
			indice = jaccard(uris, urls[url2])
			liste+= [{'url1':url1, 'url2':url2, 'indice':indice}]
			print(str(url1) +" "+str(url2)+" "+str(indice))
	return liste

def genereGroupeTest(urls,limite):
	liste_urls, liste_urls_non_liees = generer_graphe(urls, limite)	
	toRet = {}
	listeToRet = []
	for url in liste_urls:
		url1 = url['url1']
		url2 = url['url2']
		listeToRet.append(url1)
		listeToRet.append(url2)
	listeToRet += liste_urls_non_liees
	toRet["Un"] = listeToRet
	return toRet
	
def genereFiltredGraphe(urls,limite):
	#~ Cree un dict de correspondance entre l'indice du noeud
	#~ et l'url associe
	correspondance = {}
	key = urls.keys()
	i=0
	correspondance[key[0]] = i
	for url in urls[key[0]]:
		correspondance[url] = i
		i = i+1 
	
	#~ Instancie la liste de Noeud
	liste = []
	for j in range(i):
		temp = Noeud(i)
		liste.append(temp)
	 
	for url1 in urls.keys():
		uris = urls[url1]
		del urls[url1]
		for url2 in urls:
			indice = jaccard(uris, urls[url2])
			if(indice>limite):
				#~ Ajoute au noeud correspondant a url1 qu'il est lie a url2
				index1 = correspondance[url1]
				index2 = correspondance[url1]
				liste[index1].addNode(index2)
				#~ Ajoute au noeud correspondant a url2 qu'il est lie a url1 
				liste[index2].addNode(index1)				
	return liste

urls = {}
urls["url1"] = ["uri1","uri2"]
urls["url2"] = ["uri1","uri3"]
g = genereFiltredGraphe(urls,0)
for n in 
