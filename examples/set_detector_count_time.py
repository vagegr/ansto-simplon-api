import requests
import argparse

REST = "http://0.0.0.0:8008"
CNT_T = 0.01

parser = argparse.ArgumentParser(description='Set count time');
parser.add_argument('cnt_t', type=float, nargs='?', help='Count time')

args = parser.parse_args()

if isinstance(args.cnt_t, float):
    CNT_T = args.cnt_t

print(f"{'-' * 20} Configure count time {'-' * 20}")
count_time = {"value": CNT_T}
r = requests.put(f"{REST}/detector/api/1.8.0/config/count_time", json=count_time)
print(r.text)