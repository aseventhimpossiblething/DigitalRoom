import pandas
import os
from pandas import ExcelWriter
from pandas import ExcelFile
import seaborn
import matplotlib.pyplot as plt
import threading
plt.tight_layout();

def headers():
  print("Headers called 1")
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
        print("Headers called 2")
        print("Headers called active sheet ",ActiveSheet)
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
                     print(col," is catagorical cat process run");
                     catcount=0;
                     while catcount<len(dcolumn):
                           dcolumn[catcount];
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
  
  print("00000000000000000000000000000000000000000000000011111111111111") 
  print("00000000000000000000000000000000000000000000000011111111111111") 
  print(ListOfFrames);  
  print("len(ListOfFrames) ",len(ListOfFrames))
  print("00000000000000000000000000000000000000000000000022222222222222") 
  print("00000000000000000000000000000000000000000000000022222222222222") 
  #return ActiveSheets;
  
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
    print("selectedFrame");
    print(selectedFrame);
    selectedFrame=selectedFrame.dropna(axis=1);
    print(selectedFrame);
    columns=selectedFrame.columns;
    print("columns - ",columns);
    print("columns[0] - ",columns[0]);
    reviewcolData=[];
    colrcount=0;
    while colrcount<len(columns):
          reviewcol=columns[colrcount];
          reviewcol.count();
          reviewcol.sum();
          reviewcol.median();
          reviewcol.mean();
          reviewcol.std();
          colrcount=colrcount+1; 
    
   
    relations=selectedFrame.corr();
    seaborn.heatmap(relations);
    os.chdir('/GMDelight/DigitalRoom/static/');
    plt.savefig("heatmap.png",bbox_inches='tight' )
    
    selectedFrame.plot(kind='hist');
    plt.savefig("selectedFrame.png")
    print("image saved")
    print("type relations",type(relations));
    
    
    
    page="<html><header><style>#cortab{margin-top: 25px;}#right{float:right; width:15%; background-color:blue;}#left{float:left; width:15%; background-color:red;}</style></header><div>Statistical Overview</div><div id='right'><img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div id='left'><img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div id='cortab'>"+relations.to_html()+"</div></html>"
    page="<html><header><style>#cortab{margin-top: 25px;}</style></header><div>Statistical Overview</div><div id='right'><img src='http://digitalroomfileshare.cloud/static/selectedFrame.png'></div><div id='left'><img src='http://digitalroomfileshare.cloud/static/heatmap.png'></div><div id='cortab'>"+relations.to_html()+"</div></html>"
   
    
    report=open("rpt.html",'w');
    report.write(page);
    report.close();
    print("report loaded");
    
    
   
    return "RegCorDescShift";
  
  
  
  
def rpt():
    distalRPT=threading.Thread(target=RegCorDescShift); 
    distalRPT.start();
    return "temporary"
      
    








