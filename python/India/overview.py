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

htmlBase = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
<!--     Fonts and icons     -->
<link href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200" rel="stylesheet" />
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
<!-- CSS Files -->
<link href="../assets/css/bootstrap.min.css" rel="stylesheet" />
<link href="../assets/css/paper-dashboard.css?v=2.0.1" rel="stylesheet" />
<!-- CSS Just for demo purpose, don't include it in your project -->
<link href="../assets/demo/demo.css" rel="stylesheet" />
<style>
</style>
</head>
<body>
'''

with open('../India/overview.html', 'w') as overview:
    overview.write(htmlBase)

with open('../India/overview.html', 'a') as overview:
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Highest Cases:   ' + list(data.keys())[0] + ' with ' + '{:,}'.format(data[list(data.keys())[0]]['confirmed']) + ' cases</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Lowest Cases: ' + list(data.keys())[-1]+' with ' +  '{:,}'.format(data[list(data.keys())[-1]]['confirmed'])+' cases</h6><br>')
    data = dict(sorted(data.items(), key=lambda x:x[1]['deaths']))
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Highest deaths: ' + list(data.keys())[-1]+' with ' + '{:,}'.format(data[list(data.keys())[-1]]['deaths'])+' deaths</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Lowest deaths: ' + list(data.keys())[0]+' with ' + '{:,}'.format(data[list(data.keys())[0]]['deaths'])+' deaths</h6><br>')
    data = dict(sorted(data.items(), key=lambda x:x[1]['recovered']))
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Most recovered: ' + list(data.keys())[-1]+' with ' + '{:,}'.format(data[list(data.keys())[-1]]['recovered'])+' recovered</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Lowest recovered: ' + list(data.keys())[0]+' with ' + '{:,}'.format(data[list(data.keys())[0]]['recovered'])+' recovered</h6><br>')
    
    overview.write('</body></html>')
