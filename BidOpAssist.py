import os
import numpy
import scipy
import pandas

def BidOpAssist(x,y,z):
    print("***BidOpAssist Running********")
    print(x,y,z)    
BidOpAssist("BidOpAssist is Running as expected","Second Slot","Third Slot")
os.chdir('Sheets')
print(os.getcwd())


Sata=open('sample.txt').read()
#print(Sata)
Sata=numpy.array(Sata)
print(Sata)
print(Sata.shape)
numpy.reshape(Sata)
#pandas.DataFrame(Sata)
#print(data)
#except 
#readSample=open('sample.txt').read()
#print(readSample)
#incomingSheet=open('Bid_OpExperiment.xlsx')
#pandas.read_csv('Bid_OpExperiment.csv')

#incomingSheet=open('Bid_OpExperiment.xlsx')
#SHeetRead=incomingSheet.read()
#print(incomingSheet)



   
