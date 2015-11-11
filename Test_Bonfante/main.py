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
	nbError = 0
	parsed_json = json.loads(htmlSource)
	for i in range(len(parsed_json['results'])):
		print(parsed_json['results'][i]['url'])
		#print(parsed_json['results'][i]['content'])
		try:
			annotateHTML(parsed_json['results'][i]['content'])
		except:
			nbError = nbError+1
			print('\tERROR\n')
	print("Nombre d'erreurs : "+str(nbError))

def annotateHTML(html):
	annotation = spotlight.annotate("http://spotlight.dbpedia.org/rest/annotate",html)
	for i in range(len(annotation)):
		print('\t'+annotation[i]['URI'])
	print('')

requete = raw_input("Entrez votre requete : ")
print('')
url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
html = readHTML(url)
JSONParser(html)
