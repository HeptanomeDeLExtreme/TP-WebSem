import urllib
import json
import spotlight
from bs4 import BeautifulSoup

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
	#~ nbURL = len(parsed_json['results'])
	#~ for i in range(len(parsed_json['results'])):
		
	#~ Tu recuperes la page html
	#~ tu prend les noeuds qui t'interesse
	#~ tu l'envoie
	 
	nbURL = 6
	for i in range(nbURL):
		try:
			##### DEBUT TEST NICO
                        # content must be the cleaned html page (cur it's the descr)
			listeURI = annotateHTML(parsed_json['results'][i]['content'])
                        #~ url_to_exploit = parsed_json['results'][i]['url']
                        #~ listeURI = annotateHTML(getAndCleanHTML(url_to_exploit))
                        ##### FIN TEST NICO
			#~ print(parsed_json['results'][i]['url'])
			#~ print(parsed_json['results'][i]['content'])
			dict[parsed_json['results'][i]['url']] = listeURI	
		except:
			nbError = nbError+1
	print("\tNombre d'URL : "+str(nbURL))
	print("\tNombre d'erreurs : "+str(nbError))
	return dict

def annotateHTML(html):
	annotation = spotlight.annotate("http://spotlight.dbpedia.org/rest/annotate",html)
	listeURI = []
	for i in range(len(annotation)):
		listeURI += [annotation[i]['URI']]
	return listeURI
	
	
##### DEBUT TEST NICO

def getAndCleanHTML(url):
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)

        # kill all script and style elements
        for script in soup(["script", "style"]):
                script.extract()    # rip it out
                
                # get text
                text = soup.get_text()
                
                # break into lines and remove leading and trailing space on each
                lines = (line.strip() for line in text.splitlines())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
                text = '\n'.join(chunk for chunk in chunks if chunk)

                return text

##### FIN TEST NICO

#~ requete = raw_input("Entrez votre requete : ")
#~ print('')
#~ url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
#~ html = readHTML(url)
#~ JSONParser(html)
