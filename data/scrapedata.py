import os
import sys
import pickle
from itertools import islice

from movieDataScraper.driver import Driver

# otherwise pickle throws a fit trying to pack classes
sys.setrecursionlimit(9999)

base = r'./bestpicturesbyyear/'
allyears = [x[2] for x in os.walk(base)][0]

for yearFile in allyears:
    alldata = []
    print('\n'*2, yearFile, '\n'*2)
    with open(base + yearFile, 'r') as f:
        for movie in f:
            print(movie)
            driver = Driver(movie)
            alldata.append((yearFile, movie.strip(), driver.bom))

        pickle.dump(alldata, open('./pickleddata/'+yearFile+'.pkl', 'wb'))
