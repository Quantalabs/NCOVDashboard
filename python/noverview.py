import pandas as pd
import requests
import io

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

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

with open('../us/noverview.html', 'w') as overview:
    overview.write(htmlBase)

with open('../us/noverview.html', 'a') as overview:
    deaths = ('{:,}'.format(df['deaths'].to_list()[-1]))
    cases = ('{:,}'.format(df['cases'].to_list()[-1]))

    overview.write('<h6 class=\'text-primary\' align=\'center\'>Total Cases:   '+str(cases)+'</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Total Deaths: '+str(deaths)+'</h6><br>')
    overview.write('</body></html>')