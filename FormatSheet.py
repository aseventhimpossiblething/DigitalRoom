import pandas
import os
from pandas import ExcelWriter
from pandas import ExcelFile
from scipy import stats
import statistics
import seaborn
import matplotlib.pyplot as plt
import threading
import numpy
import sys
plt.tight_layout();

def modeCounter(IdCol,ModeCol,InitialTable):
      print("modeCounter running?------------------------")
      print("modeCounter running?------------------------")
      x=IdCol;
      y=ModeCol;
      z=InitialTable;
      mCount=0;
      fCounts=[];
      while mCount<len(x):
         wMode=y[mCount];
         ColName=x[mCount];
         FullCol=z[ColName];
         colModeReps=[];
         lineCount=0;
         while lineCount<len(FullCol):
              colElem=FullCol[lineCount];
              if colElem==wMode:
               colModeReps.append(colElem);
              lineCount=lineCount+1;
         ModeCount=len(colModeReps);
         fCounts.append(ModeCount);
         mCount=mCount+1;
      return fCounts;

def headers():
  
  os.chdir('/GMDelight/DigitalRoom/static/');
  if os.path.exists("heatmap.png"):
       os.remove("heatmap.png");
  if os.path.exists("selectedFrame.png"):    
       os.remove("selectedFrame.png");
  if os.path.exists("rpt.html"):    
       os.remove("rpt.html");    
  os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  if os.path.exists("heatmap.png"):
       os.remove("heatmap.png");
  if os.path.exists("selectedFrame.png"):    
       os.remove("selectedFrame.png");
  if os.path.exists("rpt.html"):    
       os.remove("rpt.html");
  if os.path.exists("BlankSheet"):    
       os.remove("BlankSheet");    
   
  #os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  ActiveSheets=os.listdir();
  print('ActiveSheets ',ActiveSheets);
  if ActiveSheets==[]:
    print("Empty slot! 3 brackets");
    print("list dir",os.listdir());
    os.system("> BlankSheet")
  if ActiveSheets==[ ]:
    print("Empty slot! 4 space brackets");
    print("list dir",os.listdir());
    
  numOfSheets=len(ActiveSheets);
  """
  print("numOfSheets = ",numOfSheets)
  if numOfSheets<1:
     print("Sheet number found to be 0") 
     return "Enter a single csv or xlsx sheet. - DO NOT ENTER A MULTISHEET WORKBOOK! "
  """
  ListOfFrames=[];
  #print("",ListOfFrames)
  lCount=0;
  while lCount < numOfSheets:
        ActiveSheet=ActiveSheets[lCount];
        isxlsx=ActiveSheet.lower().find(".xlsx");
        iscsv=ActiveSheet.lower().find(".csv");
        readActiveSheet="Drop9";
        if isxlsx > 1:
              os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
              print('xlsx listdir ',os.listdir());
              print('ActiveSheet ',ActiveSheet);
              readActiveSheet=pandas.read_excel("/GMDelight/DigitalRoom/Sheets/CTRData"+"/"+ActiveSheet);
              #print("len(readActiveSheet) -- ",len(readActiveSheet));
              #readActiveSheet=pandas.read_excel(ActiveSheet); 
        if iscsv > 1:
              readActiveSheet=pandas.read_csv(ActiveSheet); 
              readActiveSheet=pandas.DataFrame(data=readActiveSheet);
        
        print("len(readActiveSheet) -- ",len(readActiveSheet));
        os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
        if len(readActiveSheet)==0:
           os.system("> BlankSheet")
           print("list dir ln 71 ",os.getcwd()); 
           print("list dir ln 71 ",os.listdir());
           #print("",):
           sys.exit();
            
        
        def activeSheetParse(readActiveSheet):
            TypereadActiveSheet=str(type(readActiveSheet)).find('str');
            if TypereadActiveSheet>-1:
               return "Empty_File";
            strconv=str(readActiveSheet.columns)
            strconv=strconv.replace("Index(","");
            strconv=strconv.replace("dtype='object')","");
            strconv=strconv.replace("'","");
            strconv=strconv.replace("]","");
            strconv=strconv.replace("[","");
            strconv=strconv.replace(", ",",");
            if strconv.replace(",","")=="":
               return "Empty_File";
            l2count=0;
            while l2count<len(readActiveSheet.columns):
                  col=readActiveSheet.columns[l2count];
                  dcolumn=readActiveSheet[col];
                  coltype=str(dcolumn.dtypes);
                  Qobject=coltype.find('object');
                                   
                  NewKeysDictWords=[];
                  NewValuesDictNums=[];
                  NovelCats=[];
                  NewQcats=[];
                  OldQcats=[];  
                  if Qobject>-1:
                     NDictCount=0;
                     while NDictCount<len(dcolumn):
                           individual_element=dcolumn[NDictCount];
                           NewKeysDictWords.append(individual_element);
                           NewValuesDictNums.append(NDictCount);
                           NDictCount=NDictCount+1;
                     ReverseDict=zip(NewKeysDictWords,NewValuesDictNums); 
                     strAsKeyDict=dict(ReverseDict);
                  
                     catcount=0;
                     while catcount<len(dcolumn):
                           individual_element=dcolumn[catcount];
                           DictIndexNum=strAsKeyDict[individual_element];
                           Nums_As_KeyDict=dcolumn.to_dict();
                           Nums_As_KeyDict[DictIndexNum];
                           NovelCats.append(DictIndexNum); 
                           
                           catcount=catcount+1;
                     ncolnam=str(col)+"_as_Cat_Var";      
                     #readActiveSheet[ncolnam]=NewQcats;
                     readActiveSheet[ncolnam]=NovelCats;
                  l2count=l2count+1;
            return readActiveSheet;
        aSP=activeSheetParse(readActiveSheet);
        EmptyQ=str(aSP).find("Empty_File");
        if EmptyQ<0:
           ListOfFrames.append(aSP);
       
        lCount=lCount+1;
  return ListOfFrames;


