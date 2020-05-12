from openpyxl import Workbook
from openpyxl import load_workbook
import xlrd
import xlsxwriter
import glob
import chardet
import os
import numpy
import scipy
import pandas
import re
from sklearn.ensemble import RandomForestRegressor

def googConverterReverse(X):
    print("_______________________________________________")
    print("GoogConverterReverse Running")    
    Temp=X;
    cols=Temp.columns
    print("initial cols ",cols)
    New_cols=[];
    for col in cols:
        col=str(col).replace('CPA','Cost / conv.').replace("'","").replace('Bid','Max.CPC').\
          replace('Spend','Cost').replace('Conv.','Conversions').replace('Top Impr. Share','Search top IS').replace('Absolute Top Impression Share','Search abs. top IS').replace('Impr. share (IS)','Search impr. share').replace('Qual. Score','Quality Score').replace('IS lost to rank','Search lost IS (rank)').replace(']','').replace('[','')
        
        New_cols.append(col);
    print("array ",New_cols) 
    Temp.columns=New_cols
    print("final cols ",Temp.columns)  
    print("GoogConverterReverse end") 
    print("_______________________________________________")
    return Temp
   



def Match_num(x):
        Temp=x
        ccountr=0;
        Match_Type=[];
        for kw in Temp['Match type']:
               kw=kw.lower() 
              
               if kw.find("exact")>-1:
                kw="1";
               if kw.find('broad')>-1:
                kw="2";
               if str(Temp['Campaign'][ccountr]).lower().find("gppc")>-1:
                #print(type(kw))
                kw=int(kw)
                kw=kw*1000;
               Match_Type.append(int(kw))
               ccountr+=1;
        return Match_Type   
               
 
            
def MarketNumberGen(_Temp_):
        Temp=_Temp_
        Market=[];
        TempMarketCount=0;
        while TempMarketCount< len(Temp['Ad group']):
                kw=Temp['Ad group'][TempMarketCount]
                if str(re.search('>\d+',kw)).find("None")!=-1:
                      kw=Temp['Campaign'][TempMarketCount]
                      if str(re.search('>\d+',kw)).find("None")!=-1:  
                         kw="match='>0";
                kw=str(re.search('>\d+',kw))
                targLoc=kw.find("match='>")
                kw=kw[targLoc:].replace("match='>","").replace("'>","")
                Market.append(kw)
                TempMarketCount+=1;
        return Market        
                        
            
def MkNewBid(x):
    PredVar='Changes'
    Temp=x;
    Bid=Temp['Bid'];
    Changes=Temp[PredVar];
    New_Bid=[];
    count=0;
    while count<len(Bid):
          thebid=(Bid[count]*Changes[count])
          New_Bid.append(thebid)
          count+=1;
    return New_Bid

def percentIncrease(OldBid,NewBid):
    OldBid=float(OldBid);
    NewBid=float(NewBid);
    change=((NewBid/OldBid)-1);
    change=change
    return change;

def percentChangeColumn(frame):
    percentChangeCol=[];
    frame=frame;
    OldBid=frame['Bid'];
    NewBid=frame['New Bid'];
    count=0;
    for i in OldBid:
        percentChangeCol.append(percentIncrease(OldBid[count],NewBid[count]));
        count+=1;
    return percentChangeCol;


