class SaveSets:
    def __init__(self, exportLocation, data, connections):
        self.exportLocation = exportLocation
        self.data = data
        self.connections = connections
    def saveSet(self, set):
        with open(self.exportLocation, "w") as exportFile:
            exportFile.write(self.data)
            exportFile.write(self.connections)

        