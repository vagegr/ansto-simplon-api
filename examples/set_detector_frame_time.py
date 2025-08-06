import requests
import argparse

REST = "http://0.0.0.0:8008"
FRM_T = 0.01

parser = argparse.ArgumentParser(description='Set frame time');
parser.add_argument('frm_t', type=float, nargs='?', help='Frame time')

args = parser.parse_args()

if isinstance(args.frm_t, float):
    FRM_T = args.frm_t

print(f"{'-' * 20} Configure frame time {'-' * 20}")
frame_time = {"value": FRM_T}
r = requests.put(f"{REST}/detector/api/1.8.0/config/frame_time", json=frame_time)
print(r.text)