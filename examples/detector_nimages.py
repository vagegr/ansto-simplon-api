import requests
import argparse

REST = "http://0.0.0.0:8008"
NIMG = 1

parser = argparse.ArgumentParser(description='Set number of images');
parser.add_argument('nimages', type=int, nargs='?', help='Number of images')

args = parser.parse_args()

if isinstance(args.nimages, int):
    NIMG = args.nimages

print(f"{'-' * 20} Configure number of images {'-' * 20}")
nimages = {"value": NIMG}
r = requests.put(f"{REST}/detector/api/1.8.0/config/nimages", json=nimages)
print(r.text)