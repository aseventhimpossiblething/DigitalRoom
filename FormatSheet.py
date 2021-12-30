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
plt.tight_layout();

def headers():
  os.chdir('/GMDelight/DigitalRoom/static/');
  if os.path.exists("heatmap.png"):
       os.remove("heatmap.png");
  if os.path.exists("selectedFrame.png"):    
       os.remove("selectedFrame.png");
  if os.path.exists("rpt.html"):    
       os.remove("rpt.html");    
  #print("Headers called 1")
  os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  ActiveSheets=os.listdir();
  numOfSheets=len(ActiveSheets);
  if numOfSheets==0:
     return "Enter a single csv or xlsx sheet. - DO NOT ENTER A MULTISHEET WORKBOOK! "
  ListOfFrames=[];
  lCount=0;
  while lCount < numOfSheets:
        #readActiveSheet="";
        ActiveSheet=ActiveSheets[lCount];
        #print("Headers called 2")
        #print("Headers called active sheet ",ActiveSheet)
        isxlsx=ActiveSheet.lower().find(".xlsx");
        iscsv=ActiveSheet.lower().find(".csv");
        readActiveSheet="Drop9";
        if isxlsx > 1:
              readActiveSheet=pandas.read_excel(ActiveSheet); 
        if iscsv > 1:
              readActiveSheet=pandas.read_csv(ActiveSheet); 
              readActiveSheet=pandas.DataFrame(data=readActiveSheet);
        
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
                                       
                     #can delete below-----------------------------
                     #print("type dcolumn-", type(dcolumn));
                     #Newdict=dcolumn.to_dict();
                     #print("type Newdict ",type(Newdict));
                     #dcolumnEX=numpy.array(dcolumn);
                     #print("HHHHH lll end ",(dcolumnEX=='xo').sum());
                     #print( Newdict)
                     #can delet above------------------------------ 
                     
                     print(col," is catagorical cat process run");
                     catcount=0;
                     while catcount<len(dcolumn):
                           individual_element=dcolumn[catcount];
                           DictIndexNum=strAsKeyDict[individual_element];
                           Nums_As_KeyDict=dcolumn.to_dict();
                           Nums_As_KeyDict[DictIndexNum];
                           NovelCats.append(DictIndexNum); 
                           #NewQcats.append(catcount);
                           #print("catcount ",catcount); 
                           #print("DictIndexNum ",DictIndexNum); 
                           #print("strAsKeyDict[individual_element] ",strAsKeyDict[individual_element]);
                           #print("individual_element ",individual_element); 
                           #print("Nums_As_KeyDict[DictIndexNum] ",Nums_As_KeyDict[DictIndexNum]); 
                           #catnum=str(OldQcats).find(str(dcolumn[catcount]));
                           """                          
                           if catnum>-1:
                              NewQcats.append(catnum)
                           if catnum<0: 
                              OldQcats.append(dcolumn[catcount]);
                              NewQcats.append(catcount);
                           """
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
  """
  print("00000000000000000000000000000000000000000000000011111111111111") 
  print("00000000000000000000000000000000000000000000000011111111111111") 
  print(ListOfFrames);  
  print("len(ListOfFrames) ",len(ListOfFrames))
  print("00000000000000000000000000000000000000000000000022222222222222") 
  print("00000000000000000000000000000000000000000000000022222222222222") 
  #return ActiveSheets;
  """
  return ListOfFrames;


