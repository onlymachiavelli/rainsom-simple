import os 

def getCurrentDir():
    return os.getcwd()

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    textOnly = [f for f in allFiles if f.endswith('.txt')]

    print("List of files : " , textOnly)
    return textOnly

def readFile(filePath):
    with open(filePath, 'r') as file:
        data = file.read()
    return data

def deleteFile(filePath):
    os.remove(filePath)

def createFileAndWrite(filePath, data , crypted = True):
    filePath = filePath.split(".")[0] + "_crypted.txt" if crypted else filePath.split(".")[0] + "_decrypted.txt"
   
   
    with open(filePath, 'w') as file:
        file.write(data)