#import accesspoint
#import accumulateGMEfiles
#accesspoint.pullpage();
#accumulateGMEfiles.py;
#delete above after experiment



#domain="http://bdxapilink.com"
domain="rememberGME"
usr="open"
pwd="open"
from datetime import datetime








import glob
import numpy
import scipy
import pandas
import BidOpAssist
import fileHandler
#import accumulateGMEfiles
import os
from flask import Flask, Markup, render_template, request, make_response
from flask import send_file
from flask import send_from_directory




"""
nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
print(nasdaqAbbreviations)
filedate=str(datetime.now().date())
ndq=str('curl '+nasdaqAbbreviations+' -o nasdaqAbbreviations-'+filedate)
print(ndq)
os.system(ndq)
"""







#os.system('sudo chmod -R 777 var')
os.system('sudo chmod -R 777 Sheets')
os.system('sudo chmod -R 777 templates')

#os.system('curl https://www.google.com')
#os.system('curl https://www.google.com')





import psycopg2


app = Flask(__name__,"/static/")

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





@app.route('/stonks')
def stonk():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return str(accumulateGMEfiles.TableGen());




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





@app.route('/BasisOfBidsHuman')
def BasisH():
 return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/BidOpSeedViewable.xlsx', attachment_filename='BidOpSeedViewable.xlsx')

         

@app.route('/BasisOfBidsMachine')
def BasisM():
 return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/BidOpSeed.xlsx', attachment_filename='BidOpSeed.xlsx')

@app.route('/BasisOfCTRMachine')
def BasisN():
 return send_file('/var/www/workPortal/Sheets/CTRData/MachinePatternSheets/CTRSeed.xlsx', attachment_filename='CTRSeed.xlsx')

         
@app.route('/OutPutOfBiOp1')
def BasisN1():
 return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/outputsheet.xlsx', attachment_filename='Bid0p5heet1.xlsx')

@app.route('/OutPutOfCTRPred')
def BasisN2():
 return send_file('/var/www/workPortal/Sheets/CTRData/MachinePatternSheets/ctroutputsheet.xlsx', attachment_filename='CTROut5heet1.xlsx')

@app.route('/OutPutOfCTRfeatureReport')
def BasisN3():
 return send_file('/var/www/workPortal/Sheets/CTRData/MachinePatternSheets/featuresheet.xlsx', attachment_filename='CTROut5heet2.xlsx')


"""
@app.route('/GMEout0')
def GME0():
 return send_file('/Sheets/rememberGME/GMEouts/gmetemplate.xlsx', attachment_filename='GMEout.xlsx')
"""
@app.route('/GMEout0')
def GME0():
 print(os.getcwd())  
 print(os.listdir())
 return send_file('/gmetemplate.xlsx', attachment_filename='a')




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

    
    
    

print("13")
    

    
    
    
@app.route('/BidOps')
def BidOpInput():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('BidOpForm.html')



@app.route('/BidOPUpload', methods=['POST','GET'])
def BidOPUpload():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return fileHandler.BidOpFileHandler()


@app.route('/CTRForm')
def CTRform():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('CTRForm.html')


@app.route('/CTRUpload', methods=['POST','GET'])
def CTRupload():
    print("CTRUpload Button clicked")
    print("CTRUpload Button clicked")
    print("CTRUpload Button clicked")    
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return fileHandler.CTRUploadFilehandler()






    
    
   
@app.route('/BidOpPending')
def acd():
    os.chdir('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/')
    readiness=open("ForestLoadingQueue.txt","r")
    ready=readiness.read()
    print(ready)
    BPD='<meta http-equiv="refresh" content="45"><html>This Training Sheet will be added to the body of training Data  - '+ready+"</html>"
    if ready=="100%":
       BPD="render_template('BidOpPending.html')";
    if ready.find("]")>-1:
       BPD='<html>The following columns are missing from the Data set - '+ready+"</html>"           
    #BPD=str(BPD2) 
    print(BPD)
    readiness.close()     
    if ready=="100%":
       return render_template('BidOpPending.html',CacheBreakStamp=datetime.now());
    return BPD


@app.route('/CTRPending')
def acdc():
    os.chdir('/var/www/workPortal/Sheets/CTRData/MachinePatternSheets/')
    readiness=open("ForestLoadingQueue.txt","r")
    ready=readiness.read()
    print(ready)
    BPD='<meta http-equiv="refresh" content="45"><html>This Training Sheet will be added to the body of training Data  - '+ready+"</html>"
    if ready=="100%":
       BPD="render_template('BidOpPending.html')";
    if ready.find("]")>-1:
       BPD='<html>The following columns are missing from the Data set - '+ready+"</html>"           
    #BPD=str(BPD2) 
    print(BPD)
    readiness.close()     
    if ready=="100%":
       return render_template('BidOpPending.html',CacheBreakStamp=datetime.now());
    return BPD



@app.route('/BidOptimisation')
def BdOptmstn():
    print("timer fired")     
    os.chdir('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/')  
    #print(os.getcwd())
    readiness=open("ForestLoadingQueue.txt","r")
    ready=readiness.read()
    settleURL='<meta http-equiv="refresh" content="50"><html>Bids are Being Optimised  - '+ready+"</html>"
    if ready.find("100%")>-1:
       return render_template("BidOptimisation.html",CacheBreakStamp=datetime.now())           
    return settleURL

@app.route('/CTRPrediction')
def CTRmst():
    print("timer fired")     
    os.chdir('/var/www/workPortal/Sheets/CTRData/MachinePatternSheets/')  
    #print(os.getcwd())
    readiness=open("ForestLoadingQueue.txt","r")
    ready=readiness.read()
    settleURL='<meta http-equiv="refresh" content="50"><html>Bids are Being Optimised  - '+ready+"</html>"
    if ready.find("100%")>-1:
       return render_template("CTRPrediction.html",CacheBreakStamp=datetime.now())           
    return settleURL





 
    
    
    
    



if __name__=='__main__':
    app.run()

    
    
print("loaded")
    
