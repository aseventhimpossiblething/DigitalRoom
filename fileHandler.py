import BidOpAssist
import CommunityUpdatesProcess
import CommunityUpdatesProcess2
from datetime import datetime
from flask import Flask, Markup, render_template, request
import glob
import os
import pandas
import time
import xlrd
import io
import threading
from flask import send_file
import gc
import re
from openpyxl import Workbook
from openpyxl import load_workbook
import xlsxwriter


#os.system('echo his is Echoed by system os number 1')
SheetsFileLocation="/var/www/workPortal/Sheets"
currentCommunitiesLocation="/var/www/workPortal/Sheets/CommunityUpdates/currentCommunities"
currentGoogleLocation="/var/www/workPortal/Sheets/CommunityUpdates/Google/currentGoogle"
currentBingLocation="/var/www/workPortal/Sheets/CommunityUpdates/Bing/currentBing"
#os.system('echo his is Echoed by system os number 2')
def ValidatXLSXtime(arr):
        Error=arr+" Generated an error check that filetype is xlsx"
        Valid=arr+" is valid"
        if time.time()-os.path.getctime(arr)>600000:
            print(Error)
        else:
            print(Valid)

def BidOpFileHandler():
        
    os.chdir('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/')
    request.files['sheet'].save("Temp.xlsx")
    Temp=pandas.read_excel('Temp.xlsx')
    record_async_start=open("ForestLoadingQueue.txt","w")
    record_async_start.write("1%")
    record_async_start.close()
    print("1%")
    #record_async_start.close()    
    #Temp.fillna(0) 
    isTrainingSheet=str(Temp.columns).find('New Bid') 
    if isTrainingSheet!=-1:
       def TrainBehavior():
           print('async started') 
           os.chdir('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/')
           Temp=pandas.read_excel('Temp.xlsx')
           Temp=pandas.DataFrame(Temp,columns=['Keyword','New Bid','Campaign','Ad group','Match type','Changes','Bid','Clicks','CTR','Avg. CPC','Spend','Conv.','CPA','Conv. rate','Top Impr. share','Absolute Top Impression Share','Impr. share (IS)','Qual. score','IS lost to rank','IS lost to budget'])
           Temp.fillna(0)
           CoreTrainingData=pandas.read_excel('BidOpSeed.xlsx')
           CoreTrainingData=CoreTrainingData.append(Temp, sort='False')
           CoreTrainingData=pandas.DataFrame(CoreTrainingData,columns=['Keyword','New Bid','Campaign','Ad group','Match type','Changes','Bid','Clicks','CTR','Avg. CPC','Spend','Conv.','CPA','Conv. rate','Top Impr. share','Absolute Top Impression Share','Impr. share (IS)','Qual. score','IS lost to rank','IS lost to budget'])
           CoreTrainingData.to_excel('BidOpSeedViewable.xlsx')
           ccountr=0;   
           Match_Type=[];
           for kw in Temp['Match type']:
               #ccountr+=1;
               if kw=='Exact':
                kw=1;
               if kw=='Broad':
                kw=2;
               if str(Temp['Campaign'][ccountr]).lower().find("gppc")>-1:
                kw=(kw)(1000);
               #print("Timeout on second pass count ",ccountr)
               
               Match_Type.append(kw)
               #print(len(Match_Type))  
           record_async_start=open("ForestLoadingQueue.txt","w")
           record_async_start.write("25%")
           record_async_start.close()     
               
           Temp['Match Type']=Match_Type;
           #print("-------------------Immediatly following Number conversion below-----")   
           #print("Temp['Match Type']",Temp['Match Type'])     
           #print("-------------------Immediatly following Number conversion above-----") 
           Temp=pandas.DataFrame(Temp,columns=['Changes','Campaign','Ad group','Match Type','Bid','Clicks','CTR','Avg. CPC','Spend','Conv.','CPA','Conv. rate','Top Impr. share','Absolute Top Impression Share','Impr. share (IS)','Qual. score','IS lost to rank','IS lost to budget']) 
           #print("-------------------Immediatly following Number Reframe Below-----") 
           #print(Temp['Match Type'])
           #print("-------------------Immediatly following reframe above-----") 
           record_async_start=open("ForestLoadingQueue.txt","w")
           record_async_start.write("50%")
           record_async_start.close()     
           Market=[];
           for kw in Temp['Ad group']:
               if str(re.search('>\d+',kw)).find("None")!=-1:
                      kw="match='>0"
               kw=str(re.search('>\d+',kw))
               targLoc=kw.find("match='>")
               kw=kw[targLoc:].replace("match='>","").replace("'>","")
               Market.append(kw)
           Temp['Market Number']=Market
           core=pandas.read_excel('BidOpSeed.xlsx')
           core=core.append(Temp, sort='False')
           core=pandas.DataFrame(core,columns=['Changes','Campaign','Ad group','Match Type','Bid','Clicks','CTR','Avg. CPC','Spend','Conv.','CPA','Conv. rate','Top Impr. share','Absolute Top Impression Share','Impr. share (IS)','Qual. score','IS lost to rank','IS lost to budget','Market Number']) 
           core.to_excel("BidOpSeed.xlsx")
           print(core)
           record_async_start=open("ForestLoadingQueue.txt","w")
           record_async_start.write("100%")
           record_async_start.close();     
           
           return "<html><a href='/BasisOfBids'>This Training Sheet will be added to the body of training Data Click to view Basis Sheet</a></html>"
       #TrainBehavior(Temp);
       TrainLoad=threading.Thread(target=TrainBehavior);
       TrainLoad.start(); 
       #return "Sheet has Been Identified as Training Data it is being formatted and Loaded as such... please wait.. do not press back button"  
       print("is there an attempt to return")
       return "<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=http://bhiapilink.com/BidOpPending'><html>did not forward</html>"
       
    else:
       isTrainingSheet="This is Not Training Data, Attempt will be made to Optimise bids"         
                
        
    
    toscrn=isTrainingSheet
    #toscrn="Dataset is labelled Training. It will Be used as Training Data"
                
    #print(isTrainSet)
    print("os.listdir()____:",os.listdir())

    return toscrn
    #return send_file('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/BidOpSeed.xlsx', attachment_filename='BidOpSeed.xlsx')

