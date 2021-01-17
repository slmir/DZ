import datetime


for i in range(17):
    print("('S-{}'),".format(i))

today = str(datetime.date.today())
newtoday = today[8:10]+'.'+today[5:7]+'.'+today[0:4]
print(newtoday, str(datetime.date.today()))