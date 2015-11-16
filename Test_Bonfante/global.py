def main():
	requete = raw_input("Entrez votre requete : ")
	print('')
	url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
	html = readHTML(url)
	dictionnairePur = JSONParser(html)
	dictionnaireEnrichi = parcoursDict(dictionnaire) 

main()
