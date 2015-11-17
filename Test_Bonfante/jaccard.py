'''
calcul de l'indice de jaccard et générations des liens entre URLs
Cedric + Charles
'''

'''
calcule l'indice de jaccard entre deux liste d'urls
'''
def jaccard(liste1, liste2):
	set1, set2 = set(liste1), set(liste2)
	inter = set1.intersection(set2)
	return inter/(len(liste1) + len(liste2))

'''
génère les liens entre des URLs
entrée : dictionnaire des URLs, seuil à parrtir duquel les URLs sont liées
sortie : liste de triplets {url, url, indice}, liste
'''
def graphe_jaccard(urls, limite):
	liste, liste_non_liees = [], []
	for item1 in urls:
		uris = urls[item1]
		lien = False
		del urls[item1]
		graphe[url] = []
		for item2 in urls:
			indice = jaccard(uris, url[item2])
			if indice >= limite:
				liste+= {'url1':item1, 'url2':item2, 'indice':indice}
				if(!lien): lien = True
		if(!lien):
			liste_non_liees+= [item1]
	return liste, liste_non_liees

def groupe_jaccard(dict, limite):
	liste_urls, liste_urls_non_liees = graphe_jaccard(dict, limite)
	groupes = []
	i = 0
	for triplet in liste:
		uris = list(set(dict[triplet['url1'] + dict[triplet ['url2']]))
		nom_groupe = 'groupe ' + i
		i+= 1
		#for uri in uris:
		#	nom_groupe+= uri[uri.find['/':] + ' '
		groupes+= {'nomGroupe' : nom_groupe, 'listeURL' : uris}

	uris = []
	for url in liste_urls_non_liees:
		uris += dict[url]
	uris = list(set(uris))
	nom_groupe = 'groupe bite'
	groupes+= {'nomGroupe' : nom_groupe, 'listeURL' : uris}
	return groupes
