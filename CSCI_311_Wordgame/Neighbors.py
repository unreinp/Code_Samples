#Erin Hedlund and Peter Unrein
#CSCI 311
#Project Part 1

import sys
class Vertex():

	def __init__(self, key, handle):
		self.key = key
		self.handle = handle
		self.nextVertex = None
		self.weight = 0
	def addNeighbor(self,weight):
		temp = newV.nextVertex
		tempVal = newV.weight
		newV.nextVertex = Vertex(vertex.key, vertex.handle)
		newV.nextVertex.nextVertex = temp
		newV.nextVertex.weight = tempVal
		newV.weight = value
		temp = vertex.nextVertex
		tempVal = vertex.weight
		vertex.nextVertex = Vertex(newV.key, newV.handle)
		vertex.nextVertex.nextVertex = temp
		vertex.nextVertex.weight = tempVal
		vertex.weight = value
	def __repr__(self):
		if self.key == None:
			return 'String does not exist in graph'
   		return 'key: ' + str(self.getKey()) + '; handle: ' + str(self.getHandle())

	def getKey(self):
		return self.key

	def setHandle(self, inHandle):
		self.handle = inHandle

	def setKey(self, inInt):
		self.key = inInt

	def getHandle(self):
		return self.handle


def StringComp(str1,str2):

    elem1 = list(str1)
    elem2 = list(str2)
    count = 0
    value = -1

    for i in range(len(elem1)):
        if elem2[i] == elem1[i]:
            count += 1
    if count == 3:
        value = 5
    elif count == 4:
        value = 1
    else:
        value = -1
    return value


def main():
	if len(sys.argv) < 2:
		print ("please enter with a filename in terminal")
		sys.exit()
	inputfile = sys.argv[1]
	try:
		file = open(inputfile)
	except IOError:
		print("There was an error opening this file!")
		sys.exit()
	merryWebster = Graph()
	count = 0
	for line in file:
		linelist = line.split()
		for word in linelist:
			if (len(word) == 5):
				merryWebster.addVertex(word.upper(), count)
				count += 1
	file.close()
	while(1):
		s = raw_input('Enter a five-letter word: ')
   		found = merryWebster.search(s.upper())
   		if found != None:
   			merryWebster.printNeighbors(found)
   		else:
   			print("String does not exist in graph")
   		again = ''
   		while(again != 'N' and again != 'Y' and again != 'NO' and again != 'YES'):
   			again = raw_input('Would you like to enter another word? (Y/N): ')
   			again = again.upper()
   		if again == 'N' or again == 'NO':
   			break




class Graph():
	def __init__(self):
		self.vertices = []

	def addVertex(self, key, handle):
		newV = Vertex(key, handle)
		for vertex in self.vertices:
			value = StringComp(newV.key, vertex.key)
			if value > 0:
				temp = newV.nextVertex
				tempVal = newV.weight
				newV.nextVertex = Vertex(vertex.key, vertex.handle)
				newV.nextVertex.nextVertex = temp
				newV.nextVertex.weight = tempVal
				newV.weight = value
				temp = vertex.nextVertex
				tempVal = vertex.weight
				vertex.nextVertex = Vertex(newV.key, newV.handle)
				vertex.nextVertex.nextVertex = temp
				vertex.nextVertex.weight = tempVal
				vertex.weight = value
		self.vertices.append(newV)


	def search(self, key):
		for vertex in self.vertices:
			if key == vertex.key:
				return vertex
		return None

	def printNeighbors(self, v):
		print("The neighbors of " + str(v.key) + " are:")
		while v.nextVertex != None:
			print(str(v.nextVertex.key) + " (" + str(v.weight) + ")")
			v = v.nextVertex

main()
