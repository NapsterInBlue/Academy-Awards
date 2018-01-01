from bompage import BOMPage
import matplotlib.pylab as plt


movies = {'beauty': 'http://www.boxofficemojo.com/movies/?page=weekly&id=americanbeauty.htm'
         ,'cider': 'http://www.boxofficemojo.com/movies/?page=weekly&id=ciderhouserules.htm'
         ,'greenmile': 'http://www.boxofficemojo.com/movies/?page=weekly&id=greenmile.htm'
         ,'insider': 'http://www.boxofficemojo.com/movies/?page=weekly&id=insider.htm'
         ,'sixth': 'http://www.boxofficemojo.com/movies/?page=weekly&id=sixthsense.htm'
         }

def plotit(table, label):
    plt.plot(table.Thursday, table.Theaters, label=label, alpha=.5)

for movie in movies:
    try:
        plotit(BOMPage(movies[movie]).weeklyTable, movie)
    except:
        print(movie)

plt.legend()
plt.axvline('2000-02-15', c='k')
plt.axvline('2000-03-26', c='k')

plt.show()