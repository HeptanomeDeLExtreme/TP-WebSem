class Noeud:
	
	def __init__(self,n):
		self.nom = n
		self.color = -1
		self.adjacent = []
	
	def getAdjacentNode(self):
		return self.adjacent
		
	def setAdjacentNode(self,nodes):
		self.adjacent = nodes
		
	def setColor(self,color):
		self.color = color

	def getColor(self):
		return self.color

	def addNode(self,i):
		self.adjacent.append(i)
		
	def getName(self):
		return self.nom
