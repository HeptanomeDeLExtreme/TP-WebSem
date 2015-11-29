import urllib
import json
import spotlight
import re
import string
from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import Tag


contentURL = {}

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


def getContent(url):
	return contentURL[url]


def JSONParser(htmlSource):
	dict = {}
	nbError = 0
	parsed_json = json.loads(htmlSource)

		
	#~ Tu recuperes la page html
	#~ tu prend les noeuds qui t'interesse
	#~ tu l'envoie
        
	nbURL = 10
	for i in range(nbURL):
                listeURI = []
		try:
			listeURI = annotateHTML(parsed_json['results'][i]['content'])
			contentURL[parsed_json['results'][i]['url']] = parsed_json['results'][i]['content']
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
	
	

