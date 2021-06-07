import requests
import matplotlib.pyplot as plt
import io
import json

url = "https://covid-19.mathdro.id/api/countries/india/confirmed"
download = requests.get(url).text

listdata = json.loads(download)
data = {}

for state in listdata:
    data[state["provinceState"]] = {}
    for key in state:
        if not key.startswith('provinceState'):
            data[state["provinceState"]][key] = state[key]

cases = [int(list(data.values())[0]['confirmed']), int(list(data.values())[1]['confirmed']), int(list(data.values())[2]['confirmed']), int(list(data.values())[3]['confirmed']), int(list(data.values())[4]['confirmed'])]
lables = [list(data.keys())[0], list(data.keys())[1], list(data.keys())[2], list(data.keys())[3], list(data.keys())[4]]

print(cases)
print(lables)

plt.pie(cases, labels=lables)
plt.savefig('../India/graph.png')
