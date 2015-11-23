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
	
def genereFiltredGraphe2(urls2,limite):
	fichier = open("graphe.dot, "w")
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
				index1 = correspondance[url1]
				index2 = correspondance[url2]
				liste[index1].addNode(index2)
				#~ Ajoute au noeud correspondant a url2 qu'il est lie a url1 
				liste[index2].addNode(index1)				
	return liste, correspondance
	
def genereFiltredGraphe(urls2,limite):
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
				fichier.write(url2+"--"+urls[url2]+";")
				index1 = correspondance[url1]
				index2 = correspondance[url2]
				liste[index1].addNode(index2)
				#~ Ajoute au noeud correspondant a url2 qu'il est lie a url1 
				liste[index2].addNode(index1)	
	fichier.write("}")			
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
	# Je trouve tout l'indice des successeurs de node
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
		#~ print("Connex Component number : "+str(i))
		temp = True
		for n in graph:
			if(n.getColor() == i):
				#~ print("Noeud : "+str(n.getName())+ ' '+findKeyForValues(c,n.getName()))
				#~ On ajoute l'url du noeud n dans la liste tempList
				tempList.append(findKeyForValues(c,n.getName()))
				temp = False
		if(temp == True):
			hasMoreConnexComponent = False
		else:
			#~ Recuperer l'uri qui apparait le plus souvent
			#~ L'uri qui apparait le plus souvent sera le nom du groupe
			moultUri = []
			dicoUri = {}
			#~ Parcourir tous les noeuds de la composante connexe pour
			#~ recuperer toutes les uris
			for oneUrl in tempList:
				#~ urls[findKeyForValues(c,n.getName())]
				#~ print "Url : " + oneUrl
				#~ print urls[oneUrl]
				moultUri += (urls[oneUrl])
			#~ Compter le nombre d'apparition de chaque uri
			for oneUri in moultUri:
				if oneUri in dicoUri:
					dicoUri[oneUri] += 1
				else:
					dicoUri[oneUri] = 1
			#~ print dicoUri
			cle, _ = max(dicoUri.iteritems(), key=lambda x:x[1])
			del dicoUri[cle]
			nomGroupe = cle[cle.rfind('/')+1:]
			meilleursURIs = []
			contenuGroupe = {x:[] for x in tempList}
			for i in xrange(5):
				cle, _ = max(dicoUri.iteritems(), key=lambda x:x[1])
				#print cle
				meilleursURIs.append(cle)
				del dicoUri[cle]
			#print meilleursURIs
			for oneUrl in tempList:
				for keyword in meilleursURIs:
				#print '***********************'
				#	print keyword, urls[oneUrl]
					if keyword in urls[oneUrl]:
						contenuGroupe[oneUrl]+= [keyword]

			#~ print "Cle = " + cle
			toRet[nomGroupe] = contenuGroupe
		i = i+1
	print '*****************groupes************'
	print toRet
	return toRet

def test():	
	urls = {}
	urls["url1"] = ["uri1","uri2"]
	urls["url2"] = ["uri1","uri3"]
	urls["url3"] = ["uri5","uri3"]
	urls["url4"] = ["uri9"]
	urls["url5"] = ["uri10"]
	g,c = genereFiltredGraphe(urls,0)
	CC(g)
	print createGroups(g,c, urls)

#~ test()
