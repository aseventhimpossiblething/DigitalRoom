domain="http://bdxapilink.com"
usr="BDXPPC"
pwd="#!!9ooRanch"




print("1")



"""
import glob
import numpy
import scipy
import pandas
import BidOpAssist
import CommunityUpdatesProcess
import fileHandler
import os
from flask import Flask, Markup, render_template, request, make_response
from flask import send_file
from flask import send_from_directory
#import get_campaigns
"""


print("2")






from datetime import datetime
os.system('sudo chmod -R 777 Sheets')
os.system('sudo chmod -R 777 templates')


print("3")


import psycopg2
app = Flask(__name__,"/static/")


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


print("4")


def chckbdxcred():
    x=request.cookies.get(setCnam());
    y=str(x).find(bdxcred());
    if y==-1:
       print(x==bdxcred(),"*") 
       a="<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL="
       b=login_page
       c="'><html>did not forward</html>"
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
    gencook=make_response("<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=/'><html>did not forward</html>");
    x=request.form['username'];
    y=request.form['password'];
    if x==usr and y==pwd:
       print("pass"); 
       #gencook=make_response("<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=/'><html>did not forward</html>");
       gencook.set_cookie(setCnam(),bdxcred());
    #gencook="stop"
    return gencook



print("6")





@app.route('/apiresponse')
def off1():
    print("api response called")    
    return "api response called"      
     


         
@app.route('/get_campaigns')
def official():
    get_campaigns     
    return "."      
       
         

@app.route('/favicon.png')
def favicon():
    return send_from_directory('/app/favicon.png','favicon')     



print("7")


@app.route('/DisplayCommUpdate')
def CommUpdateDisplay():
    os.chdir('/var/www/workPortal/Sheets/')     
    storeRequest=open('RequestsVsResponses.txt','r+')
    read_storeRequest=storeRequest.read()
    storeRequest.close()
    print("read_storeRequest ",read_storeRequest)
    read_storeRequest1=read_storeRequest.count('Request')
    read_storeRequest2=read_storeRequest.count('Response')
    print(read_storeRequest1," <> ",read_storeRequest)     
    print("read_storeRequest ",read_storeRequest)     
    print("________________________________________________________________exp ",read_storeRequest1," : ",read_storeRequest2)
    if read_storeRequest1==read_storeRequest2:
     return "<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=/CommUpdateExcel?'><html>This Message indicates an error in URL Forward</html>"
    if read_storeRequest1!=read_storeRequest2:
     return '<meta http-equiv="refresh" content="120"><html>LOADING..... This can Take up to 20 minuites</html>'



@app.route('/CommUpdateExcel')
def CommUpdateExcel():
 global domain
 domain=domain
 return render_template('/CommUpdateExcel.html',CacheBreakStamp=datetime.now(),domain=domain)

@app.route('/GoogleKWSBMM')
def GoogleKWSBMMKW():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleKeywords/GoogleBMMKW/DefaultSheet.xlsx",\
                  attachment_filename="GoogleBMMKW.xlsx")
         
@app.route('/GoogleKWSB')
def GoogleKWSBKW():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleKeywords/GoogleBroadKW/DefaultSheet.xlsx",\
                  attachment_filename="GoogleKWSB.xlsx")

@app.route('/GoogleKWSX')
def GoogleKWSX():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleKeywords/GoogleExactKW/DefaultSheet.xlsx",\
                  attachment_filename="GoogleKWSX.xlsx")


print("8")


@app.route('/GoogleAdSBMMA')
def GoogleASBMM():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionA/GoogleAdsVersionABMM/DefaultSheet.xlsx",\
                 attachment_filename="GoogleAdSBMMA.xlsx")
                 
         


@app.route('/GoogleAdSBMMB')
def GoogleBSBMM():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionB/GoogleAdsVersionBBMM/DefaultSheet.xlsx",\
                 attachment_filename="GoogleAdSBMMB.xlsx")
                 
         
  
@app.route('/GoogleAdSBMA')
def GoogleASBM():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionA/GoogleAdsVersionABroad/DefaultSheet.xlsx",\
                 attachment_filename="GoogleAdSBMA.xlsx")
                
         

