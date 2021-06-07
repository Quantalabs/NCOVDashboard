import requests
import io
import json
import datetime

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

with open('../India/table.html', 'w') as table:
    table.write(htmlBase)

with open('../India/table.html', 'a') as table:
    table.write('''
    <table align="center" class='table' width='100%'>
        <tr class='text-primary'>
            <th>Last Updated</th>
            <th>State/Territory</th>
            <th>Cases</th>
            <th>Deaths</th>
            <th>Recovered</th>
        </tr>
    ''')
    for x in range(0, len(list(data.keys()))):
        '''
        active = 'N/A'
        recovered = 'N/A'

        if data["Active"][x] == data["Active"][x]:
            active = int(data["Active"][x])
            recovered = int(data["Confirmed"][x]) - active
        '''

        table.write('''
        <tr>
            <th>''' + str(datetime.datetime.today().strftime("%d-%m-%Y")) + ' ' + str(datetime.datetime.now().strftime("%H:%M:%S"))+'''</th>
            <th>''' + str(list(data.keys())[x])+'''</th>
            <th>''' + '{:,}'.format(data[list(data.keys())[x]]['confirmed'])+'''</th>
            <th>''' + '{:,}'.format(data[list(data.keys())[x]]['deaths'])+'''</th>
            <th>''' + '{:,}'.format(data[list(data.keys())[x]]['recovered'])+'''</th>
        <tr>
        ''')

    table.write('''</table><br>
    </body>
</html>''')