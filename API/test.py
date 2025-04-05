import requests

url = "http://localhost:8000/poem/invoke"
data = {"input": {"input": "moonlight"}}  # Ensure correct format

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Raw Response:", response.text)  # See full response
