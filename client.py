import requests
import sys

SERVER_IP = sys.argv[1] 
url = f"http://{SERVER_IP}:5013/api/american"
headers = { "Content-Type" : "application/json" }

r = requests.post(url, headers=headers, json={ "text": sys.argv[2]} )
print(r.json())
