import urllib
import json
import spotlight
import re
import string
from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import Tag

##### DEBUT TEST NICO

NEGATIVE = re.compile(".*comment.*|.*meta.*|.*footer.*|.*foot.*|.*cloud.*|.*head.*")
POSITIVE = re.compile(".*post.*|.*hentry.*|.*entry.*|.*content.*|.*text.*|.*body.*")
BR = re.compile("<br */? *>[ \r\n]*<br */? *>")

##### FIN TEST NICO

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
	#~ print url
	return contentURL[url]


def JSONParser(htmlSource):
	dict = {}
	nbError = 0
	parsed_json = json.loads(htmlSource)
	#~ nbURL = len(parsed_json['results'])
	#~ for i in range(len(parsed_json['results'])):
		
	#~ Tu recuperes la page html
	#~ tu prend les noeuds qui t'interesse
	#~ tu l'envoie
        
	nbURL = 10
	for i in range(nbURL):
                listeURI = []
		try:
			##### DEBUT TEST NICO
                        # content must be the cleaned html page
                        # (currently it's the short description)
			listeURI = annotateHTML(parsed_json['results'][i]['content'])
			contentURL[parsed_json['results'][i]['url']] = parsed_json['results'][i]['content']
                        # url_to_exploit = parsed_json['results'][i]['url']
                        # print url_to_exploit
                        # clean_source = getAndCleanHTML(url_to_exploit)
                        # #print "Clean source"
                        # #print clean_source
                        # #print "Test pre-split"
                        # sentences = clean_source.split('\n')
                        # clean_sentences = cleanSentences(sentences)
                        
                        #print "Test sentences"
                        # for s in clean_sentences:
                        #         #print "I'm in the for loop"
                        #         print s
                        #         uris = annotateHTML(s)
                        #         listeURI.append(uris)
                        # listeURI = annotateHTML(clean_source)
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
        soup = BeautifulSoup(html,"lxml")

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
                text += '\n'.join(chunk for chunk in chunks if chunk)

        return text

# Remove empty lines from sentences list
def cleanSentences(sentences):
        #print "I shall clean sentences"
        ret = []
        for s in sentences:
                # empty strings are 'falsy'
                if s:
                        ret.append(s)
        return ret


# def getCleanSource(url):
#         html = urllib.urlopen(url).read()
#         #clean_source = extract_content_with_Arc90(html)
#         clean_source = BeautifulSoup(html,"lxml")
#         return clean_source


# def extract_content_with_Arc90(html):
 
#     soup = BeautifulSoup(re.sub(BR, "</p><p>", html),"lxml" )
#     soup = simplify_html_before(soup)
 
#     topParent = None
#     parents = []
#     for paragraph in soup.findAll("p"):
        
#         parent = paragraph.parent
        
#         if (parent not in parents):
#             parents.append(parent)
#             parent.score = 0
 
#             if (parent.has_key("class")):
#                 if (NEGATIVE.match(str(parent["class"]))):
#                     parent.score -= 50
#                 elif (POSITIVE.match(str(parent["class"]))):
#                     parent.score += 25
 
#             if (parent.has_key("id")):
#                 if (NEGATIVE.match(str(parent["id"]))):
#                     parent.score -= 50
#                 elif (POSITIVE.match(str(parent["id"]))):
#                     parent.score += 25
 
#         if (len( paragraph.renderContents() ) > 10):
#             parent.score += 1
 
#         # you can add more rules here!
 
#     topParent = max(parents, key=lambda x: x.score)
#     simplify_html_after(topParent)
#     return topParent.text
 
# def simplify_html_after(soup):
 
#     for element in soup.findAll(True):
#         element.attrs = {}    
#         if( len( element.renderContents().strip() ) == 0 ):
#             element.extract()
#     return soup
 
# def simplify_html_before(soup):
 
#     comments = soup.findAll(text=lambda text:isinstance(text, Comment))
#     [comment.extract() for comment in comments]
 
#     # you can add more rules here!
 
#     map(lambda x: x.replaceWith(x.text.strip()), soup.findAll("li"))    # tag to text
#     map(lambda x: x.replaceWith(x.text.strip()), soup.findAll("em"))    # tag to text
#     map(lambda x: x.replaceWith(x.text.strip()), soup.findAll("tt"))    # tag to text
#     map(lambda x: x.replaceWith(x.text.strip()), soup.findAll("b"))     # tag to text
    
#     replace_by_paragraph(soup, 'blockquote')
#     replace_by_paragraph(soup, 'quote')
 
#     map(lambda x: x.extract(), soup.findAll("code"))      # delete all
#     map(lambda x: x.extract(), soup.findAll("style"))     # delete all
#     map(lambda x: x.extract(), soup.findAll("script"))    # delete all
#     map(lambda x: x.extract(), soup.findAll("link"))      # delete all
    
#     delete_if_no_text(soup, "td")
#     delete_if_no_text(soup, "tr")
#     delete_if_no_text(soup, "div")
 
#     delete_by_min_size(soup, "td", 10, 2)
#     delete_by_min_size(soup, "tr", 10, 2)
#     delete_by_min_size(soup, "div", 10, 2)
#     delete_by_min_size(soup, "table", 10, 2)
#     delete_by_min_size(soup, "p", 50, 2)
 
#     return soup
 
# def delete_if_no_text(soup, tag):
    
#     for p in soup.findAll(tag):
#         if(len(p.renderContents().strip()) == 0):
#             p.extract()
 
# def delete_by_min_size(soup, tag, length, children):
    
#     for p in soup.findAll(tag):
#         if(len(p.text) < length and len(p) <= children):
#             p.extract()
 
# def replace_by_paragraph(soup, tag):
    
#     for t in soup.findAll(tag):
#         t.name = "p"
#         t.attrs = {}

##### FIN TEST NICO

#~ requete = raw_input("Entrez votre requete : ")
#~ print('')
#~ url = "https://searx.laquadrature.net/?q=["+requete+"]&format=json"
#~ html = readHTML(url)
#~ JSONParser(html)
