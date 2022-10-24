import json
from collections import Counter

f=open("result.json", "r", encoding="utf-8")


messages=json.loads(f.read())


dates=[]
days=[]

for m in messages:
    #print(m["text"])
    if type(m["text"])== str:
        #print("not getting")
        if m["text"].find("ядерн")!=-1:
            print(m["date"])
            days.append(str(m["date"][0:10]))
            dates.append(m["date"][0:7])
    else:
       # print(type(m["text"]))
        if type(m["text"])==list:
            #print(m["text"])
            for y in m["text"]:
                if type(y)==str:
                    if y.find("ядерн")!=-1:
                        print(m["date"])
                        days.append(str(m["date"][0:10]))
                        dates.append(m["date"][0:7])
                else:
                    if type(y)==dict:
                        if "text" in y.keys():
                            if y["text"].find("ядерн")!=-1:
                                print(m["date"])
                                break
                                days.append(str(m["date"][0:10]))
                                dates.append(m["date"][0:7])
                            
                        

count_date=Counter(dates)
count_day=Counter(days)

print(count_date)

print(count_day)


    
