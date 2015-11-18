
def jaccard(liste1, liste2):
	set1, set2 = set(liste1), set(liste2)
	inter = set1.intersection(set2)
	return float(len(inter))/(len(liste1) + len(liste2)) #fuck python2


def generer_graphe(urls, limite):
	liste, liste_non_liees = [], []
	for url1 in urls.keys():
		uris = urls[url1]
		lien = False
		del urls[url1]
		for url2 in urls:
			indice = jaccard(uris, urls[url2])
			if indice >= limite:
				liste+= [{'url1':url1, 'url2':url2, 'indice':indice}]
				print(url1+' '+url2+' '+indice)
				if(not lien): lien = True
		if(not lien):
			liste_non_liees+= [url1]
	return liste, liste_non_liees

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
	
def generer_groupes(urls, limite):
	liste_urls, liste_urls_non_liees = generer_graphe(urls, limite)	
	groupes = []
	i = 0
	for triplet in liste_urls:
		uris = list(set(dict[triplet['url1']] + dict[triplet['url2']]))
		nom_groupe = 'groupe ' + str(i)
		i+= 1
		#for uri in uris:
		#   nom_groupe+= uri[uri.find['/':] + ' '
		groupes[nom_groupe] = uris

	uris = []
	for url in liste_urls_non_liees:
		uris += dict[url]
	uris = list(set(uris))
	nom_groupe = 'groupe bite'
	groupes[nom_groupe] = uris
	return groupes
