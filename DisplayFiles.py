import os

def showfiles():
    print("os.getcwd() 1 ",os.getcwd())
    os.chdir("/GMDelight/externalDiskforDR")
    print("os.getcwd() 2 ",os.getcwd())
    return os.getcwd();
print("!!!!!!!!!!!!!!!!!!!",showfiles(),"!!!!!!!!!!!!!!!!!!!!"); 
