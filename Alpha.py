




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

import os
from flask import Flask, Markup, render_template, request, make_response
from flask import send_file
from flask import send_from_directory









#os.system('sudo chmod -R 777 var')
os.system('sudo chmod -R 777 Sheets')
os.system('sudo chmod -R 777 templates')










app = Flask(__name__,"/static/")




@app.route('/DRUpload', methods=['POST','GET'])
def Cupload():
    os.chdir("/GMDelight/externalDiskForDR");
    #Uploads.store();
    print("CTRUpload Button clicked")
    print("CTRUpload Button clicked")
    print("CTRUpload Button clicked") 
    print("request-",request.files['sheet'])
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('LoadingTemplate2.html');


@app.route('/proxy1')
def prox1():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    #return render_template('proxy1.html')
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
       #return logontrue();
    else:
       return "NULL"
 
    
    

print("5")
    


@app.route(login_page)
def mlgn():
    gencook="<a href='/l2'>form</a>";
    gencook=render_template("loginPage.html")
    #gencook.set_cookie(setCnam(),bdxcred());
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
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    global domain;     
    domainFavi=domain+"/favicon.png";
    view9="http://"+domain+"/view9"
    fimage=str(DisplayFiles.showfiles())
    return render_template('LoadingTemplate.html',domain=domain,domainFav=domainFavi,fimage=fimage,view9=view9);
    #return "vfiles!";
    #return str(DisplayFiles.showfiles())
    
    
    

print("13")
    

@app.route('/tests')
def indtest():
    global domain;     
    domainFavi=domain+"/favicon.png";
    fimage=str(DisplayFiles.showfiles())
    return render_template('LoadingTemplate2.html',domain=domain,domainFav=domainFavi,fimage=fimage,);
    
        
    
    














    
    









 
    
    
    
    



if __name__=='__main__':
    app.run()

    
    
print("loaded")
    
