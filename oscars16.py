from bompage import BOMPage
import matplotlib.pylab as plt


movies = {'moonlight': 'http://www.boxofficemojo.com/movies/?page=weekly&id=moonlight2016.htm'
         ,'arrival': 'http://www.boxofficemojo.com/movies/?page=weekly&id=arrival2016.htm'
         ,'fences': 'http://www.boxofficemojo.com/movies/?page=weekly&id=fences.htm'
         ,'hacksaw': 'http://www.boxofficemojo.com/movies/?page=weekly&id=hacksawridge.htm'
         ,'hell': 'http://www.boxofficemojo.com/movies/?page=weekly&id=hellorhighwater.htm'
         ,'hidden': 'http://www.boxofficemojo.com/movies/?page=weekly&id=hiddenfigures.htm'
         ,'lala': 'http://www.boxofficemojo.com/movies/?page=weekly&id=lalaland.htm'
         ,'lion': 'http://www.boxofficemojo.com/movies/?page=weekly&id=lion.htm'
         ,'manchester': 'http://www.boxofficemojo.com/movies/?page=weekly&id=manchesterbythesea.htm'
         }

def plotit(table, label):
    plt.plot(table.Thursday, table.Theaters, label=label, alpha=.5)

for movie in movies:
    try:
        plotit(BOMPage(movies[movie]).weeklyTable, movie)
    except:
        print(movie)
    plt.legend()
    plt.axvline('2017-01-24')
    plt.axvline('2017-03-04')

    plt.show()