from SPARQLWrapper import SPARQLWrapper, JSON
import enrichissement

def apropos(motcle):
	motcle.replace(' ', '_')
	requete = genererrequete(motcle)
	sparql = SPARQLWrapper("http://dbpedia.org/sparql")
	sparql.setQuery(requete)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	dicFinal = {}
	for result in results["results"]["bindings"]:
		predicat = result["p"]["value"]
		objet = result["o"]["value"]
		dicFinal[predicat] = objet
	return dicFinal

def genererrequete(motcle):
	requete = """
	SELECT ?p ?o
	WHERE { ?s ?p ?o. 
        ?s rdf:type <http://schema.org/Country>.
	FILTER(?s in (<http://dbpedia.org/resource/"""
	requete += motcle
	requete += """>))
        FILTER ((regex(?p, rdfs:label) && langMatches(lang(?o), "en"))  || 
	(regex(?p, rdfs:comment) && langMatches(lang(?o), "en")) || 
	regex(?p, <http://dbpedia.org/ontology/PopulatedPlace/areaTotal>) || 
	regex(?p, <http://xmlns.com/foaf/0.1/depiction>) || 
	regex(?p, <http://dbpedia.org/ontology/areaTotal>) || 
	regex(?p, <http://dbpedia.org/property/areaKm>) || 
	regex(?p, <http://dbpedia.org/property/englishmotto>) || 
	(regex(?p, <http://dbpedia.org/property/languages>) && langMatches(lang(?o), "en"))
	)} 
	LIMIT 100"""
	return requete