print("9")

        

@app.route('/GoogleAdSBMB')
def GoogleBSBM():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionB/GoogleAdsVersionBBroad/DefaultSheet.xlsx",\
                 attachment_filename="GoogleAdSBMB.xlsx")
                 



@app.route('/GoogleAdSXA')
def GoogleASX():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionA/GoogleAdsVersionAExact/DefaultSheet.xlsx",\
                 attachment_filename="GoogleAdASX.xlsx")
              
         


@app.route('/GoogleAdSXB')
def GoogleBSX():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Google/GoogleOutputs/GoogleAds/GoogleAdsVersionB/GoogleAdsVersionBExact/DefaultSheet.xlsx",\
                 attachment_filename="GoogleAdBSX.xlsx")
  
 
print("10")
   
        

@app.route('/BingKWSBMM')
def BingSBMMKW():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingKW/BingKWBMM/DefaultSheet.xlsx",\
                  attachment_filename="BingBMMKW.xlsx")
 
         
@app.route('/BingKWSB')
def BingSBKW():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingKW/BingKWBroad/DefaultSheet.xlsx",\
                  attachment_filename="BingSBKW.xlsx")



@app.route('/BingKWSX')
def BingSXKW():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingKW/BingKWExact/DefaultSheet.xlsx",\
                  attachment_filename="BingSXKW.xlsx")
         

         
       
@app.route('/BingAdSBMMA')
def BingASBMM():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsAtype/BingAdsAtypeBMM/DefaultSheet.xlsx",\
                 attachment_filename="BingAdSBMMA.xlsx")
                


print("11")
    
    

@app.route('/BingAdSBMMB')
def BingBSBMM():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsBtype/BingAdsBtypeBMM/DefaultSheet.xlsx",\
                 attachment_filename="BingAdSBMMB.xlsx")
              
 
         
         
@app.route('/BingAdSBA')
def BingASB():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsAtype/BingAdsAtypeBroad/DefaultSheet.xlsx",\
                 attachment_filename="BingAdSBA.xlsx")
              
         
         
  

@app.route('/BingAdSBB')
def BingBSB():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsBtype/BingAdsBtypeBroad/DefaultSheet.xlsx",\
                 attachment_filename="BingAdSBB.xlsx")
                      
                  
 



@app.route('/BingAdSXA')
def BingASX():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsAtype/BingAdsAtypeExact/DefaultSheet.xlsx",\
                 attachment_filename="BingAdSXA.xlsx")
                  


@app.route('/BingAdSXB')
def BingBSX():
 return send_file("/var/www/workPortal/Sheets/CommunityUpdates/Bing/BingOutputs/BingAds/BingAdsBtype/BingAdsBtypeExact/DefaultSheet.xlsx",\
                 attachment_filename="BingAdSXB.xlsx")



@app.route('/BasisOfBidsHuman')
def BasisH():
 return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/BidOpSeedViewable.xlsx', attachment_filename='BidOpSeedViewable.xlsx')

         

@app.route('/BasisOfBidsMachine')
def BasisM():
 return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/BidOpSeed.xlsx', attachment_filename='BidOpSeed.xlsx')

         
@app.route('/OutPutOfBiOp1')
def BasisN1():
 return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/outputsheet.xlsx', attachment_filename='Bid0p5heet1.xlsx')





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





print("14")




@app.route('/CommunityUpdates')
def CommunitiesUploads():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('CommunitiesForm.html')

@app.route('/CommunityFileHander', methods=['POST','GET'])
def CommunityFileHandling():
    return fileHandler.CommListFileHandler()
    

@app.route('/account')
def acc():
    return render_template('account.html')
    
    

print("15")
    
    
   
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





print("16")

    


@app.route('/Budget')
def Budge():
    if chckbdxcred().find("NULL")==-1:
        print(str(chckbdxcred()));
        return str(chckbdxcred());
    return render_template('Budget.html');   
    
    
    
    
    



if __name__=='__main__':
    app.run()

    
    

print("17")
    
