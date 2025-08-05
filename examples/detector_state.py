import requests

REST = "http://0.0.0.0:8008"

print(f"{'-' * 20} Detector state {'-' * 20}")
r = requests.get(f"{REST}/detector/api/1.8.0/status/state")
print(r.text)