import pandas as pd
import requests
import io
from datetime import date, timedelta

dates = date.today() - timedelta(days=1)
url = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"
    + dates.strftime("%m-%d-%Y")
    + ".csv"
)
download = requests.get(url).content
url2 = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv"
download2 = requests.get(url2).content

df = pd.read_csv(io.StringIO(download.decode("utf-8")))
df2 = pd.read_csv(io.StringIO(download2.decode("utf-8")))

vaccinations = []

for x in range(0, len(df2["date"])):
    if df2["date"][x] == dates.strftime("%Y-%m-%d"):
        vaccinations.append([df2["location"][x], df2["total_vaccinations"][x]])

htmlBase = """
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
"""

with open("../us/table.html", "w") as table:
    table.write(htmlBase)

with open("../us/table.html", "a") as table:
    table.write(
        """
    <table align="center" class='table' width='100%'>
        <tr class='text-primary'>
            <th>Last Updated</th>
            <th>State/Territory</th>
            <th>Cases</th>
            <th>Deaths</th>
            <th>Vaccinations</th>
        </tr>
    """
    )
    for x in range(0, 58):
        """
        active = 'N/A'
        recovered = 'N/A'

        if df["Active"][x] == df["Active"][x]:
            active = int(df["Active"][x])
            recovered = int(df["Confirmed"][x]) - active
        """
        for z in vaccinations:
            if z[0] == df["Province_State"][x]:
                vax_data = z[1]

        table.write(
            """
        <tr>
            <th>"""
            + str(df["Last_Update"][x])
            + """</th> 
            <th>"""
            + str(df["Province_State"][x])
            + """</th> 
            <th>"""
            + "{:,}".format(df["Confirmed"][x])
            + """</th> 
            <th>"""
            + "{:,}".format(df["Deaths"][x])
            + """</th> 
            <th>"""
            + "{:,}".format(int(vax_data))
            + """</th>
        <tr>
        """
        )

    table.write(
        """</table>
    </body>
</html>"""
    )
