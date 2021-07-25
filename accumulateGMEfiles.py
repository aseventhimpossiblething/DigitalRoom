
"""
Your dedicated access key is: 70YMNXM4BZWGEGOA
Please record this API key at a safe place for future data access.
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=demo
"""
# all IEX supported symbols https://cloud.iexapis.com/beta/ref-data/symbols?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
# workin0g example 1 quote current price https://cloud.iexapis.com/stable/stock/XOM/quote?token=pk_2a5af8857a7940d4b361bc2b4a14d0adf
#zetapk_2a5af8857a7940d4b361bc2b4a14d0adf 
#zetask_20d88bd4d61b4e92b2ae7b22d8f8f0aef

#Below need testing
#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMD&apikey=70YMNXM4BZWGEGOA"
#AlphaVantageAbbreviations="https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=70YMNXM4BZWGEGOA"
#AlphaVantageEndPoint="https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbol=AMD&apikey=70YMNXM4BZWGEGOA"
print("accumulateGMEfiles.py internal run");
import openpyxl
import threading
import requests
import os
from datetime import datetime
import pandas
import json
import numpy

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10)

from sklearn import linear_model
ols = linear_model.LinearRegression()

from sklearn.model_selection import train_test_split


test="https://sandbox.iexapis.com/stable/stock/AMD/chart/1y?token=Tpk_ae999384a70348b3855e8904d4c46e5e"
def SinglestockIEXdict(x,y,z):
        innerarr=[];
        count=0;
        if z!=0:
           innerarr.append(z+y);
        else:
           innerarr.append(y);  
        while count<len(x):
              push=x[count][y];
              innerarr.append(push); 
              count=count+1;
        out=pandas.DataFrame(innerarr, columns=[y]);
        return innerarr;      
        
        
