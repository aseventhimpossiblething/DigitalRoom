import os

def headers():
  print("-----------------------------------------------------------")
  print("---calling headers-----")
  print("os getcwd ",os.getcwd())
  print("os chdir ",os.chdir('/GMDelight/DigitalRoom/Sheets/CTRData'))
  print(" entered sequence ")
  print("os listdir ",os.listdir())
  return os.listdir();
