import pandas as pd
import requests
import io
import numpy as np
from datetime import date, timedelta

dates = date.today()-timedelta(days=1)
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"+dates.strftime('%m-%d-%Y')+".csv"
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
    deaths = '{:,}'.format(np.sum(np.array(df['Deaths'].to_list())))
    cases = '{:,}'.format(np.sum(np.array(df['Confirmed'].to_list())))
    try:
        recovered = '{:,}'.format(np.sum(np.array(df['Confirmed'].to_list()))-np.sum(np.array(list(map(int, df['Active'].to_list())))))
    except:
        recovered = 'No current data'
    try:
        active = '{:,}'.format(np.sum(np.array(list(map(int, df['Active'].to_list())))))
    except:
        active = 'No current data'

    overview.write('<h6 class=\'text-primary\' align=\'center\'>Total Cases:   '+str(cases)+'</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Total Deaths: '+str(deaths)+'</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Total Recovered: '+str(recovered)+'</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Total Active: '+str(active)+'</h6><br>')
    overview.write('</body></html>')