def IEXColmaker():
        print("IEXColmaker(): running");
        URLPull=test;
        vixPull=URLPull.replace("AMD","VXX");
        xlfPull=URLPull.replace("AMD","SQQQ");
        iexpull=requests.get(URLPull);
        vixPull=requests.get(vixPull);
        xlfPull=requests.get(xlfPull);
        print(iexpull)
        iexdata=json.loads(iexpull.text);
        vixdata=json.loads(vixPull.text);
        xlfdata=json.loads(xlfPull.text);
       
        arr=[];
        vixarr=[];
        xlfarr=[];
                
        keys=list(iexdata[0].keys());
        vixkeys=list(vixdata[0].keys());
        xlfkeys=list(xlfdata[0].keys());
        
        def colPrefix(x):
            print("colPrefix running")    
            prefixedelems=[];
            for elems in x:
                elems="vx"+elems;
                prefixedelems.append(elems);
                prefixedelems;
            return prefixedelems;    
        vixkeys=colPrefix(vixkeys);               
        def subtable(data,key,z):
            iarr=[];    
            count=0;
            while count<len(key): 
              iarr.append(SinglestockIEXdict(data,key[count],z));  
              count=count+1;
            return iarr;
        arr=subtable(iexdata,keys,0);
        vixarr=subtable(vixdata,keys,"vx");
        xlfarr=subtable(xlfdata,keys,"xl");
                       
        def dframemaker(x,y):
            drops=["label","symbol","id","key","subkey"];
            altdrops=[];
            for elem in drops:
                elem=y+elem;
                altdrops.append(elem);
            Newarr=pandas.DataFrame(x).transpose();
            Newarr=Newarr.rename(columns=Newarr.iloc[0]);
            Newarr=Newarr.drop([0]).reset_index().drop(altdrops, axis=1);    
            return Newarr;    
        arr1=dframemaker(arr,"");
        vixarr1=dframemaker(vixarr,"vx");
        xlfxarr1=dframemaker(xlfarr,"xl");
              
        def metricshift(w,q):
            shiftCol=[];
            shiftColDate=[];
            w=w[q];
            #print(w)    
            #w=frame (arr1);    
            #q=basis columns
            #z=projection timeframe in days
            date=arr1['date'];
            count=0;
            while count<len(w):
              shiftColDate.append(date[count]);  
              count=count+1;
              if count==len(w):
                 return shiftCol;       
              shiftCol.append(w[count]);
            return shiftCol;
        dayshiftedclose=metricshift(arr1,'close');
        #arr1=arr1.drop([len(dayshiftedclose)]);
        #vixarr1=vixarr1.drop([len(dayshiftedclose)]);
        #xlfxarr1=xlfxarr1.drop([len(dayshiftedclose)]);
        
        #print(arr1.columns)
        #print(arr1['date'])
        
        #print(vixarr1.columns)
        #print(vixarr1['vxdate'])
        
        #print(xlfxarr1['xldate'])
        
        #print(vixarr1)
        #print(xlfxarr1)
        #print(vixarr1)
        
        
        #print(arr1['date'],vixarr1['vxdate'],xlfxarr1['xldate']);
        print("pause before?")
        def compare(x1,y1,z):
            print(len(y1));
            y1.iloc[len(y1)]
            if len(y1)>len(x1):
               #y1=y1.drop([len(dayshiftedclose)]); 
               y1=y1.drop([len(y1)-1]);
            print(len(y1));    
            y1.iloc[len(y1)]
            return;    
            #print(len(y1));     
            #list(y1.columns).find('date')    
            daten=z+'date'    
            x=x1['date']; 
            y=y1[daten];    
                
            print("compare running")    
            arr=[]; 
            count=0;  
            xdesignator=int(x[len(x)-1][8:]);
            ydesignator=int(y[len(y)-1][8:]);
            alty=y1;
            #arr1=arr1.drop([len(dayshiftedclose)])
            print("xdesignator==ydesignator ",xdesignator,"==",ydesignator) 
            if xdesignator==ydesignator:
               print("xdesignator==ydesignator ",xdesignator,"==",ydesignator)         
               return y1;
            """
            if xdesignator>ydesignator:
               y1=y1.drop([len(dayshiftedclose)]);
               y=y1[daten];
               ydesignator=int(y[len(y)-1][8:]); 
               #print("xdesignator==ydesignator ",xdesignator,"==",ydesignator)         
               #return y1=y1.drop([len(dayshiftedclose)]);
               return y1
            """
            if xdesignator<ydesignator:  
               while count < len(x):
                  if x[count]==y[count]: 
                     print(count,"--",x[count],"==",y[count]);   
                        
                  else:
                     print("break")           
                     print(count,"--",x[count],"==",y[count]); 
                     yrmo=y[count][:8];
                     newday=x[count];
                     newday=pandas.DataFrame([newday], columns=[daten]);
                     for elem in alty.columns:
                         arr.append(0);
                     narr=pandas.DataFrame(arr);
                     narr=narr.transpose();
                     altyCols=list(alty.columns).remove('index');
                     narr.columns=alty.columns; 
                     #narr[daten];
                     narr=narr.drop(columns=[daten]);
                     narr[daten]=newday;
                     topcan=alty[:count];
                     midcan=narr;
                     bottomcan=alty[count:];
                     topcan=topcan.append(midcan);
                     topcan=topcan.append(bottomcan);
                     #print(topcan)
                     
                     tdesignator=topcan[daten].iloc[len(topcan)-1]; 
                     print((tdesignator[8:]))   
                     tdesignator=int(tdesignator[8:]); 
                     if xdesignator==tdesignator:
                        print("xdesignator=tdesignator ",xdesignator,"==",tdesignator)        
                        return topcan        
                     else:
                        print("lens() ",len(x1),"--",len(topcan));        
                        print("compare() ,looping");
                        print("because xdesignator=tdesignator ",xdesignator,"==",tdesignator,"--",xdesignator==tdesignator)   
                        compare(x1,y1,z);
                     #return topcan;   
                     
                  count=count+1;
                  
            return y1;            
             
        #compare(arr1['date'],xlfxarr1['xldate']); 
        #print("first divergence ",comp);
        arr1=arr1.drop([len(dayshiftedclose)]);
        vixarr1=compare(arr1,vixarr1,'vx'); 
        xlfxarr1=compare(arr1,xlfxarr1,'xl'); 
        #vixarr1=vixarr1.drop([len(dayshiftedclose)]);
        #xlfxarr1=xlfxarr1.drop([len(dayshiftedclose)]);
        
        arr1['dayshiftedclose']=dayshiftedclose;
        arrvix=arr1.merge(vixarr1, on="index");
        xlfarrvix=arrvix.merge(xlfxarr1, on="index");
        
        #print("77777777777777777777777777777777777777777000000000000000000000000000000000000000")
        #print(arrvix)
        #print("77777777777777777777777777777777777777777000000000000000000000000000000000000000")
        
        xx=xlfarrvix.drop(['dayshiftedclose','date','xldate'], axis=1);
        xy=xlfarrvix['dayshiftedclose'];
        vx=arrvix.drop(['dayshiftedclose','date','vxdate'], axis=1);
        vy=arrvix['dayshiftedclose'];
        x=arr1.drop(['dayshiftedclose','date'], axis=1);
        y=arr1['dayshiftedclose'];
                  
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2);
        
        TreeMod10=RandomForestRegressor(n_estimators = 10).fit(x_train,y_train);
        TreeModPredict10=TreeMod10.predict(x_test);
               
        TreeMod100=RandomForestRegressor(n_estimators = 100).fit(x_train,y_train);
        TreeModPredict100=TreeMod100.predict(x_test);
        
        TreeMod200=RandomForestRegressor(n_estimators = 200).fit(x_train,y_train);
        TreeModPredict200=TreeMod200.predict(x_test);
            
        LinearMod=linear_model.LinearRegression().fit(x_train,y_train);
        LinearPredictMod=LinearMod.predict(x_test);
              
        reviewFrame=pandas.DataFrame(y_test);
        reviewFrame.columns=['Shifted close'];
        reviewFrame['close']=list(x_test['close']);
           
        reviewFrame['Tree Prediction 10']=TreeModPredict10;
        reviewFrame['Tree Prediction 100']=TreeModPredict100;
        reviewFrame['Tree Prediction 200']=TreeModPredict200;
        reviewFrame['Linear Prediction']=LinearPredictMod;
        
        
        vx_train,vx_test,vy_train,vy_test=train_test_split(vx,vy,test_size=0.2);
        
        vTreeMod10=RandomForestRegressor(n_estimators = 10).fit(vx_train,vy_train);
        vTreeModPredict10=vTreeMod10.predict(vx_test);
               
        vTreeMod100=RandomForestRegressor(n_estimators = 100).fit(vx_train,vy_train);
        vTreeModPredict100=vTreeMod100.predict(vx_test);
        
        vTreeMod200=RandomForestRegressor(n_estimators = 200).fit(vx_train,vy_train);
        vTreeModPredict200=vTreeMod200.predict(vx_test);
            
        vLinearMod=linear_model.LinearRegression().fit(vx_train,vy_train);
        vLinearPredictMod=vLinearMod.predict(vx_test);
              
        vreviewFrame=pandas.DataFrame(vy_test);
        vreviewFrame.columns=['Shifted close'];
        vreviewFrame['close']=list(vx_test['close']);
           
        vreviewFrame['Tree Prediction 10']=vTreeModPredict10;
        vreviewFrame['Tree Prediction 100']=vTreeModPredict100;
        vreviewFrame['Tree Prediction 200']=vTreeModPredict200;
        vreviewFrame['Linear Prediction']=vLinearPredictMod;
     
        print("after pause ")
       
        print("reviewFrame.corr()");
        print(reviewFrame.corr());
        print("std")
        STD=numpy.std(reviewFrame);
        print(STD)
        
        #print(STD);
        #print("reviewFrame ")
        #print(reviewFrame);
        print("exp============")
        print("vreviewFrame.corr()");
        print(vreviewFrame.corr());
        print("vstd")
        vSTD=numpy.std(reviewFrame);
        print(vSTD)
     
        
        
        #compare(arr1,xlfxarr1,'xl');      
        return arr1;
              

