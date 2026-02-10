from fileControl import *
from EncryptControl import *

if __name__ == "__main__":
    

    option = ""
    print("""

          1 - encrypt all the files 
          2 - decrypt all the files
          3 - crypt one file by id
          4 - decrypt one file by id

    """)


    option = input("Enter your option: ")

    match option:

        case "1":
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            key = get_valid_key()

            for file in listOfFiles:
                data = readFile(file)

                #YOU SHOULD CRYPT THE CODE HERE
                cryptedData = encrypt_decrypt(text, 'e', key) 
                print("crypted data : " , cryptedData)
                createFileAndWrite(file, data)
                deleteFile(file)

        case "2" : 
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            key = get_valid_key()
            for file in listOfFiles:
                data = readFile(file)
                #YOU SHOULD DECRYPT THE CODE HERE
                uncryptedData = encrypt_decrypt(text, 'd', key)
                createFileAndWrite(file, uncryptedData , False)
                deleteFile(file)

        case "3":
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            fileId = input("Enter the file id : which is the number of the file in ")
            targetFile = listOfFiles[int(fileId)]
            data = readFile(targetFile)
            key = get_valid_key()
            #YOU SHOULD CRYPT THE CODE HERE
            cryptedData = encrypt_decrypt(text, 'd', key)
            createFileAndWrite(targetFile, cryptedData)
            deleteFile(targetFile)

        case "4":
            currentDir = getCurrentDir()

            listOfFiles = getListOfFiles(currentDir)
            fileId = input("Enter the file id : which is the number of the file in  ")
            targetFile = listOfFiles[int(fileId)]   
            data = readFile(targetFile)
            #YOU SHOULD DECRYPT THE CODE HERE
            key = get_valid_key()
            uncryptedData = plaintext = encrypt_decrypt(text, 'd', key)
            createFileAndWrite(targetFile, uncryptedData , False)        
            deleteFile(targetFile)  
        
        
