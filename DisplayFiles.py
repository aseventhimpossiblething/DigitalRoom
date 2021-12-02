import os

def showfiles():
    print("os.getcwd() 1 ",os.getcwd())
    os.chdir("/GMDelight/externalDiskForDR")
    print("os.getcwd() 2 ",os.getcwd())
    contents=str("File Location = ",os.getcwd()," ::: Contents==",os.listdir())
    #return os.getcwd();
    return contents
#print("!!!!!!!!!!!!!!!!!!!",showfiles(),"!!!!!!!!!!!!!!!!!!!!"); 
