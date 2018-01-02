import pickle
import os

import pandas as pd

d = {}
df = pd.DataFrame()
base = './pickleddata/'
pickles = [x[2] for x in os.walk(base)][0]

for pick in pickles:
    p = open(base+pick, 'rb')
    alldata = pickle.load(p)
    p.close()

    for movie in alldata:
        d[movie[1].strip()] = movie[2].metadata
        tempDf = pd.DataFrame(movie[2].weeklyTable)
        tempDf['name'] = movie[1].strip()
        tempDf['year'] = movie[0]
        df = df.append(tempDf, ignore_index=True)

winners = df.groupby('year').first().name.values
df['Winner'] = df['name'].isin(winners)

df.to_csv('movieData.csv', index=False)