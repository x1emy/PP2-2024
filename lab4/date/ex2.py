import datetime
yesterday=datetime.datetime.now()-datetime.timedelta(days=1)
print("Yesterday was: ", yesterday.strftime("%Y-%m-%d"))
today=datetime.datetime.now()
print("Today is:",today.strftime("%Y-%m-%d"))
tomorrow=datetime.datetime.now()+datetime.timedelta(days=1)
print("Tomorrow will be: ",tomorrow.strftime("%Y-%m_%d"))
