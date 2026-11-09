import requests

response = requests.get("http://127.0.0.1:8000/config")
print("Config:", response.json())

payload = {"record_id": "REC-9921", "anonymized": True}
res = requests.post("http://127.0.0.1:8000/audit/record", json=payload)
print("Audit Result:", res.json())
