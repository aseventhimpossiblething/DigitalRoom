import pandas
import os
from pandas import ExcelWriter
from pandas import ExcelFile

def headers():
  os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  ActiveSheets=os.listdir();
  numOfSheets=len(ActiveSheets);
  if numOfSheets==0:
     return "Enter a single csv or xlsx sheet. - DO NOT ENTER A MULTISHEET WORKBOOK! "
  print("-----------------------------------------------------------")
  print("---calling headers-----")
  #print("numOfSheets ",numOfSheets)
  #ActiveSheets=os.listdir();
  lCount=0;
  while lCount < numOfSheets:
        ListOfFrames=[];
        ActiveSheet=ActiveSheets[lCount];
        isxlsx=ActiveSheet.lower().find(".xlsx");
        iscsv=ActiveSheet.lower().find(".csv");
        #print("ActiveSheet ",ActiveSheet);
        #print("isxlsx ",isxlsx); 
        #print("iscsv ",iscsv);
        #print(" opened ",ActiveSheet);
        #OpenActiveSheet=open(ActiveSheet,'r');
        #print("OpenActiveSheet ",OpenActiveSheet)
        if isxlsx > 1:
              readActiveSheet=pandas.read_excel(ActiveSheet); 
        if iscsv > 1:
              readActiveSheet=pandas.read_csv(ActiveSheet); 
              readActiveSheet=pandas.DataFrame(data=readActiveSheet); 
        def activeSheetParse(readActiveSheet):
            global ListOfFrames
            #ListOfFrames=[];
            #print("readActiveSheet");
            #print(readActiveSheet);
            print("readActiveSheet.columns = ",readActiveSheet.columns);
            print("typeof readActiveSheet.columns = ",type(readActiveSheet.columns));
            strconv=str(readActiveSheet.columns)
            strconv=strconv.replace("Index(","");
            strconv=strconv.replace("dtype='object')","");
            strconv=strconv.replace("'","");
            strconv=strconv.replace("]","");
            strconv=strconv.replace("[","");
            strconv=strconv.replace(", ",",");
            if strconv.replace(",","")=="":
               print("emptySet!"); 
               return "Empty_File";
            ListOfFrames.append(readActiveSheet);
            print("strconv ch 1 = ",strconv);
            strconv=strconv.split(",");
            print("strconv ch 2 = ",strconv);
            print("typeof strconv = ",type(strconv));
            print("strconv[0] = ",strconv[0]);
            print("strconv[1] = ",strconv[1]);
            l2count=0;
            """
            while l2count<len(strconv):
              hcolnam=strconv[l2count];
              if hcolnam.find("\n")>-1:
                 print("\n+7 found")
                 hcolnam=hcolnam.replace("\n       ","");
              #hcolnam=hcolnam.replace("       ","");
              hcolnam=hcolnam.replace(" ","m");
              col=readActiveSheet[hcolnam];
              print(col);
              l2count=l2count+1;
            """
            print("000000000000000000000000000000000000000000000000oooooooooooooo")
            print("000000000000000000000000000000000000000000000000oooooooooooooo") 
            print(ListOfFrames);
            print("000000000000000000000000000000000000000000000000oooooooooooooo") 
            print("000000000000000000000000000000000000000000000000oooooooooooooo") 
            print("ActiveSheetParse Finished")  
        activeSheetParse(readActiveSheet);
        lCount=lCount+1;
  return ActiveSheets;
