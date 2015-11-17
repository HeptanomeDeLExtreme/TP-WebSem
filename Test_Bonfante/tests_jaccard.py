from jaccard2 import *

def test_jaccard():
	liste1=[];
	liste2=[]
	
	liste1.append ('http://dbpedia.org/resource/Category:Dog_breeds')
	liste1.append ('http://dbpedia.org/resource/Category:Dog_types')
	liste1.append('http://dbpedia.org/resource/Category:Dog_food')
	
	liste2.append('http://dbpedia.org/resource/Category:Dog_breeds')
	liste2.append('http://dbpedia.org/resource/Category:NaughtyDog')
	
	expectedResult = 0.25
	print('Resultat attendu =', expectedResult)
	
	result=jaccard(liste1,liste2)
	print('Resultat obtenu =', result)

def test_genererGraphe():
	urls = {}
	
	urls['DogsA'] = ['http://dbpedia.org/resource/Category:Dog_breeds',
			'http://dbpedia.org/resource/Category:Dog_types',
			'http://dbpedia.org/resource/Category:Dog_food']
	
	urls['DogsB'] = ['http://dbpedia.org/resource/Category:Dog_breeds',
			'http://dbpedia.org/resource/Category:NaughtyDog']
			
	print (generer_graphe(urls))

test_jaccard()
test_genererGraphe()
	
	
	

