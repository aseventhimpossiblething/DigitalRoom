import os

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
        print("ActiveSheet ",ActiveSheet);
        try:
         OpenActiveSheets=open(ActiveSheet,'r');
         readActiveSheets=read(ActiveSheets);
         print(" opened ",ActiveSheet)
        except:
          print(" failed to open ",ActiveSheet)
        #print(lCount," done")
        lCount=lCount+1;
          
  return ActiveSheets;
