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

def createFileAndWrite(filePath, data):
    filePath = filePath.split(".")[0] + "_crypted.txt"
   
   
    with open(filePath, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    

    option = ""
    print("""

          1 - encrypt all the files 
          2 - decrypt all the files
          3 - crypt one file by id

    """)


    option = input("Enter your option: ")

    match option:

        case "1":
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)

            for file in listOfFiles:
                data = readFile(file)
                cryptedData = data 
                print("crypted data : " , cryptedData)
                createFileAndWrite(file, data)
                deleteFile(file)

        case "2" : 
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            for file in listOfFiles:
                data = readFile(file)
                createFileAndWrite(file, data)
                deleteFile(file)

        case "3":
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            fileId = input("Enter the file id : which is the number of the file in ")
            targetFile = listOfFiles[int(fileId)]
            data = readFile(targetFile)
            uncryptedData = data
            createFileAndWrite(targetFile, data)
            deleteFile(targetFile)