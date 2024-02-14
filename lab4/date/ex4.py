import datetime
today=datetime.datetime.now()
few_days=int(input())
some_days_ago=today.replace(day=few_days)
arasi=today.day - some_days_ago.day
print(arasi)
print(arasi*24*60*60)