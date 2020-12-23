class SaveSets:
    def __init__(self, exportLocation, data, connections, name):
        self.exportLocation = exportLocation
        self.data = data
        self.connections = connections
        self.name = name
    def saveSet(self):
        with open(self.exportLocation, "w") as exportFile:
            exportFile.write(self.name)
            exportFile.write(self.data)
            exportFile.write(self.connections)
            exportFile.write("-----")

        