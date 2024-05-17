import requests

age=20
sex='F'

response=requests.get(f"http://localhost:8000/predict?age={age}&sex={sex}")

output = response.json()

print(output)

