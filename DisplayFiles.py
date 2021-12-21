import os
import pandas
def SaveFileFromLoadingTemplate(x):
    request=x
    os.chdir("/GMDelight/view9");
    #print(os.listdir())
    req=request.files['sheet'];
    reqstr=str(req);
    print(os.listdir())
    print(reqstr)
    #startfn=reqstr.find("FileStorage:");
    #print(startfn)
    endfn=reqstr.find("(");
    #print(endfn)
    FileName=reqstr[15:endfn-2];
    print("FileName - ",FileName);
    request.files['sheet'].save(FileName);
    #Uploads.store();
    print(" Button clicked")
    print("Button clicked")
    print("Button clicked") 
    #print("request-",request.files['sheet'])

def showfiles():
    print("os.getcwd() 1 ",os.getcwd())
    os.chdir("/GMDelight/view9")
    print("os.getcwd() 2 ",os.getcwd())
    print("len(os.listdir())  ",len(os.listdir()))
    contents=os.listdir()
    DF=pandas.DataFrame(contents);
    print("DF ",DF)
    len(contents);
    print("len(contents) = ",len(contents));
    
    nz=0;
    while nz<len(contents):
          li=contents[nz];
             
          print(li)  
          nz=nz+1;
    #return os.getcwd();
    return contents
#print("!!!!!!!!!!!!!!!!!!!",showfiles(),"!!!!!!!!!!!!!!!!!!!!"); 
