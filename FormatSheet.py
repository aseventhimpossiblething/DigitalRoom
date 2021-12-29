import pandas
import os
from pandas import ExcelWriter
from pandas import ExcelFile
from scipy import stats
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
                  
                 
                  
                  NewQcats=[];
                  OldQcats=[];  
                  if Qobject>-1:
                     
                     #can delete below-----------------------------
                     print("type dcolumn-", type(dcolumn));
                     Newdict=dcolumn.to_dict();
                     print("type Newdict ",type(Newdict));
                     #print("Newdict ",Newdict); 
                     print("Newdict[0] ",Newdict[0]); 
                     print("Newdict[1] ",Newdict[1]);  
                     print("Newdict[2] ",Newdict[2]); 
                     dcolumnEX=numpy.array(dcolumn);
                     print("HHHHH lll end ",(dcolumnEX=='xo').sum());
                     #print( Newdict)
                      
                     #can delet above------------------------------ 
                     
                     print(col," is catagorical cat process run");
                     catcount=0;
                     while catcount<len(dcolumn):
                           dcolumn[catcount];
                           ind_elementName=Newdict[catcount];
                           catnum=str(OldQcats).find(str(dcolumn[catcount]));
                           if catnum>-1:
                              NewQcats.append(catnum)
                           if catnum<0: 
                              OldQcats.append(dcolumn[catcount]);
                              NewQcats.append(catcount);
                           
                           #NewQcats.append(catcount);
                           catcount=catcount+1;
                     ncolnam=str(col)+"_as_Cat_Var";      
                     readActiveSheet[ncolnam]=NewQcats; 
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
    selectedFrame=headers()[0];
    #print("selectedFrame");
    #print(selectedFrame);
    selectedFrame=selectedFrame.dropna(axis=1);
    print(selectedFrame);
    columns=selectedFrame.columns;
    #print("columns - ",columns);
    #print("columns[0] - ",columns[0]);
    colNames=[];
    colcounts=[];
    colSums=[];
    colMedians=[];
    colMeans=[];
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
         colrcount=colrcount+1; 
    
    DescriptiveTable=pandas.DataFrame({'Descriptive_Statistic':colNames,'N':colcounts,'Sum':colSums,'Median':colMedians,'Mean':colMeans,'Std_Deviation':colSTDs,'Max':colMaxs,'Min':colMins,'5%_Trimmed_Mean':Trimmed05s,'10%_Trimmed_Mean':Trimmed10s,'15%_Trimmed_Mean':Trimmed15s,'Range':colranges});
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
    page="<html><header><style>#title{text-align:center; font-weight:bold; font-size:20px; margin-bottom:80px;}#cortab{margin-top: 25px;}#right{float:right; width:15%; background-color:blue;}#left{float:left; width:15%; background-color:red;}</style></header><div id='title'>Statistical Overview</div><div>"+lorem+"<img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div>"+lorem+"<img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div>"+DescriptiveTableTB+"</div><div id='cortab'>"+relations.to_html()+"</div></html>"
    
    
    report=open("rpt.html",'w');
    report.write(page);
    report.close();
    print("report loaded");
    
    
   
    return "RegCorDescShift";
  
  
  
  
def rpt():
    distalRPT=threading.Thread(target=RegCorDescShift); 
    distalRPT.start();
    return "report pending"
      
    








