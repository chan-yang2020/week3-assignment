import urllib.request as  request
import json
scr="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(scr) as response:
    data=json.load(response)
spot_list=data["result"]["results"]
with open("data.txt","w", encoding="utf-8") as file :
    for i in spot_list:
        pic=i["file"].split("http://")
        file.write(i["stitle"]+","+i["longitude"]+","+i["latitude"]+","+"http://"+pic[1]+"\n")
   