import matplotlib.pyplot as plt
import matplotlib

def plot_water_levels(station,dates,levels,poly = None):
    """This procedure plots water level against time for a certain station"""
    plt.plot(dates,levels)
    plt.axhline(station.typical_range[0],color = 'g',label = 'Low typical range boundary')
    plt.axhline(station.typical_range[1],color = 'r',label = 'High typical range boundary')
    plt.axhline(station.average_value,color = 'y', label = 'Average typical water level')
    average = 0
    for i in levels:
        average+= i
    average = average/len(levels)
    #plt.axhline(average,color = 'b', label = 'Mean recent water level')
    if poly != None:
        polyVal = []
        for date in dates:
            polyVal.append(poly(matplotlib.dates.date2num(date)))
        plt.plot(dates,polyVal,label = "Best Fit Polynomial")
    plt.plot(dates,levels, label = 'Water Level Against Time')
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=11)
    plt.title(station.name)
    plt.legend()
    plt.show()