def Char2Num(col):
 arr={};
 arrout=[];
 count=0;
 for member in col:
     if member in arr:
        arrout.append(arr[member]);
     else:
        arr[member]=count;
        arrout.append(arr[member]);
        count=count+1;
 return arrout;      
  
def pullNasdaqAbbreves():
  
    os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/NasdaqAbbreviations")
    mglob=str(os.listdir());
    ActivendqAdd=mglob.find("ActivendqAbbrev");
    if ActivendqAdd>-1:
       os.system('rm ActivendqAbbrev');
    
    nasdaqNativeAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"   
    nasdaqAbbreviations="http://ftp.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
    filedate=str(datetime.now().date())
    
    ndqNativeAbbrecords=str('curl '+nasdaqNativeAbbreviations+' -o nasdaqNativeAbbreviations-'+filedate)
    ActNativendqAbbrv=str('curl '+nasdaqNativeAbbreviations+' -o ActiveNativendqAbbrev')
    
    ndqAbbrecords=str('curl '+nasdaqAbbreviations+' -o nasdaqAbbreviations-'+filedate)
    ActndqAbbrv=str('curl '+nasdaqAbbreviations+' -o ActivendqAbbrev')
   
    os.system(ndqNativeAbbrecords)
    os.system(ActNativendqAbbrv)
    os.system(ndqAbbrecords)
    os.system(ActndqAbbrv)
    
      
  
