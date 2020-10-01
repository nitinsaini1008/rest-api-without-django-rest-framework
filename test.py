import requests
import json
url='http://127.0.0.1:8000/api/'
# data={"sub": "changed something@62", "num": 100,}
# ans=requests.get(url+str(1))
# ans=requests.put(url+str(100),data=json.dumps(data))
# print(ans.json())
# print(ans.status_code)
ans=requests.delete(url+str(2))
print(ans.json())
print(ans.status_code)