




domain="DigitalRoomFileShare.Cloud"
usr="open"
pwd="open"
from datetime import datetime






import Uploads
import DisplayFiles
import glob
import numpy
import scipy
import pandas
import FormatSheet
import threading
import os
import sys

from flask import Flask, Markup, render_template, request, make_response, redirect
from flask import send_file
from flask import send_from_directory









#os.system('sudo chmod -R 777 var')
os.system('sudo chmod -R 777 Sheets')
os.system('sudo chmod -R 777 templates')










app = Flask(__name__,"/static/")




@app.route('/DRUpload', methods=['POST','GET'])
def Cupload():
    DisplayFiles.SaveFileFromLoadingTemplate(request,"/GMDelight/view9");
    domainFavi=domain+"/static/favicon.png";
    delfile="/delfile"
    fimage=str(DisplayFiles.showfiles("/GMDelight/view9",delfile))
    view9="http://"+domain+"/view10"
    return render_template('LoadingTemplate.html',domain=domain,domainFav=domainFavi,fimage=fimage,view9=view9);
    """
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('LoadingTemplate.html');
    """


@app.route('/delfile',methods=['POST','GET'])
def dfile():
    delfile="/delfile"
    print("request ",request);
    reqstr=str(request);
    findsign=reqstr.find("=")
    findendspace=reqstr.find("' ")
    print("find = ",findsign)
    print("findendspace ",findendspace)
    filename=reqstr[findsign+1:findendspace]
    print("filename ",filename)
    print("os,getcwd() ",os.getcwd())
    print("listdir ",os.listdir())
    os.chdir("/GMDelight/view9")
    os.remove(filename.replace("+"," "));
    print("os,getcwd() ",os.getcwd());
    print("listdir ",os.listdir())
    deletedfile=filename+" deleted"
    return DisplayFiles.showfiles("/GMDelight/view9",delfile);

@app.route('/delfile0',methods=['POST','GET'])
def dfile0():
    print("request ",request);
    reqstr=str(request);
    findsign=reqstr.find("=")
    findendspace=reqstr.find("' ")
    delfile="/delfile0"
    print("find = ",findsign)
    print("findendspace ",findendspace)
    filename=reqstr[findsign+1:findendspace]
    print("filename ",filename)
    print("os,getcwd() ",os.getcwd())
    print("listdir ",os.listdir())
    os.chdir("/GMDelight/DigitalRoom/Sheets/CTRData")
    os.remove(filename.replace("+"," "));
    print("os,getcwd() ",os.getcwd());
    print("listdir ",os.listdir())
    deletedfile=filename+" deleted"
    return DisplayFiles.showfiles("/GMDelight/DigitalRoom/Sheets/CTRData",delfile);
    
    
@app.route('/proxy1')
def prox1():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return accesspoint.pullpage();  


@app.route('/proxy2')
def prox2():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('proxy2.html')



login_page="/login"
def setCnam():
    return "hyo123"

def bdxcred():
    credential="sancho1001"
    return credential



def logontrue():
    return "pass"
def logonfalse():
    return "no pass"





def chckbdxcred():
    x=request.cookies.get(setCnam());
    y=str(x).find(bdxcred());
    if y==-1:
       print(x==bdxcred(),"*") 
       a="<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL="
       b=login_page
       c="'><html>did not forward - GMDelight</html>"
       abc=a+b+c
       return abc 
    else:
       return "NULL"
 
    
    

print("5")
    


@app.route(login_page)
def mlgn():
    gencook="<a href='/l2'>form</a>";
    gencook=render_template("loginPage.html")
    return gencook

@app.route('/l2', methods=['POST'])
def mlgne():
    global usr
    usr=usr;
    global pwd
    pwd=pwd;
    print(usr);
    print(pwd);
    gencook=make_response("<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=/'><html>did not forward - GMDelight </html>");
    x=request.form['username'];
    y=request.form['password'];
    if x==usr and y==pwd:
       print("pass"); 
       #gencook=make_response("<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=/'><html>did not forward</html>");
       gencook.set_cookie(setCnam(),bdxcred());
    #gencook="stop"
    return gencook



print("6")





@app.route('/favicon.png')
def favicon():
    return send_from_directory('/app/favicon.png','favicon')     



print("7")









print("12")






@app.route('/css')
def styleSheet1():
    return render_template('csstemplate.css')

@app.route('/Scripts')
def Scripts():    
    return render_template('Scripts.js')

@app.route('/')
def index():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    global domain;     
    domainFavi=domain+"/favicon.png";
    return render_template('LandingTemplate.html',domain=domain,domainFav=domainFavi);
    #return chckbdxcred();
    
    
@app.route('/vfiles')
def indece():
    delfile="/delfile"
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    global domain;     
    domainFavi=domain+"/favicon.png";
    #view9="http://"+domain+"/Testing"
    #view9="http://"+domain+"/Testing"
    fimage=DisplayFiles.showfiles("/GMDelight/view9",delfile)
    view9="http://"+domain+"/view10"
    return render_template('LoadingTemplate.html',domain=domain,domainFav=domainFavi,fimage=fimage,view9=view9);

