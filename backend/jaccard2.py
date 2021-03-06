from Noeud import *

def jaccard(liste1, liste2):
	set1, set2 = set(liste1), set(liste2)
	inter = set1.intersection(set2)
	return float(len(inter))/(len(liste1) + len(liste2)-len(inter))


def generer_graphe(urls):
	liste= []
	for url1 in urls.keys():
		uris = urls[url1]
		del urls[url1]
		for url2 in urls:
			indice = jaccard(uris, urls[url2])
			liste+= [{'url1':url1, 'url2':url2, 'indice':indice}]
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
	
def genereFiltredGraphe2(urls2,limite):
	fichier = open("graphe.dot", "w")
	fichier.write("graph mon_graphe {")
	urls = urls2.copy()
	#~ Cree un dict de correspondance entre l'indice du noeud
	#~ et l'url associe
	correspondance = {}
	key = urls.keys()
	i=0
	for url in key:
		correspondance[key[i]] = i
		i = i+1 
	
	#~ Instancie la liste de Noeud
	liste = []
	for j in range(i):
		temp = Noeud(j)
		liste.append(temp)
	 
	for url1 in urls.keys():
		uris = urls[url1]
		del urls[url1]
		for url2 in urls:
			indice = jaccard(uris, urls[url2])
			if(indice>limite):
				#~ Ajoute au noeud correspondant a url1 qu'il est lie a url2
				fichier.write(str(url2)+"--"+str(url1)+";\n")
				index1 = correspondance[url1]
				index2 = correspondance[url2]
				liste[index1].addNode(index2)
				#~ Ajoute au noeud correspondant a url2 qu'il est lie a url1 
				liste[index2].addNode(index1)	
	fichier.write("}")	
	fichier.close()					
	return liste, correspondance
	


def findKeyForValues(dic,val):
	for e in dic.keys():
		if(dic[e]==val):
			return e
	return -1

def lastUncoloredNode(graph):
	for i in range(0,len(graph)):
		if(graph[i].getColor() == -1):
			return i
	return -1
			
	
def CC_Sommet(graph,node,color):
	#~ Je colorie node en color 
	graph[node].setColor(color)
	#~ Je trouve tout l'indice des successeurs de node
	succInt = graph[node].getAdjacentNode()
	#~ Parcours tout les succ y de node 
	for y in succInt:
		#~ si y n'est pas colore
		if(graph[y].getColor() == -1):
			CC_Sommet(graph,y,color) 
	

def CC(graph):
	color = -1
	#~ tant que tout les sommets ne sont pas colories 
	while(lastUncoloredNode(graph) != -1):
		#~ choisir un noeud parmi les non-colories 
		last = lastUncoloredNode(graph)
		#~ choisir une nouvelle couleur 
		color = color + 1
		CC_Sommet(graph,last,color)

def printGraph(graph):
	for n in graph:
		print("Noeud : "+str(n.getName())+ ' '+findKeyForValues(c,n.getName()))
		print("Color : "+str(n.getColor()))
		
def createGroups(graph,c, urls):
	toRet = {}
	hasMoreConnexComponent = True
	temp = True
	i = 0
	while(hasMoreConnexComponent):
		tempList = []
		temp = True
		for n in graph:
			if(n.getColor() == i):
				#~ On ajoute l'url du noeud n dans la liste tempList
				tempList.append(findKeyForValues(c,n.getName()))
				temp = False
		if(temp == True):
			hasMoreConnexComponent = False
		else:
			toRet["Group "+str(i)] = tempList
		i = i+1

	return toRet