def runNasdaq():
    def NasdaqMKTIndicator0(x):
        arr=[];
        count=0; 
        while count<len(x):
              arr.append(0);
              count=count+1;
        return arr;
    
    def NONnasdaqMKTIndicator(col):
        arr={};
        arrout=[];
        count=0;
        for member in col:
            if member in arr:
               arrout.append(arr[member]);
            else:
               count=count+1
               arr[member]=count;
               arrout.append(arr[member]);
        return arrout;   
        
    os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/NasdaqAbbreviations");
    try:
       NasdaqNativeAbbreviations=pandas.read_csv('ActiveNativendqAbbrev','|');
       NasdaqAbbreviations=pandas.read_csv('ActivendqAbbrev','|');
    except:
       print("Nasdaq Symbol Update Failed - Archive in use") 
       NasdaqNativeAbbreviations=pandas.read_excel('NasdaqArcaneNative.xlsx');
       NasdaqAbbreviations=pandas.read_excel('NasdaqArcaneOther.xlsx');
      
    TopSymbols=NasdaqNativeAbbreviations[["Symbol","Security Name","ETF"]];
    TopSymbols["MKT"]=NasdaqMKTIndicator0(TopSymbols);
    
    
    BottomSymbols=NasdaqAbbreviations[["ACT Symbol","Security Name","ETF"]];
    BottomSymbols["Symbol"]=BottomSymbols["ACT Symbol"];
    BottomSymbols=BottomSymbols.drop(["ACT Symbol"], axis=1);
    BottomSymbols["MKT"]=NONnasdaqMKTIndicator(NasdaqAbbreviations["Exchange"]);
    
    STKsymbols=TopSymbols.append(BottomSymbols).reset_index();
    STKsymbols=STKsymbols.drop(["index"], axis = 1);
    STKsymbols.columns=["Symbols","Security Name","ETF","MKT"];
    STKsymbols["ETF Num"]=Char2Num(STKsymbols["ETF"])

    #print(IEXColmaker())    
    print(STKsymbols) 
    
    
    
"""
['Symbols', 'Security Name', 'ETF', 'MKT', 'ETF Num','index', 'close', 'high', 'low', 'open', 'symbol', 'volume', 'id',\
 'key', 'subkey', 'date', 'updated', 'changeOverTime','marketChangeOverTime', 'uOpen', 'uClose', 'uHigh', 'uLow', 'uVolume',\
 'fOpen', 'fClose', 'fHigh', 'fLow', 'fVolume', 'label', 'change','changePercent', 'date1']    
"""
"""
['Symbols', 'Security Name', 'ETF', 'MKT', 'ETF Num', 'close', 'high', 'low', 'open', 'volume',\
  'date', 'updated', 'changeOverTime','marketChangeOverTime', 'uOpen', 'uClose', 'uHigh', 'uLow', 'uVolume',\
 'fOpen', 'fClose', 'fHigh', 'fLow', 'fVolume', 'change','changePercent']    
"""



#pullNasdaqAbbreves();
#runNasdaq();
print(IEXColmaker());

sqlTableCreate="create table main.iextransaction(Symbols text,SecurityName text,ETF  text,MKT real,ETFNum  real,close real,high real,low real,open real,volume real,date real,updated real,changeOverTime real,marketChangeOverTime real,uOpen real,uClose real,uHigh real,uLow real,uVolume real,fOpen real,fClose real,fHigh real,fLow real,fVolume real,change real,changePercent real)"   
#os.system("sqlite3");

#os.system(sqlTableCreate);
#os.system(.exit);

