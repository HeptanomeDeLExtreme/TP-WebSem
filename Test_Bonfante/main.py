from htmlReader import *
from enrichissement import *
from jaccard import *

def main():
	requete = raw_input("Entrez votre requete : ")
	print('')
	url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
	print("Enregistrement de la page html ...")
	html = readHTML(url)
	print("Page HTML enregistree.")
	print("Requete DBPedia SpotLight...")
	dictionnairePur = JSONParser(html)
	print("Requete effectuee.")
	print("Enrichissement en cours ...")
	dictionnaireEnrichi = parcoursDict(dictionnairePur)
	print("Enrichissement effectue.")
	print("Creation des groupes...") 
	groupes = generer_groupes(dictionnaireEnrichi,0.1)
	print("Groupes crees.")	
	print(groupes)

main()
