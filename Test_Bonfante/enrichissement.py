from SPARQLWrapper import SPARQLWrapper, JSON

# Permet de créer la requête à envoyer à DBPedia pour un URI
def creerRequete(URI):
	query = "SELECT * WHERE { ?s ?p ?o. FILTER(?s in (" + URI + ")) } LIMIT 10"
	#print "Requete creee : " + query
	return query

# Permet pour chaque URI de créer la requête, de récupérer les résultats
# de cette requête sur DBPedia puis de compléter le tableau existant
# par de nouveaux URI
def traitementChaqueURI(tableauURI):
	for URI in tableauURI:
		query = creerRequete(URI)
		results = requete(query)
		creationResultat(results)
		
# Permet d'envoyer la requête sur DBPedia et d'obtenir un résultat
# (liste d'URI) en JSON
def requete(query):
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	return results

# Permet de modifier le tableau existant pour rajouter les URI
# nouvellement trouvés par l'enrichissement
# TODO : Modifier le tableau envoyé et rajouter pour chaque URI
# TODO : étudié, la liste d'URI associée
def creationResultat(tableauJSON):
	for result in tableauJSON["results"]["bindings"]:
		print("Resultat : " + result["o"]["value"])

tableauURI = ["<http://dbpedia.org/resource/Michelle_Obama>", "<http://dbpedia.org/resource/Michelle_Obama>"]
traitementChaqueURI(tableauURI)
