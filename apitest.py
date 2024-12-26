import requests

url = "http://127.0.0.1:5000/status"
response = requests.get(url)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
