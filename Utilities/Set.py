from SaveSets import SaveSets
class Set:
    def __init__(self, setName):
        self.setName = setName
        self.data = []
        self.connections = []
        self.connectionInitialized = False
    def initializeData(self):
        self.vocabInput = 0
        while self.vocabInput != '9999':
            self.vocabInput = input('Please enter the next vocab word. If you want to stop entering in words type 9999 instead\n')
            if self.vocabInput != '9999':
                self.addWord(self.vocabInput)
                self.connectionInput = input("Do you want a connection for this vocab word? Something like a laptop is the computer that is portable because of 'lap'. These help you quickly remember words. If not, type 999\n")
                if self.connectionInput != '999':
                    if self.connectionInitialized == False:
                        self.initializeConnections()
                    self.addConnection(self.vocabInput, self.connectionInput)
        self.saveBool = input("Do you want to save this set? If not it will only last until you close thise program. y/n \n")     
        if self.saveBool == "y":
            self.saver = SaveSets("C:\Code\Python\Mem-O-Rise\Data\Sets.txt", self.getData(), self.getConnections())  
            self.saver.saveSet()

    def getData(self):
        return self.data

    def getConnections(self):
        return self.connections

    def addWord(self, word):
        self.data.append(word)

    def initializeConnections(self):
        self.dataLength = len(self.data)
        self.connections = [0 for x in range(self.dataLength)]
        self.connectionInitialized = True   

    def addConnection(self, word, connection):
        index = self.data.index(word)
        self.connections[index] = connection
