import pandas as pd
import requests
import io
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv"
download = requests.get(url).content

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

df.sort_values(by=['cases'], inplace=True, ascending=False)

data = [df['cases'].to_list()[0],df['cases'].to_list()[1],df['cases'].to_list()[2],df['cases'].to_list()[3],df['cases'].to_list()[4]]
states = [df['state'].to_list()[0],df['state'].to_list()[1],df['state'].to_list()[2],df['state'].to_list()[3],df['state'].to_list()[4]]

plt.pie(data, labels=states)
plt.savefig('../us/graph.png')