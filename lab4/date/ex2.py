import datetime
print("Yesterday was: ", datetime.datetime.now()-datetime.timedelta(days=1))
print("Today is:", datetime.datetime.now())
print("Tomorrow will be: ", datetime.datetime.now()+datetime.timedelta(days=1))