def BidOpOverview(desiCols,corecols,change):
    print("Start of Bid OverView..............................")
    print("desiCols")
    print(desiCols)
    
    PredVar=change    
    designated_Columns=desiCols;
    core_cols=corecols;
    loc=corecols.count(PredVar)
       
    if loc<1:
       print(PreVar," not present")     
       print("x.count(",PredVar, "- 2) ",loc )     
       loc=corecols.index(PredVar)
    
    loc=corecols.index(PredVar)        
    predict_colsP1=corecols[:loc]
    predict_colsP2=corecols[loc+1:]
    predict_cols=predict_colsP1+predict_colsP2
        

    os.chdir('/var/www/workPortal/Sheets/BidOpData/MachinePatternSheets/')
    Seed=pandas.read_excel('BidOpSeed.xlsx');
    Seed=pandas.DataFrame(Seed,columns=core_cols)
    Seed=Seed.replace('>','');
    Seed=Seed.replace('<',''); 
    Seed=Seed.replace('%','');
    Seed=Seed.replace("-",0).fillna(0);
    Seed=Seed.replace("--",0).fillna(0); 
    Seed=Seed.replace(" --",0).fillna(0); 
    XofSeed=Seed.drop(['Campaign','Ad group',PredVar],axis=1);
    YofSeed=Seed[PredVar]
    Model=RandomForestRegressor()
    Model.fit(XofSeed,YofSeed)
            
    Temp=pandas.read_excel('Temp.xlsx');
    Temp=Temp.replace('>','');
    Temp=Temp.replace('<','');
    Temp=Temp.replace('%','');
    Temp=Temp.replace('-',0).fillna(0); 
    Temp=Temp.replace('--',0).fillna(0); 
    Temp=Temp.replace(' --',0).fillna(0); 
    Temp['Match Number']=Match_num(Temp);
    Temp['Market Number']=MarketNumberGen(Temp)
    
    
    print('isna test')
    print("Seed Columns",Seed.columns.values)
    
    print("Temp columns",Temp.columns.values)
    
    
    """
    print(Temp.isna())
    
    print(Temp.columns.values[0])
    print(Temp.isna()[[Temp.columns.values[0]]])  
    
    print(Temp.columns.values[1])
    print(Temp.isna()[[Temp.columns.values[1]]])
    
    print(Temp.columns.values[2])
    print(Temp.isna()[[Temp.columns.values[2]]])
    
    print(Temp.columns.values[3])
    print(Temp.isna()[[Temp.columns.values[3]]])  
    
    print(Temp.columns.values[4])
    print(Temp.isna()[[Temp.columns.values[0]]])
    
    print(Temp.columns.values[5])
    print(Temp.isna()[[Temp.columns.values[5]]])
    
    print(Temp.columns.values[6])
    print(Temp.isna()[[Temp.columns.values[6]]])  
    
    print(Temp.columns.values[7])
    print(Temp.isna()[[Temp.columns.values[7]]])
    
    print(Temp.columns.values[8])
    print(Temp.isna()[[Temp.columns.values[8]]])
    
    print(Temp.columns.values[9])
    print(Temp.isna()[[Temp.columns.values[9]]])  
    
    print(Temp.columns.values[10])
    print(Temp.isna()[[Temp.columns.values[10]]])
    
    print(Temp.columns.values[12])
    print(Temp.isna()[[Temp.columns.values[12]]])
    
    print(Temp.columns.values[13])
    print(Temp.isna()[[Temp.columns.values[13]]])  
    
    print(Temp.columns.values[14])
    print(Temp.isna()[[Temp.columns.values[14]]])
    
    print(Temp.columns.values[15])
    print(Temp.isna()[[Temp.columns.values[15]]])
              
    print(Temp.columns.values[16])
    print(Temp.isna()[[Temp.columns.values[16]]])  
    
    print(Temp.columns.values[17])
    print(Temp.isna()[[Temp.columns.values[17]]])
    
    print(Temp.columns.values[18])
    print(Temp.isna()[[Temp.columns.values[18]]])
    """
                      
    
    
     
    
    
    TempForOutPut=pandas.DataFrame(Temp,columns=predict_cols);
    print("TempOut 1 ",TempForOutPut.columns.values);
    TempForOutPut=TempForOutPut.drop(['Campaign','Ad group'],axis=1);
    print("TempOut 2 ",TempForOutPut.columns.values);
    print("Temp file self  ",Temp.columns.values);
    print("Temp ",Temp['Keyword'])
    print("Temp ",Temp[['Keyword']])
    
    print(TempForOutPut)
    print(TempForOutPut[[TempForOutPut.columns.values[0],TempForOutPut.columns.values[1],TempForOutPut.columns.values[2],TempForOutPut.columns.values[3],TempForOutPut.columns.values[4],TempForOutPut.columns.values[5],TempForOutPut.columns.values[6],TempForOutPut.columns.values[7],TempForOutPut.columns.values[8],TempForOutPut.columns.values[9],TempForOutPut.columns.values[10]]])
    
    
    OutputBid=Model.predict(TempForOutPut); 
    #print('OutputBid ',OutputBid);
    #print("OutputBid['rank'] ",OutputBid[['rank']]);
    Temp[PredVar]=OutputBid; 
    if str(Temp['Campaign']).lower().find('gppc')>-1:
        Temp=googConverterReverse(X)

    print(" after predict_____________________________________")

    Temp['Change']=percentChangeColumn(Temp); 
    #print(Temp.head())

    

    Temp.to_excel("outputsheet.xlsx")
    print("outputsheet.xlsx ",pandas.read_excel("outputsheet.xlsx"))
    print('end overview')
    
    #record_async_start=open("ForestLoadingQueue.txt","w")
    #record_async_start.write("100%")

    #record_async_start.close(); 
    
    return Temp  

