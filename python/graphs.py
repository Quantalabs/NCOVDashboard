import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
from datetime import date, timedelta

dates = date.today() - timedelta(days=1)
url = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"
    + dates.strftime("%m-%d-%Y")
    + ".csv"
)
print(url)
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode("utf-8")))

df.sort_values(by=["Confirmed"], inplace=True, ascending=False)

data = [
    df["Confirmed"].to_list()[0],
    df["Confirmed"].to_list()[1],
    df["Confirmed"].to_list()[2],
    df["Confirmed"].to_list()[3],
    df["Confirmed"].to_list()[4],
]
states = [
    df["Province_State"].to_list()[0],
    df["Province_State"].to_list()[1],
    df["Province_State"].to_list()[2],
    df["Province_State"].to_list()[3],
    df["Province_State"].to_list()[4],
]

plt.pie(data, labels=states)
plt.savefig("../us/graph.png")
