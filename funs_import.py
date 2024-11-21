import requests

url = "https://raw.githubusercontent.com/wugimy/public/refs/heads/master/funs.py"
res = requests.get(url).text
path = "funs.py"
with open(path,'w') as f:
    f.write(res)
res
