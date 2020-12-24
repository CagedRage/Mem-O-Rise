from SaveSets import SaveSets
#TODO: learn set has to take 3 at a time


class Set:
    def __init__(self, setName):
        self.setName = setName
        self.data = []
        self.connections = []
        self.connectionInitialized = False
        self.mastery = [0 for x in range(self.dataLength)]
        #self.masateryBool = False
        self.masteryOrdered = []

    def initializeData(self):
        self.vocabInput = 0
        while self.vocabInput != '9999':
            self.vocabInput = input('Please enter the next vocab word. If you want to stop entering in words type 9999 instead\n')
            if self.vocabInput != '9999':
                definition = self.getDefinition()
                self.addWord(self.vocabInput, definition)
                self.connectionInput = input("Do you want a connection for this vocab word? Something like a laptop is the computer that is portable because of 'lap'. These help you quickly remember words. If not, type 999\n")
                if self.connectionInput != '999':
                    if self.connectionInitialized == False:
                        self.initializeConnections()
                    self.addConnection(self.vocabInput, self.connectionInput)
        self.saveBool = input("Do you want to save this set? If not it will only last until you close thise program. y/n \n")     
        if self.saveBool == "y":
            saver = SaveSets("C:\Code\Python\Mem-O-Rise\Data\Sets.txt", self.getData(), self.getConnections(), self.setName)  
            saver.saveSet()

    def teachWord(self, word, word2, word3):
        wordIndex = self.data.index(word)
        masteryForWord = self.mastery[wordIndex]

        wordIndex2 = self.data.index(word2)
        masteryForWord2 = self.mastery[wordIndex2]

        wordIndex3 = self.data.index(word3)
        masteryForWord3 = self.mastery[wordIndex3]s

        averageMastery = (masteryForWord + masteryForWord2 + masteryForWord3) / 3
        if averageMastery < 10:
            self.writeVocabWord(word)
            self.writeVocabWord(word2)
            self.writeVocabWord(word3)

            self.mastery[wordIndex] += 5

    def getData(self):
        return self.data

    def getDefinition(self):
        definition = input("Enter the definition for this vocab word\n")
        return definition
    def getConnections(self):
        return self.connections

    def addWord(self, word, definition):
        newWord = word + "," + definition
        self.data.append(newWord)

    def initializeConnections(self):
        self.dataLength = len(self.data)
        self.connections = [0 for x in range(self.dataLength)]
        self.connectionInitialized = True   

    def orderByMastery(self):
        self.masteryOrdered = [x for _,x in sorted(zip(self.mastery, self.data))]

    def addConnection(self, word, connection):
        index = self.data.index(word)
        self.connections[index] = connection

    def learnSet(self):
        for vocabWord in self.masteryOrdered:  #TODO; Make this range so u can take 3 at a time
            self.teachWord(vocabWord)
    
    def writeVocabWord(self, word):
        timesWordWritten = 0
        while timesWordWritten <= 5:
            wordInput = input(f"please enter {word} 5 times. You have written it {timesWordWritten} amount of time\ns")
            if wordInput == word:
                timesWordWritten += 1

    def testConnections(self, word, word2, word3):
        wordIndex = self.data.index(word)
        word2Index = self.data.index(word2)
        word3Index = self.data.index(word3)
        print("Now you will review connections, which will help you remember your words. Connections make it much more efficient and easier to use\n")
        print(f"As a reminder, here are the connections for your words {word}: {self.connections[wordIndex]}, {word2}: {self.connections[word2Index]}, {word3}: {self.connections[word3Index]})
    
        
