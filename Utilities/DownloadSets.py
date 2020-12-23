class DownloadSets:
    def __init__(self, importLocation):
        self.importLocation = importLocation
    def importSet(self, name):
        with open(self.importLocation, "r") as f:
            fContents = f.read().split("-----")
            for x in range(len(fContents):
                currentSet = fContents[x]
                currentSet = currentSet.split("\n")
                if currentSet[0] == name:
                    return fContents[x]
        return "not found"