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
        ActiveSheet=ActiveSheets[lCount];
        isxlsx=ActiveSheet.lower().find(".xlsx");
        iscsv=ActiveSheet.lower().find(".csv");
        print("ActiveSheet ",ActiveSheet);
        #print("isxlsx ",isxlsx); 
        #print("iscsv ",iscsv);
        print(" opened ",ActiveSheet);
        OpenActiveSheet=open(ActiveSheet,'r');
        if isxlsx > 1:
              readActiveSheet=pandas.read_excel(ActiveSheet); 
        if iscsv > 1:
              #readActiveSheets=open(ActiveSheet,'r').read();
              readActiveSheet=pandas.read_csv(ActiveSheet); 
              readActiveSheet=pandas.DataFrame(data=readActiveSheets) 
        print("readActiveSheet");
        print(readActiveSheet);
        print("readActiveSheet.columns = ",readActiveSheet.columns);
        print("typeof readActiveSheet.columns = ",type(readActiveSheet.columns));
        lCount=lCount+1;
  return ActiveSheets;