def RegCorDescShift():
    os.chdir('/GMDelight/DigitalRoom/static/');
    if os.path.exists("heatmap.png"):
       os.remove("heatmap.png");
    if os.path.exists("selectedFrame.png"):    
       os.remove("selectedFrame.png");
    if os.path.exists("rpt.html"):    
       os.remove("rpt.html");    
        
    
    #headers() 
    #print("headers() regcordescshift ",headers());
    selected=headers()[0];
    #print("selectedFrame");
    #print(selectedFrame);
    
    #selectedFrame=selected.dropna(axis=1);
    selectedFrame=selected
    #print(selectedFrame);
    columns=selectedFrame.columns;
    #print("columns - ",columns);
    #print("columns[0] - ",columns[0]);
    catModes=[];
    colNames=[];
    colcounts=[];
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
         
         #print("colName ",colName);
         reviewcol=selectedFrame[colName];
         guard1=str(reviewcol.dtype).find('object')
         guard2=str(reviewcol.dtype).find('str') 
         guardVar=guard1+guard2;
         #print("dtype ",reviewcol.dtype);
         #print("guard ",guardVar);
         
         #guardVar<-1; 
         if guardVar==-2: 
          #print("Passed the Guard")
          colName=columns[colrcount];
          colNames.append(colName)
          #print("colName  ",colName,"Passed the Guard");
          reviewcol=selectedFrame[colName];
          #colMode=reviewcol.mode();
          #colMode=statistics.multimode(list(reviewcol));
          #print("mode ",colMode)
          #colModes.append(colMode);
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
          #print("mode ",colMode)
          #colModes.append(colMode);
          colModes.append(colMode);
          
          def AboveBelowMean(x):
              """
              try:
                print("running ",x.columns)
              except:
                print("Cols value not available")
              """
              #print("type ",type(x)) 
              #print("running mean ",x.mean()) 
              valuesAboveMean=[];
              valuesBelowMean=[];
              HPCounter=0;
              while HPCounter<len(x):
                    #print("") 
                    elem=x[HPCounter];
                    if elem>x.mean():
                       valuesAboveMean.append(elem);
                    if elem<x.mean():    
                       valuesBelowMean.append(elem); 
                    HPCounter=HPCounter+1;
              return [valuesAboveMean,valuesBelowMean];       
          splitAtMean=AboveBelowMean(reviewcol);
          #print("splitAtMean[0] ",splitAtMean[0])
          print("type splitAtMean[0] ",type(splitAtMean[0]))
          UpperHalf=splitAtMean[0]
          #AboveBelowMean(UpperHalf);
          print("type UpperHalf ",type(UpperHalf))
          UpperQuartilesAtMean=AboveBelowMean(UpperHalf)[0];
          #UpperQuartilesAtMean[0]
          print('UpperQuartilesAtMean ',UpperQuartilesAtMean);
          print('UpperQuartilesAtMean ',UpperQuartilesAtMean);
          #LowerQuartilesAtMean=AboveBelowMean(pandas.DataFrame(splitAtMean[1]));
          #HighstQuartile=pandas.DataFrame(UpperQuartilesAtMean[0]);
          #LowestQuartile=pandas.DataFrame(LowerQuartilesAtMean[1]);
          #print("splitArr ",splitArr);
          #print("splitArr[0] ",splitArr[0]);
          #print("splitArr[1] ",splitArr[1]);
         else:
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
    print("len cat modes ",len(catModes))
    print("len colNames ",len(colNames))
    print("colcounts ",len(colcounts))
    print("colSums ",len(colSums))
    print("coledians ",len(colMedians))
    print("colMeans ",len(colMeans))
    print("colMods ",len(colModes))
    print("colSTDs ",len(colSTDs))
    print("colMaxs ",len(colMaxs))
    print("colranges ",len(colranges))
    print("colMins ",len(colMins))
    print("colranges ",len(colranges))
    print("Trimmed05s ",len(Trimmed05s))
    print("Trimmed10s ",len(Trimmed10s))
    print("Trimmed15s ",len(Trimmed15s))
    #colrcount=0;
    print(" cat modes ",catModes);
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
         #print("len(x) ",len(x))
         #print("wMode ",wMode)
         #print("mCount ",mCount)
         #fCounts.append(wMode);
         lineCount=0;
         while lineCount<len(FullCol):
              colElem=FullCol[lineCount];
              if colElem==wMode:
               colModeReps.append(colElem);
              lineCount=lineCount+1;
         ModeCount=len(colModeReps);
         fCounts.append(ModeCount);
         #print("Mode ",wMode," size ",ModeCount);
         #print("fCounts ",fCounts," size ",len(fCounts));
         
         mCount=mCount+1;
      return fCounts;
    catModCount=modeCounter(colNames,catModes,selected); 
    #print("catModCount ",catModCount)
    
    
    #DescriptiveTable=pandas.DataFrame({'Descriptive_Statistic':colNames,'N':colcounts,'Sum':colSums,'Median':colMedians,'Mean':colMeans,'#Mode':colModes,'Catagorical Modes':catModes,'Std_Deviation':colSTDs,'Max':colMaxs,'Min':colMins,'5%_Trimmed_Mean':Trimmed05s,'10%_Trimmed_Mean':Trimmed10s,'15%_Trimmed_Mean':Trimmed15s,'Range':colranges});
    DescriptiveTable=pandas.DataFrame({'Descriptive_Statistic':colNames,'N':colcounts,'Median':colMedians,'Mean':colMeans,'#Mode':colModes,'Catagorical_Modes':catModes,'Count_Of_Prime_Mode':catModCount,'Std_Deviation':colSTDs,'Max':colMaxs,'Min':colMins,'5%_Trimmed_Mean':Trimmed05s,'10%_Trimmed_Mean':Trimmed10s,'15%_Trimmed_Mean':Trimmed15s,'Range':colranges});
      
    #print("DescriptiveTable");
    #print("DescriptiveTable");
    #print(DescriptiveTable);
    DescriptiveTableTB=DescriptiveTable.to_html();
    
    relations=selectedFrame.corr();
    seaborn.heatmap(relations);
    os.chdir('/GMDelight/DigitalRoom/static/');
    plt.savefig("heatmap.png",bbox_inches='tight' )
    
    selectedFrame.plot(kind='hist');
    plt.savefig("selectedFrame.png")
    print("image saved")
    #print("type relations",type(relations));
    
    lorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    
    page="<html><header><style>#title{text-align:center; font-weight:bold; font-size:20px; margin-bottom:80px;}#cortab{margin-top: 25px;}#right{float:right; width:15%; background-color:blue;}#left{float:left; width:15%; background-color:red;}</style></header><div id='title'>Statistical Overview</div><div id='right'><img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div id='left'><img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div>"+DescriptiveTableTB+"</div><div id='cortab'>"+relations.to_html()+"</div></html>"
    #page="<html><header><style>#cortab{margin-top: 25px;}</style></header><div>Statistical Overview</div><div>"+DescriptiveTableTB+"</div><div id='right'><img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div id='left'><img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div id='cortab'>"+relations.to_html()+"</div></html>"
    page="<html><header><style>th{background-color:blue; color:white;}tr:nth-child(even){background-color:blue; color:white;}#title{text-align:center; font-weight:bold; font-size:20px; margin-bottom:80px;}#cortab{margin-top: 25px;}#right{float:right; width:15%; background-color:blue;}#left{float:left; width:15%; background-color:red;}</style></header><div id='title'>Statistical Overview</div><div>"+lorem+"<img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div>"+lorem+"<img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div>"+DescriptiveTableTB+"</div><div id='cortab'>"+relations.to_html()+"</div></html>"
    
    
    report=open("rpt.html",'w');
    report.write(page);
    report.close();
    print("report loaded");
    
    
   
    return "RegCorDescShift";
  
  
  
  
def rpt():
    distalRPT=threading.Thread(target=RegCorDescShift); 
    distalRPT.start();
    return "report pending"
      
    








