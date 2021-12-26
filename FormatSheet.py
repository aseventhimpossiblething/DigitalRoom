import os

def headers():
  os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  ActiveSheets=os.listdir();
  numOfSheets=len(ActiveSheets);
  if numOfSheets =0:
     return "Enter a single csv or xlsx sheet. - DO NOT ENTER A MULTISHEET WORKBOOK! "
  print("-----------------------------------------------------------")
  print("---calling headers-----")
  print("numOfSheets ",numOfSheets)
  #ActiveSheets=os.listdir();
  lCount=0;
  while lCount < numOfSheets():
        ActiveSheet=ActiveSheets[lCount];
        print("ActiveSheets ",ActiveSheets);
        OpenActiveSheets=open(ActiveSheets,'r');
        print(lCount," done")
        
  print(" entered sequence ")
  print("os listdir[0] ",os.listdir()[0])
  #print("os listdir[1] ",os.listdir()[1])
  #print("os listdir[2] ",os.listdir()[2])
  
  return numOfSheets+os.listdir();
