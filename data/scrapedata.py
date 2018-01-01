from itertools import islice
import os

from movieDataScraper.driver import Driver

base = r'./bestpicturesbyyear/'

allyears = [x[2] for x in os.walk('./bestpicturesbyyear')][0]

for yearFile in islice(allyears, 0, 2):
    with open(base + yearFile, 'r') as f:
        for movie in f:
            print(movie)