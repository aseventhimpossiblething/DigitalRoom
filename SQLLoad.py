print("pre import sql")
import sqlite3
import pandas

def MakeDailyTable(x):
    #print(x)
    x=x.drop(columns=['index'])
    #print(x)
    novelXstr="";
    y=x.columns;
    print("Make Data Input")
    for elem in y:
        elem=elem+" REAL, ";
        novelXstr=novelXstr+elem;
        #novelXarr.append(elem)
    novelXstr=novelXstr[:len(novelXstr)-1]     
    novelXstr2="create table DailyTable("+novelXstr[:len(novelXstr)-1]+");" 
    novelXstr3=novelXstr.replace(" REAL","");
    #novelXstr=novelXstr#.replace("index REAL,","")
    #print("length of x");
    #print(len(x));
    #print("length of new arr");
    #print(len(novelXarr))
    #print(novelXstr2)
    
    """
    rowcount=0;
    while rowcount<len(x):
          print("start cycle-------------");
          littleArray=[];       
          littlecount=0;
          while littlecount<len(x.iloc[rowcount]):
                littleArray.append(x.iloc[rowcount][littlecount]) 
                littlecount=littlecount+1;
                print(littlecount,"-littleArray ",littleArray)
             
          print(type(x.iloc[rowcount]),"-",x.iloc[rowcount]);
          
          print("end cycle-------------");  
          #print(z.iloc([1])); 
          #print(x[rowcount]);
          rowcount=rowcount+1;
    
    """
    
    insertionCols=novelXstr
    
    
    insert="insert into DailyTable() Values()"
    query="select*from DailyTable"
    SQLite3conn=sqlite3.connect("DailyDB")
    cursor=SQLite3conn.cursor();
    cursor.execute(novelXstr2);
    #cursor.executemany();
    cursor.execute(query);
    
    results=cursor.fetchall();
    print("results",results)
    print(x)
    print("novelXstr",novelXstr)
    print("novelXstr2",novelXstr2)
    print("novelXstr3",novelXstr3)
   
    
    print("end Make Daily")
    
    

    
    
"""
SQLite3conn=sqlite3.connect("DailyBD")
cursor=SQLite3conn.cursor();
cursor.execute("create table DailyTable")

b=cursor.execute("select*from DailyTable limit 1;")
c=ColNames=pandas.DataFrame(cursor.description)
c=c[[0]];

a=cursor.fetchall();

#print(cursor)
#print(cursor.description)
#print(SQLcolsnames)
print(a)
#print(b)
print(c)
print("post connect")
"""