@app.route('/view10')
def indembd():
    delfile="/delfile"
    global domain;     
    domainFavi=domain+"/favicon.png";
    #fimage=str(DisplayFiles.showfilesV0())
    #return render_template('LoadingTemplate2.html',domain=domain,domainFav=domainFavi,fimage=fimage,);
    return DisplayFiles.showfiles("/GMDelight/view9",delfile);

@app.route('/external')
def indvr():
    global domain;     
    domainFavi=domain+"/favicon.png";
    #view9="http://"+domain+"/Testing"
    #view9="http://"+domain+"/Testing"
    #fimage=DisplayFiles.showfilesV0()
    view9="http://"+domain+"/externalview"
    return render_template('LoadingTemplate2.html',domain=domain,domainFav=domainFavi,view9=view9);
    
    
    
    
    

print("13")

@app.route('/externalview')
def indembed():
    delfile="/delfile0"
    global domain;     
    domainFavi=domain+"/favicon.png";
    return DisplayFiles.showfilesV0("/GMDelight/view9");

@app.route('/view11')
def inde11d():
    delfile="/delfile0"
    global domain;     
    domainFavi=domain+"/favicon.png";
    return DisplayFiles.showfiles("/GMDelight/DigitalRoom/Sheets/CTRData",delfile);

@app.route('/externalupdate', methods=['POST','GET'])
def indupdate():
    DisplayFiles.SaveFileFromLoadingTemplate(request,"/GMDelight/view9");
    global domain;     
    domainFavi=domain+"/favicon.png";
    view9="http://"+domain+"/externalview"
    return render_template('LoadingTemplate2.html',domain=domain,domainFav=domainFavi,view9=view9);

    
@app.route('/Loadfiles')
def inddigogo():
    print("---------------------------------------------------")
    os.chdir('/GMDelight/DigitalRoom/static/');
    print("get cwd ",os.getcwd())
    #os.remove("rpt.html"); 
    print("List dir ",os.listdir())
    if os.path.exists("/rpt.html"): 
       print("If path ") 
       os.remove("rpt.html"); 
    os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData'); 
    print("List dir ",os.listdir())
    print("---------------------------------------------------")    
    global domain;     
    domainFavi=domain+"/favicon.png";
    view9="/view11"
    #FormatSheet.rpt();
    #rpt=threading.Thread(target=FormatSheet.RegCorDescShift());
    #rpt.start();
    #Formatinput=FormatSheet.RegCorDescShift();
    return render_template('LoadingTemplate3.html',domain=domain,domainFav=domainFavi,view9=view9);
   
    
@app.route('/Loadfiles1',methods=['POST','GET'])
def inddigog1():
    """
    os.chdir('/GMDelight/DigitalRoom/static/');
    if os.path.exists("rpt.html"):    
       os.remove("rpt.html"); 
    print("Print cwd ",os.getcwd())
    """
    DisplayFiles.SaveFileFromLoadingTemplate(request,"/GMDelight/DigitalRoom/Sheets/CTRData");
    global domain;     
    domainFavi=domain+"/favicon.png";
    view9="/view11"
    #FormatSheet.rpt();
    #rpt=threading.Thread(target=FormatSheet.RegCorDescShift());
    #rpt.start();
    #Formatinput=FormatSheet.RegCorDescShift();
    return render_template('LoadingTemplate3.html',domain=domain,domainFav=domainFavi,view9=view9);

@app.route('/rpt',methods=['POST','GET'])
def rpt():
    os.chdir('/GMDelight/DigitalRoom/static/');
    if os.path.exists("rpt.html"):    
       os.remove("rpt.html"); 
    global domain;     
    domainFavi=domain+"/favicon.png";
    print('return from process attempt = ',FormatSheet.rpt())
    return redirect("/rptry?");
 
         
@app.route('/rptry')
def rptt():
    os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
    print("check for fail  ",os.listdir())
    if os.path.exists("BlankSheet"):    
       os.remove("BlankSheet"); 
       print("check for fail; path followed  ")
       return "FAILED TRANSACTION..NO VALID SHEET FOUND" 
    global domain;     
    domainFavi=domain+"/favicon.png";
    print("reload-----")
    print(os.getcwd())
    os.chdir('/GMDelight/DigitalRoom/static/');
    print(os.getcwd())
    if os.path.exists("rpt.html"):
        page=open("rpt.html",'r');
        DisplayPage=page.read();
        page.close();
        print("if path entered..")
        return DisplayPage;
        #return '<html><iframe src="/static/rpt.html"></iframe></html>'
        #return "<html><meta http-equiv='refresh' content='1'; url='/static/rpt.html'>Loading...</html>"
        #return "<html><meta http-equiv='refresh' content='10'; url='http://"+domain+"/static/rpt.html'>Loading...</html>"
    return "<html><meta http-equiv='refresh' content='60'>Loading...</html>"
  
             
    
    
"""
@app.route('/tests')
def indtest():
    global domain;     
    domainFavi=domain+"/favicon.png";
    fimage=str(DisplayFiles.showfiles())
    return render_template('LoadingTemplate2.html',domain=domain,domainFav=domainFavi,fimage=fimage,);
"""    
        
    
    














    
    









 
    
    
    
    



if __name__=='__main__':
    app.run()

    
    
print("loaded")
    
