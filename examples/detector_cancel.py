import requests

REST = "http://0.0.0.0:8008"

print(f"{'-' * 20} Cancel detector {'-' * 20}")
r = requests.put(f"{REST}/detector/api/1.8.0/command/cancel")
print(r)