#print(percentChangeColumn(Temp))



"""            
Sheet_To_Be_analysed="None"
Dimension_Predicted='Changes'
ExampleSheetName='Machine.xlsx'

    record_async_start.close();         
    return Temp  
            
Sheet_To_Be_analysed="None"
Dimension_Predicted='Changes'
ExampleSheetName='Machine.xlsx'



ModelCol1=['Campaign','Ad group','Keyword','Max. CPC','Avg. CPC','Cost','Clicks','Conversions','CTR','Changes']
ModelCol2=['Cost / conv.','Impr. (Top) %','Impr. (Abs. Top) %','Search impr. share','Search lost IS (rank)','Quality Score','Match type']
ModelCol3=['Campaign','Ad group','Keyword','Max. CPC','Avg. CPC','Cost','Clicks','Conversions','CTR']
ModelColumns=ModelCol1+ModelCol2
ModelColumns_for_Analysed_Sheet=ModelCol2+ModelCol3
ColumnsToClear_for_Analysis=[Dimension_Predicted,'Campaign','Ad group','Keyword','Match type']
ColumnsToClear_for_Analysis2=['Campaign','Ad group','Keyword','Match type']

Pattern_inputModel="Empty"
Pattern_New_CPC="Empty"
X_Sheet_Analysis="Empty"



def PrepModel():      
    PatternSheet=open(ExampleSheetName, 'rb')
    Pattern_no_Frame=pandas.read_excel(PatternSheet)
    PatternSheetFramed=pandas.DataFrame(Pattern_no_Frame, columns=ModelColumns).fillna(0)
    global Pattern_New_CPC
    Pattern_New_CPC=PatternSheetFramed[Dimension_Predicted]
    global Pattern_inputModel
    Pattern_inputModel=PatternSheetFramed.drop(ColumnsToClear_for_Analysis, axis=1)
    
    
def Analysis():
    print("*******from inside analysis max ctime file***",max(glob.glob('*xlsx'),key=os.path.getctime))
    global MostRecentFile
    MostRecentFile=newFileSyntax2

      
    global Sheet_To_Be_analysed
    Sheet_To_Be_analysed=open(newFileSyntax2,'rb')
    print("type Sheet_To_Be_analysed",type(Sheet_To_Be_analysed))
    print("Sheet_To_Be_analysed",Sheet_To_Be_analysed)
    print("pandas.read_excel(newFileSyntax2)",pandas.read_excel(newFileSyntax2))
    

    
 
def Predict():
    taughtModel=RandomForestRegressor(n_estimators=25).fit(Pattern_inputModel,Pattern_New_CPC)
    outputArr=taughtModel.predict(X_Sheet_Analysis)
    #print(list(outputArr))
    return list(outputArr)

def BidOpAssist():
    PrepModel()
    Analysis()
    return list(numpy.array(Predict()))


"""



print("end of doc")


