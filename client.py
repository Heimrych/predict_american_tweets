import requests
import sys

url = 'http://localhost:5013/api/american'
headers = { "Content-Type" : "application/json" }

r = requests.post(url, headers=headers, json={ "text": sys.argv[1]} )
print(r.json())