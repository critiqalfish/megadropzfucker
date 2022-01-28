import requests

r = requests.get(f"http://api.scraperapi.com?api_key=c665572ee042a836770340e6f54ab055&url=https://pastebin.com/hTyvZjYC").text
print(r)