
import json
import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)
people = result["people"]
for p in people:
    print(p['name'] + " - on board")