import pandas
import os
from pandas import ExcelWriter
from pandas import ExcelFile
import seaborn
import matplotlib.pyplot as plt

def headers():
  os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  ActiveSheets=os.listdir();
  numOfSheets=len(ActiveSheets);
  if numOfSheets==0:
     return "Enter a single csv or xlsx sheet. - DO NOT ENTER A MULTISHEET WORKBOOK! "
  #print("-----------------------------------------------------------")
  #print("---calling headers-----")
  #print("numOfSheets ",numOfSheets)
  #ActiveSheets=os.listdir();
  ListOfFrames=[];
  lCount=0;
  while lCount < numOfSheets:
        ActiveSheet=ActiveSheets[lCount];
        isxlsx=ActiveSheet.lower().find(".xlsx");
        iscsv=ActiveSheet.lower().find(".csv");
        if isxlsx > 1:
              readActiveSheet=pandas.read_excel(ActiveSheet); 
        if iscsv > 1:
              readActiveSheet=pandas.read_csv(ActiveSheet); 
              readActiveSheet=pandas.DataFrame(data=readActiveSheet); 
        def activeSheetParse(readActiveSheet):
            #print("readActiveSheet.columns = ",readActiveSheet.columns);
            #print("typeof readActiveSheet.columns = ",type(readActiveSheet.columns));
            strconv=str(readActiveSheet.columns)
            strconv=strconv.replace("Index(","");
            strconv=strconv.replace("dtype='object')","");
            strconv=strconv.replace("'","");
            strconv=strconv.replace("]","");
            strconv=strconv.replace("[","");
            strconv=strconv.replace(", ",",");
            if strconv.replace(",","")=="":
               #print("emptySet!"); 
               return "Empty_File";
            #print("len(readActiveSheet.columns); ",len(readActiveSheet.columns));
            #readActiveSheet=readActiveSheet.dropna(axis=1);
            #print("len(readActiveSheet.columns); ",len(readActiveSheet.columns));
            l2count=0;
            while l2count<len(readActiveSheet.columns):
                  col=readActiveSheet.columns[l2count];
                  dcolumn=readActiveSheet[col];
                  coltype=str(dcolumn.dtypes);
                  Qobject=coltype.find('object');
                  """
                  print(" dcolumn ", dcolumn);
                  print("coltype ",coltype);
                  print("Qobject ",Qobject);
                  """
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
                     #readActiveSheet.drop([col]);
                     readActiveSheet[ncolnam]=NewQcats; 
                  """
                  print("col ",col);
                  print("dcolumn ", dcolumn);
                  print("coltype ", coltype);
                  """
                  l2count=l2count+1;
            return readActiveSheet;
        aSP=activeSheetParse(readActiveSheet);
        EmptyQ=str(aSP).find("Empty_File");
        if EmptyQ<0:
           ListOfFrames.append(aSP);
        """    
        print("EmptyQ ",EmptyQ)
        print(" str aSP ",str(aSP))
        print("type str aSP ",type(str(aSP)))
        #if aSP!="Empty_File":
        """
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
    #headers() 
    #print("headers() regcordescshift ",headers());
    selectedFrame=headers()[0];
    print("selectedFrame");
    print(selectedFrame);
    selectedFrame=selectedFrame.dropna(axis=1);
    print(selectedFrame);
    relations=selectedFrame.corr();
    seaborn.heatmap(relations);
    plt.show();
    print(relations);
    
    
    return "RegCorDescShift"; 
#RegCorDescShift();
      
    








