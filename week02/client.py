import requests

url = 'http://127.0.0.1:8000/items/6612345678?q=Winai'
conn = requests.get(url)

print(conn.status_code)