def CommListFileHandler():
    print("Starting to Handle Files") 
    
    reqs=request.files,request.files['Communities'],request.files['currentGoogle'],request.files['currentBing']   
    emptyObj="<FileStorage: '' ('application/octet-stream')>" 
    if emptyObj==str(request.files['currentBing']):
         return "Bing slot is empty"
    if emptyObj==str(request.files['currentGoogle']):
        return "Google slot is empty"
    if emptyObj==str(request.files['Communities']):
        return "Active Community slot is empty"
       
    
    #print("did not Check That File Slots are Filled")    
    
    if request.files['Communities'].filename.find("xlsx")<1:
                return "The Community Sheet is not XLSX file type";
    if request.files['currentGoogle'].filename.find("xlsx")<1:
                return "The Google Sheet is not XLSX file type";
    if request.files['currentBing'].filename.find("xlsx")<1:
                return "The Bing Sheet is not XLSX file type"; 
            
    #print("did not Check that Filles are XlSX")    
   
    os.chdir(currentCommunitiesLocation)
    SHcommand="sudo chmod -R 777 "+currentCommunitiesLocation
    os.system(SHcommand+"/WorkingCommunities")
    request.files['Communities'].save('WorkingCommunities')
       
    os.chdir(currentGoogleLocation)
    request.files['currentGoogle'].save('WorkingGoogle')
    
    os.chdir(currentBingLocation)
    request.files['currentBing'].save('WorkingBing')
     
    #print("saved Files") 
  
    
   
   
       
    def async_fileloader():
     os.chdir(SheetsFileLocation) 
     storeRequest=open('RequestsVsResponses.txt','w')    
     storeRequest.write("Request, ")
     storeRequest.close()           
     CommunityUpdatesProcess.initialCommUpdatProcess()
    LoadAllCommunityFiles=threading.Thread(target=async_fileloader)
    LoadAllCommunityFiles.start()    
    #print("Should respond now!!! ")
    #os.system('echo his is Echoed by system os number 3')    
    return "<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate'><meta http-equiv='refresh' content='0;URL=http://bhiapilink.com/DisplayCommUpdate'><html>did not forward</html>"
         







    




    


    

    

