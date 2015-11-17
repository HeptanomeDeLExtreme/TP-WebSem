def jaccard(liste1, liste2):
	set1, set2 = set(liste1), set(liste2)
	inter = set1.intersection(set2)
	return float(len(inter))/(len(liste1) + len(liste2)) #fuck python2


def generer_graphe(urls, limite):
	liste= []
	for url1 in urls.keys():
		uris = urls[url1]
		
		del urls[url1]
		for url2 in urls:
			indice = jaccard(uris, urls[url2])
			liste+= [{'url1':url1, 'url2':url2, 'indice':indice}]
				
		
	return liste
