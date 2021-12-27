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
        isxlsx=lower( ActiveSheet).find(".xlsx");
        iscsv=lower( ActiveSheet).find(".csv");
        print("ActiveSheet ",ActiveSheet);
        print("isxlsx ",isxlsx); 
        print("iscsv ",iscsv);
        print(" opened ",ActiveSheet);
        try:
           isxlsx=lower( ActiveSheet).find(".xlsx");
           iscsv=lower( ActiveSheet).find(".csv"); 
           OpenActiveSheets=open(ActiveSheet,'r');
           print("isxlsx ",isxlsx); 
           print("iscsv ",iscsv);
           print(" opened ",ActiveSheet);
           readActiveSheets=pandas.read_excel(ActiveSheet);
           print(" readActiveSheets ",readActiveSheets);
        except:
           print(" failed to open ",ActiveSheet)
       
        lCount=lCount+1;
          
  return ActiveSheets;
