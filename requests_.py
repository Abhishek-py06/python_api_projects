import requests
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)  # Send GET request
print(response.status_code)   # 200 means success

data = response.json()  # Converts JSON response into Python object (list of dicts)

print(type(data))       # Check type → should be <class 'list'>
for i in data[:5]:
    print(i)
    print(type(i))
for i in data[:10]:
    print(i["title"])
for i in data[:10]:
    if i["userId"] == 5 :
        print(i)
count ={}
for i in data:
    uid = i["userId"]
    if uid in count :
       count[uid] +=1
    else:
        count[uid]= 1
print(count)

import json 
with open("posts.json" , "w") as f:
    json.dump(data,f,indent=2)
print("data saved into posts.json")

import pandas as pd 

df = pd.DataFrame(data)

df.to_csv("posts.csv" , index=False)

print("data saved to csv file ")