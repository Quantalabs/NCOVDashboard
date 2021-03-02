from numpy.core.fromnumeric import size
import pandas as pd
import requests
import io
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

cases = df['cases'].to_list()
dates = df['date'].to_list()

from matplotlib.ticker import MaxNLocator


fig, ax = plt.subplots()
labels = df['date'].to_list()

plt.xlabel('Date')
plt.ylabel('Cases')
ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))
ax.plot(dates, cases)
plt.savefig('../us/pcd.png')