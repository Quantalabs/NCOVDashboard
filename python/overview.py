import pandas as pd
import requests
import io
import datetime

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
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

with open('../us/overview.html', 'w') as overview:
    overview.write(htmlBase)

with open('../us/overview.html', 'a') as overview:
    df.sort_values(by=['cases'], inplace=True, ascending=False)
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Highest Cases:   '+df['state'].to_list()[0]+' with '+ '{:,.2f}'.format(df['cases'].to_list()[0])+' cases</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Lowest Cases: '+df['state'].to_list()[-1]+' with '+ '{:,.2f}'.format(df['cases'].to_list()[-1])+' cases</h6><br>')
    df.sort_values(by=['deaths'], inplace=True, ascending=False)
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Highest Deaths: '+df['state'].to_list()[0]+' with '+'{:,.2f}'.format(df['deaths'].to_list()[0])+' deaths</h6><br>')
    overview.write('<h6 class=\'text-primary\' align=\'center\'>Lowest Deaths: '+df['state'].to_list()[-1]+' with '+'{:,.2f}'.format(df['deaths'].to_list()[-1])+' deaths</h6><br>')
    
    overview.write('</body></html>')