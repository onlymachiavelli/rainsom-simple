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
    return textOnly

def readFile(filePath):
    with open(filePath, 'r') as file:
        data = file.read()
    return data

def deleteFile(filePath):
    os.remove(filePath)

def createFileAndWrite(filePath, data):
    with open("ciph/"+filePath, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    
    currentDir = getCurrentDir()
    listOfFiles = getListOfFiles(currentDir)


    option = ""
    print("""

          1 - encrypt all the files 
          2 - decrypt all the files
          3 - crypt one file by id

    """)


    option = input("Enter your option: ")

    match option:
        case "1":
            for file in listOfFiles:
                    #read the files 
                data = readFile(file)
                    #should crypt the files 

                cryptedData = data 
                createFileAndWrite(file, data)
                    #delete the old files 
                deleteFile(file)
        case "2" : 
            for file in listOfFiles:
                    #read the files 
                data = readFile(file)
                        #should crypt the files 
                createFileAndWrite(file, data)
                        #delete the old files 
                deleteFile(file)
        case "3":
            fileId = input("Enter the file id : which is the number of the file in ")

            targetFile = listOfFiles[int(fileId)]
            data = readFile(targetFile)
            uncryptedData = data
            createFileAndWrite(targetFile, data)
            deleteFile(targetFile)