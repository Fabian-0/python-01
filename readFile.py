import re

class ReadFile:

  def __init__(self, fileName):
    self.name = fileName

  def getFile(self):
    try:
      file = open(self.name)
      self.file = file
      return file
    except Exception:
      print('Input no valido')
      exit()
  
  def getWordsRepeat(self):
    wordsDict = {}
    for palabra in self.file:
      wordsDict[palabra] = wordsDict.get(palabra, 0) + 1 
    return wordsDict
  
  def getFirstReapetWords(self, wordsDict, numberOfWords = 10):
    auxList = []
    for key, value in wordsDict.items():
      auxList.append((value, key))
    toReturn = sorted(auxList, reverse=True)[:numberOfWords]
    return toReturn

  def cleanText(self, regularExpression = '[a-zA-Z0]+'):
    exp = re.compile(regularExpression)
    cleaned = exp.findall(self.file.read())
    self.file = cleaned
    return cleaned

  def printArray(self, toPrintArray):
    for i in range(len(toPrintArray)):
      print(f"{i+1}.- {toPrintArray[i]}")

text = input('introduzca el nombre del archivo >>> ')
createInstance = ReadFile(text)
createInstance.getFile()
createInstance.cleanText()
wordsRepeat = createInstance.getWordsRepeat()
firtsXWords = createInstance.getFirstReapetWords(wordsRepeat)
createInstance.printArray(firtsXWords)