import requests

REST = "http://0.0.0.0:8008"

print(f"{'-' * 20} Get count time {'-' * 20}")
r = requests.get(f"{REST}/detector/api/1.8.0/config/count_time")
print(r.text)