def RegCorDescShift():
    os.chdir('/GMDelight/DigitalRoom/static/');
    if os.path.exists("heatmap.png"):
       os.remove("heatmap.png");
    if os.path.exists("selectedFrame.png"):    
       os.remove("selectedFrame.png");
    if os.path.exists("rpt.html"):    
       os.remove("rpt.html");  
    
    selected=headers()[0];
    print("selected ",selected)
    selectedFrame=selected
    
    try:
      columns=selectedFrame.columns;
    except:
      print("end of try fail ");
      page="Enter a single csv or xlsx sheet. - DO NOT ENTER A MULTISHEET WORKBOOK! Please Retry"
      sys.exit(); 
    catModes=[];
    colNames=[];
    colcounts=[];
    NoAboveMeanArr=[];
    NoBelowMeanArr=[];
    NofUpperQuartileArr=[];
    NofLowerQuartileArr=[];
    colSums=[];
    colMedians=[];
    colMeans=[];
    colModes=[];
    colSTDs=[];
    colMaxs=[];
    colMins=[];
    colranges=[];
    Trimmed05s=[];
    Trimmed10s=[];
    Trimmed15s=[];
    colrcount=0;
    while colrcount<len(columns):
         colName=columns[colrcount]; 
         catMode=statistics.mode(list(selected[colName]));
         catModes.append(catMode);
         
         reviewcol=selectedFrame[colName];
         guard1=str(reviewcol.dtype).find('object')
         guard2=str(reviewcol.dtype).find('str') 
         guardVar=guard1+guard2;
        
         if guardVar==-2: 
          colName=columns[colrcount];
          colNames.append(colName)
          reviewcol=selectedFrame[colName];
          colcount=len(reviewcol);
          colcounts.append(colcount);
          colSum=reviewcol.sum();
          colSums.append(colSum);
          colMedian=reviewcol.median(skipna=True);
          colMedians.append(colMedian);
          colMean=reviewcol.mean();
          colMeans.append(colMean);
          colSTD=reviewcol.std();
          colSTDs.append(colSTD);
          colMax=reviewcol.max();
          colMaxs.append(colMax);
          colMin=reviewcol.min();
          colMins.append(colMin);
          colrange=colMax-colMin;
          colranges.append(colrange);
          Trimmed05=stats.trim_mean(reviewcol,0.05);
          Trimmed05s.append(Trimmed05);
          Trimmed10=stats.trim_mean(reviewcol,0.10);
          Trimmed10s.append(Trimmed10);
          Trimmed15=stats.trim_mean(reviewcol,0.15);
          Trimmed15s.append(Trimmed15); 
          colMode=statistics.multimode(list(reviewcol));
          if colcount>len(colMode)-1:
             colMode="-";
          colModes.append(colMode);
          
          def AboveBelowMean(x):
              Vartype=type(x);
              SeekStr=str(Vartype).find('str');
              valuesAboveMean=[];
              valuesBelowMean=[];
              HPCounter=0;
              while HPCounter<len(x):
                    mean=statistics.mean(x);
                    elem=x[HPCounter];
                    if elem>mean:
                        valuesAboveMean.append(elem);
                    if elem<mean:
                       valuesBelowMean.append(elem); 
                    HPCounter=HPCounter+1;
              return [valuesAboveMean,valuesBelowMean];       
          splitAtMean=AboveBelowMean(reviewcol);
          UpperHalf=splitAtMean[0];
          LowerHalf=splitAtMean[1];
          UpperQuartileAtMean=AboveBelowMean(UpperHalf)[0];
          LowerQuartileAtMean=AboveBelowMean(LowerHalf)[1];
          NofUpperhalf=len(UpperHalf)
          NoFLowerhalf=len(LowerHalf)          
          NofUpperQuartile=len(UpperQuartileAtMean);
          NofLowerQuartile=len(LowerQuartileAtMean);
          
          NoAboveMeanArr.append(NofUpperhalf);
          NoBelowMeanArr.append(NoFLowerhalf);
          NofUpperQuartileArr.append(NofUpperQuartile);
          NofLowerQuartileArr.append(NofLowerQuartile);
         else:
          NoAboveMeanArr.append("-");
          NoBelowMeanArr.append("-");
          NofUpperQuartileArr.append("-");
          NofLowerQuartileArr.append("-");
          
          colcount=len(reviewcol);
          colcounts.append(colcount);
          colNames.append(colName);
          colMode=statistics.multimode(list(reviewcol));
          if len(colMode)>colcount-1:
            colMode="-";
          colModes.append(colMode);
          
          colMedian="-";
          colMedians.append(colMedian);
          colMean="-";
          colMeans.append(colMean);
          colSTD="-";
          colSTDs.append(colSTD);
          colMax="-";
          colMaxs.append(colMax);
          colMin="-";
          colMins.append(colMin);
          colrange="-";
          colranges.append(colrange);
          Trimmed05="-";
          Trimmed05s.append(Trimmed05);
          Trimmed10="-";
          Trimmed10s.append(Trimmed10);
          Trimmed15="-";
          Trimmed15s.append(Trimmed15); 
         colrcount=colrcount+1; 
    
    """
    def modeCounter(IdCol,ModeCol,InitialTable):
      x=IdCol;
      y=ModeCol;
      z=InitialTable;
      mCount=0;
      fCounts=[];
      while mCount<len(x):
         wMode=y[mCount];
         ColName=x[mCount];
         FullCol=z[ColName];
         colModeReps=[];
         lineCount=0;
         while lineCount<len(FullCol):
              colElem=FullCol[lineCount];
              if colElem==wMode:
               colModeReps.append(colElem);
              lineCount=lineCount+1;
         ModeCount=len(colModeReps);
         fCounts.append(ModeCount);
         mCount=mCount+1;
      return fCounts;
    """
    print("Start modeCounter ------------------------")  
    catModCount=modeCounter(colNames,catModes,selected);
    print("After modeCounter ------------------------")    
 
    
    #DescriptiveTable=pandas.DataFrame({'Descriptive_Statistic':colNames,'N':colcounts,'Sum':colSums,'Median':colMedians,'Mean':colMeans,'#Mode':colModes,'Catagorical Modes':catModes,'Std_Deviation':colSTDs,'Max':colMaxs,'Min':colMins,'5%_Trimmed_Mean':Trimmed05s,'10%_Trimmed_Mean':Trimmed10s,'15%_Trimmed_Mean':Trimmed15s,'Range':colranges});
    DescriptiveTable=pandas.DataFrame({'Descriptive_Statistic':colNames,'N':colcounts,'Median':colMedians,'Mean':colMeans,'#Mode':colModes,'Catagorical_Modes':catModes,'Count_Of_Prime_Mode':catModCount,'Std_Deviation':colSTDs,'Max':colMaxs,'Min':colMins,'5%_Trimmed_Mean':Trimmed05s,'10%_Trimmed_Mean':Trimmed10s,'15%_Trimmed_Mean':Trimmed15s,'Range':colranges,'#_Above_Mean':NoAboveMeanArr,'#_Below_Mean':NoBelowMeanArr,'Distal_Quartile>Mean':NofUpperQuartileArr,'Distal_Quartile<Mean':NofLowerQuartileArr});
    DescriptiveTableTB=DescriptiveTable.to_html();
    
    relations=selectedFrame.corr();
    seaborn.heatmap(relations);
    os.chdir('/GMDelight/DigitalRoom/static/');
    plt.savefig("heatmap.png",bbox_inches='tight' )
    
    selectedFrame.plot(kind='hist');
    plt.savefig("selectedFrame.png")
    print("image saved")
   
    lorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    lorem1=""
    lorem2=""
    #page="<html><header><style>#title{text-align:center; font-weight:bold; font-size:20px; margin-bottom:80px;}#cortab{margin-top: 25px;}#right{float:right; width:15%; background-color:blue;}#left{float:left; width:15%; background-color:red;}</style></header><div id='title'>Statistical Overview</div><div id='right'><img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div id='left'><img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div>"+DescriptiveTableTB+"</div><div id='cortab'>"+relations.to_html()+"</div></html>"
    #page="<html><header><style>#cortab{margin-top: 25px;}</style></header><div>Statistical Overview</div><div>"+DescriptiveTableTB+"</div><div id='right'><img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div id='left'><img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div id='cortab'>"+relations.to_html()+"</div></html>"
    page="<html><header><style>th{background-color:blue; color:white;}tr:nth-child(even){background-color:blue; color:white;}#title{text-align:center; font-weight:bold; font-size:20px; margin-bottom:80px;}#cortab{margin-top: 25px;}#right{float:right; width:15%; background-color:blue;}#left{float:left; width:15%; background-color:red;}</style></header><div id='title'>Statistical Overview</div><div>"+lorem1+"<img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div>"+lorem2+"<img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div>"+DescriptiveTableTB+"</div><div id='cortab'>"+relations.to_html()+"</div></html>"
    report=open("rpt.html",'w');
    report.write(page);
    report.close();
    print("report loaded");
    return "RegCorDescShift";

def rpt():
    distalRPT=threading.Thread(target=RegCorDescShift); 
    distalRPT.start();
    return "report pending"
      
    








