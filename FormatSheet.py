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
            return readActiveSheet;
        aSP=activeSheetParse(readActiveSheet);
        ListOfFrames.append(aSP);
        lCount=lCount+1;
  print("00000000000000000000000000000000000000000000000011111111111111") 
  print("00000000000000000000000000000000000000000000000011111111111111") 
  print(ListOfFrames);  
  print("len(ListOfFrames) ",len(ListOfFrames))
  print("00000000000000000000000000000000000000000000000022222222222222") 
  print("00000000000000000000000000000000000000000000000022222222222222") 
  return ActiveSheets;


def RegCorDescShift(x):
    print("headers() regcordescshift ");  

RegCorDescShift(headers());
      
    








