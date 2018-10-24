import sys

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


def ConstructGraph():
   filename = sys.argv[1]
   file = open(filename)
   merryWebster = Graph()
 #  print(list(file))
   for line in file:
      print(line)
      linelist = line.split()
      for word in linelist:
          if (len(word) == 5):
            print(word.upper())
            merryWebster.add([word.upper()])
   print(merryWebster.words)
   file.close()
   return


class Graph():
    def __init__(self):
        self.words = []
    def add(self,word):
        self.words += word
ConstructGraph()
