import os

def showfiles():
    print("os.getcwd() 1 ",os.getcwd())
    os.chdir("/GMDelight/externalDiskForDR")
    print("os.getcwd() 2 ",os.getcwd())
    contents=str(os.getcwd(),"-",str(os.listdir()))
    #return os.getcwd();
    return contents
#print("!!!!!!!!!!!!!!!!!!!",showfiles(),"!!!!!!!!!!!!!!!!!!!!"); 
