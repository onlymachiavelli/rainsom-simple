from fileControl import *
from EncryptionControl import *

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
            if len(listOfFiles) == 0:
                print("No files to encrypt")
                exit()
            key = get_valid_key()

            for file in listOfFiles:
                data = readFile(file)

                #YOU SHOULD CRYPT THE CODE HERE
                cryptedData = encrypt_decrypt(data, 'e', key) 
                print("crypted data : " , cryptedData)
                createFileAndWrite(file, cryptedData)
                deleteFile(file)

        case "2" : 
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            key = get_valid_key()
            if len(listOfFiles) == 0:
                print("No files to decrypt")
                exit()
            for file in listOfFiles:
                data = readFile(file)
                #YOU SHOULD DECRYPT THE CODE HERE
                uncryptedData = encrypt_decrypt(data, 'd', key)
                createFileAndWrite(file, uncryptedData , False)
                deleteFile(file)

        case "3":
            currentDir = getCurrentDir()
            listOfFiles = getListOfFiles(currentDir)
            if len(listOfFiles) == 0:
                print("No files to encrypt")
                exit()
            fileId = input("Enter the file id : which is the number of the file in ")
            while int(fileId) >= len(listOfFiles) or int(fileId) < 0:
                print("Invalid file id")
                fileId = input("Enter AGAIN the file id : which is the number of the file in ")

                
            targetFile = listOfFiles[int(fileId)]
            data = readFile(targetFile)
            key = get_valid_key()
            #YOU SHOULD CRYPT THE CODE HERE
            cryptedData = encrypt_decrypt(data, 'e', key)
            createFileAndWrite(targetFile, cryptedData)
            deleteFile(targetFile)

        case "4":
            currentDir = getCurrentDir()

            listOfFiles = getListOfFiles(currentDir)
            if len(listOfFiles) == 0:
                print("No files to decrypt")
                exit()
            fileId = input("Enter the file id : which is the number of the file in  ")
            targetFile = listOfFiles[int(fileId)]   
            data = readFile(targetFile)
            #YOU SHOULD DECRYPT THE CODE HERE
            key = get_valid_key()
            uncryptedData = plaintext = encrypt_decrypt(data, 'd', key)
            createFileAndWrite(targetFile, uncryptedData , False)        
            deleteFile(targetFile)  
        
        
