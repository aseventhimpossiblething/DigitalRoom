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
        OpenActiveSheets=open(ActiveSheet,'r');
        if isxlsx > 1:
              readActiveSheets=pandas.read_excel(ActiveSheet); 
        if iscsv > 1:
              readActiveSheets=open(ActiveSheet,'r').read();  
              readActiveSheets=pandas.DataFrame(readActiveSheets) 
        print(" readActiveSheets ",readActiveSheets);
        lCount=lCount+1;
  return ActiveSheets;
