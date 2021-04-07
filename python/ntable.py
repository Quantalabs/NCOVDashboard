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

with open('../us/ntable.html', 'w') as table:
    table.write(htmlBase)

with open('../us/ntable.html', 'a') as table:
    table.write('''
    <table align="center" class='table' width='100%'>
        <tr class='text-primary'>
            <th>Date</th>
            <th>Cases</th>
            <th>Deaths</th>
            <th>New Cases</th>
        </tr>
    ''')
    for x in range(len(df["date"].to_list())):
        if x == 0:
            table.write('''
            <tr>
                <th>'''+str(df["date"][x])+'''</th>
                <th>'''+'{:,}'.format(df["cases"][x])+'''</th> 
                <th>'''+'{:,}'.format(df["deaths"][x])+'''</th>
                <th>'''+'{:,}'.format(df["cases"][x])+'''</th> 
            <tr>
            ''')
        else:
            #print('Cases x '+str(df["cases"][x]))
            #print('Cases x-1 '+str(df["cases"][x-1]))
            #print('Deaths '+str(df["deaths"][x]))
            #print('Date '+str(df["date"][x]))
            amb = None
            try: 
                amb = '''<th>'''+'{:,}'.format(df["cases"][x]-df["cases"][x-1])+'''</th>'''
            except:
                '''<th> No current data </th>'''
                amb = '''No Case Data!'''
            #print(amb)
            table.write('''
            <tr>
            <th>'''+str(df["date"][x])+'''</th>
            <th>'''+'{:,}'.format(df["cases"][x])+'''</th> 
            <th>'''+'{:,}'.format(df["deaths"][x])+'''</th>'''+
            amb+ '''<tr>
            ''')

    table.write('''</table>
    </body>
</html>''')
