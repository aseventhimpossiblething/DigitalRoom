"""
Need to determine state/status
Need to limit redis/celery connections
reliable redis/celery cmds
voir les log persistant
Separer les contenue static es dynamique
"""
print("this is the master branch tasque..............................................................")


import CommunityUpdatesProcess
import glob
import numpy
import scipy
import pandas
import BidOpAssist
import fileHandler
import redis
import os
from redis import Redis
from celery import Celery
from flask import Flask
from celery.result import AsyncResult
from celery.result import ResultBase

#print("++++++++++++++++++++++++++++++++++++",app.name())
#print("++++++++++++++++++++++++++++++++++++",app.name)
print("____________________________+++++++++++++++++(1)++++++++++++++_________________________________")


#print(Redis)    
#the_redis='redis://localhost:6379/0'
the_redis=os.environ.get("REDIS_URL")
print('REDIS_URL.....................',the_redis)


print("____________________________+++++++++++++++++(2)++++++++++++++_________________________________")





cel=Celery("Taskque", broker=the_redis)

@cel.task()
def zfunc():
    print("--------------PRINTED FROM IN ZFUNC")
    return 42
zfunc.apply_async()

#zfunc.apply_async(countdown=100)


print("____________________________+++++++++++++++++(3)++++++++++++++_________________________________")



#zfunc()
#print("zfunc.delay()------",zfunc.delay())
#Zfunc.delay()
#Zfunc.apply_async()
@cel.task()
def initiLjoV():
  print("tasque File Running initiJoV")
  Rval="return value"
  return Rval
#initiLjoV.delay()
#initiLjoV.apply_async()
#run_initiLjoV=initiLjoV.delay()
run_initiLjoV=initiLjoV.apply_async()
taskId=run_initiLjoV.task_id
print("taskId.....This is the task ID............",taskId)
#run_initiLjoV=initiLjoV.apply_async()
#result=run_initiLjoV.result
#run_initiLjoV=initiLjoV.apply_async()
#print('printed result____________',result)
print(AsyncResult(taskId))





print("____________________________+++++++++++++++++(4)++++++++++++++_________________________________")











#run_initiLjoV.result.state()
#print('run_initiLjoV.result...',run_initiLjoV.result)

#print("AsyncResult(taskId).ready()...",AsyncResult(taskId).ready())
#print('run_initiLjoV.ready()...This seems to work? ...',run_initiLjoV.ready())

#AsyncResult(taskId).status()
#result.state
#result.state()
#result.status
#result.status()


#print("run_initiLjoV.state.........",run_initiLjoV.state)
#run_initiLjoV.status()
#print("run_initiLjoV.status........",run_initiLjoV.status)
#run_initiLjoV.result()
#run_initiLjoV.result

#AsyncResult(taskId).status()



"""
initiLjoV.delay().state
initiLjoV.delay().status
initiLjoV.delay().result
"""


#redis.Redis().client_getname()
#run_initiLjoV=initiLjoV.delay()


"""
print('redis.Redis()',redis.Redis())
print('redis.Redis',redis.Redis)
print('redis',redis)
"""

#print('This is the client id',redis.Redis().client_id)




#print("initiLjoV State 1",run_initiLjoV.state)
#redis.Redis().flushdb()
#print("ended redis")
#print(redis.scan())

#print("initiLjoV State 2",run_initiLjoV.state)
"""
print("initiLjoV State 3",run_initiLjoV.state)
print("initiLjoV State 4",run_initiLjoV.state)
print("initiLjoV State 5",run_initiLjoV.state)
print("initiLjoV State 6",run_initiLjoV.state)
print("initiLjoV State 7",run_initiLjoV.state)
print("initiLjoV State 8",run_initiLjoV.state)
"""
#print("result",run_initiLjoV.result)






