import urllib
import json
import spotlight

def readHTML(url):
	sock = urllib.urlopen(url)
	htmlSource = sock.read()
	sock.close()
	return htmlSource

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def processHTML(htmlContent):
	secondIndex= find_nth(htmlContent,'[',2)
	return htmlContent[(secondIndex+1):(len(htmlContent)-2)]

def JSONParser(htmlSource):
	dict = {}
	nbError = 0
	parsed_json = json.loads(htmlSource)
	for i in range(len(parsed_json['results'])):
	#for i in range(3):
		#print(parsed_json['results'][i]['url'])
		try:
			listeURI = annotateHTML(parsed_json['results'][i]['content'])
			dict[parsed_json['results'][i]['url']] = listeURI	
			#print(dict[parsed_json['results'][i]['url']])
		except:
			nbError = nbError+1
			#print('\tERROR\n')
	#print("Nombre d'erreurs : "+str(nbError))
	return dict

def annotateHTML(html):
	annotation = spotlight.annotate("http://spotlight.dbpedia.org/rest/annotate",html)
	listeURI = []
	for i in range(len(annotation)):
		listeURI += [annotation[i]['URI']]
	return listeURI

#~ requete = raw_input("Entrez votre requete : ")
#~ print('')
#~ url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
#~ html = readHTML(url)
#~ print JSONParser(html)
