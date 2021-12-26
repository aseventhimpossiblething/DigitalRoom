import os

def headers():
  os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData');
  numOfSheets=len(os.listdir());
  print("-----------------------------------------------------------")
  print("---calling headers-----")
  print("numOfSheets ",numOfSheets)
  #print("os chdir ",os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData'))
  print(" entered sequence ")
  #print("os listdir[0] ",os.listdir()[0])
  #print("os listdir[1] ",os.listdir()[1])
  #print("os listdir[2] ",os.listdir()[2])
  
  return numOfSheets+os.listdir();
