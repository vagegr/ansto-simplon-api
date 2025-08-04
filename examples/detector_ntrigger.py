import requests
import argparse

REST = "http://0.0.0.0:8008"
NTRG = 1

parser = argparse.ArgumentParser(description='Set number of triggers');
parser.add_argument('ntrigger', type=int, nargs='?', help='Number of triggers')

args = parser.parse_args()

if isinstance(args.ntrigger, int):
    NTRG = args.ntrigger

print(f"{'-' * 20} Configure number of triggers {'-' * 20}")
ntrigger = {"value": NTRG}
r = requests.put(f"{REST}/detector/api/1.8.0/config/ntrigger", json=ntrigger)
print(r.text)