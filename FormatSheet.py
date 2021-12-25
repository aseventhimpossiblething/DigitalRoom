import os

def headers():
  print("---calling headers-----")
  print("os getcwd ",os.getcwd())
  print(" entered sequence ")
  print("os listdir ",os.listdir())
  return os.listdir();