#---------------------------------------------------------------------------------------------------------------
"""
    
    def nasdaqTester():
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------")
        #brokenlines=[];
        responseCode=[];
        columnsOfNasdaqNativeAbbreviation=NasdaqAbbreviations.columns
        NasdaqTesFrame=NasdaqAbbreviations['CQS Symbol'];
        print(type(NasdaqTesFrame))
        print(NasdaqTesFrame)
        sze=len(NasdaqTesFrame)
        lineItem=0;
        errCount=0;
       
       #while (lineItem < 10):
        #    nums=NasdaqAbbreviations['CQS Symbol'][lineItem];
        #print(NasdaqTesFrame)
      
        for nums in NasdaqAbbreviations['CQS Symbol']:
          
            test="https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e"
                     
   #ACTIVATE FOR REAL DATA0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000         
            #test="https://cloud.iexapis.com/stable/stock/"+str(nums)+"/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
            rtest=requests.get(test); 
            if (str(rtest).find("200")>0):
                errCount=errCount+str(rtest).find("200"); 
            
            print(str(rtest).find("200"));
            #brokenlines.append(lineItem);
            responseCode.append(rtest);
            print(str(rtest)+"   "+str(lineItem)+" of "+str(sze));
            lineItem=lineItem+1;
        NasdaqTesFrame=pandas.DataFrame(NasdaqTesFrame,columns=['CQS Symbol']); 
        
        print("NasdaqTesFrame")
        print(NasdaqTesFrame)
        #NasdaqTesFrame['broken line numbers']=brokenlines;
        NasdaqTesFrame['response Code']=responseCode;
        print(type(NasdaqTesFrame)) 
        print(NasdaqTesFrame.columns)
        print(NasdaqTesFrame) 
        print("errCount = "+str(errCount))
        print(os.getcwd())
        os.chdir("/GMDelight/GMDelight/Sheets/rememberGME/GMEouts")
        print(os.getcwd())
        print(os.listdir())
        NasdaqExp=pandas.read_excel('gmetemplate.xlsx')
        print(NasdaqExp)
        NasdaqTesFrame.to_excel(r'gmetemplate.xlsx',index=False)
        #NasdaqExp=pandas.reprint("NasdaqExp.columns")ad_excel('gmetemplate.xlsx')
        print(NasdaqExp)
        print("NasdaqExp.columns")
        print(NasdaqExp.columns)
        
        print("---------------------------------------------------------------------")
        print("---------------------------------------------------------------------")
    trd=threading.Thread(target=nasdaqTester);
    trd.start();
    #NasdaqTesFrame['broken line numbers']=brokenlines;
    #NasdaqTesFrame['response Code']=responseCode;
    #print(NasdaqTestFrame)
    
    
    #print(NasdaqAbbreviations);
    
    #print(NasdaqNativeAbbreviations);
    #print(NasdaqAbbreviations['CQS Symbol'])
    #print("columnsOfNasdaqNativeAbbreviation "+str(columnsOfNasdaqNativeAbbreviation))
    
    return NasdaqNativeAbbreviations;


chartIEXdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
#chartIEXdata="https://cloud.iexapis.com/stable/stock/XOM/chart/1m?token=pk_2a5af8857a7940d4b361bc2b4a14d0ad"
#chartIEXdata="https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e"

#https://sandbox.iexapis.com/stable/stock/AMD/dividends/1y?token=Tpk_ae999384a70348b3855e8904d4c46e5e
#https://sandbox.iexapis.com/stable/stock/AMD/chart/1m?token=Tpk_ae999384a70348b3855e8904d4c46e5e

workingChartData=requests.get(chartIEXdata).json()
def columnMaker(columndata,columnName):
    newCol=[];
    x=columndata;
    y=columnName;
    newCol.append(y);
    for days in x:
        fi=str(type(days[y])).find('int');
        ff=str(type(days[y])).find('float');
        fff=ff+fi;
        if fff<=-2:
           newCol.append(0.0); 
        else:
           newCol.append(days[y]);
    newCol=pandas.DataFrame(newCol, columns=[y]);
    return newCol;                        
        


def MonthTableMaker(chartData):
    PreFrame=[]; 
    x=chartData;
    names=list(x[0].keys());
    for columns in list(x[0]):
        PreFrame.append(columnMaker(x,columns));
    NewFrame=pandas.DataFrame(PreFrame[0], columns=[names[0]])
    cnt=0;
    while cnt<len(PreFrame)-1:
        cnt=cnt+1;
        NewFrame[names[cnt]]=PreFrame[cnt];
    NewFrame=NewFrame.drop([0]);
    print("Month Maker")
    print(NewFrame);
    return NewFrame;
 
#MonthTableMaker(workingChartData); 
def TableGen():
    print("TableGen Run")
    #MonthTableMaker(workingChartData);
    runNasdaq();
    ready=MonthTableMaker(workingChartData).to_html
    #return ready
TableGen();
"""    
    
     
     






