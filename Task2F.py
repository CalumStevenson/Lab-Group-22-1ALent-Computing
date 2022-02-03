import floodsystem.stationdata
import floodsystem.datafetcher
import floodsystem.analysis
import floodsystem.plot
import datetime



stations = floodsystem.stationdata.build_station_list()
'''
topFive = fetch_station_list_levels(stations,2,5)
for station in topFive:
    poly, d0 = floodsystem.analysis.polyfit(station.level_history[0],station.level_history[1],4)
    floodsystem.plot.plot_water_levels(station,station.level_history[0],station.level_history[1],poly)
'''
station = stations[0]
dt = 2
dates, levels = floodsystem.datafetcher.fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
station.latest_level = levels[0]
station.level_history = (dates,levels)
poly, d0 = floodsystem.analysis.polyfit(station.level_history[0],station.level_history[1],4)
print(poly)
#floodsystem.plot.plot_water_levels(station,station.level_history[0],station.level_history[1],poly)