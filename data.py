import pandas as pd
import random

colors=["#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff", "#f7bb5f"]

def get_population_data():
    url = 'https://gist.githubusercontent.com/johnburnmurdoch/4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/city_populations'
    df = pd.read_csv(url, usecols=['name', 'year', 'value'])
    df['color']=[colors[random.randint(0,5)] for i in range(df.shape[0])]
    return df

def get_gdp_data():
    pass
