
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import datetime
from tqdm import tqdm
#You must pip install tqdm!!!

def run():
    stations = build_station_list()
    stations = inconsistent_typical_range_stations(stations,True,True)
    update_water_levels(stations)
    topStations = stations_highest_rel_level(stations,5)
    for item in tqdm(topStations, desc= "Loading plots for Task 2E: "):
        station = item[0]
        dates,levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days = 10))
        station.level_history = (dates,levels)
        poly, d0 = polyfit(station.level_history[0],station.level_history[1],4)
        plot_water_level_with_fit(station,station.level_history[0],station.level_history[1],poly)

"""
def run():
    stations = floodsystem.stationdata.build_station_list()

    topFive = floodsystem.utils.fetch_station_list_levels(stations,2,5)
    for station in topFive:
        poly, d0 = floodsystem.analysis.polyfit(station.level_history[0],station.level_history[1],4)
        floodsystem.plot.plot_water_level_with_fit(station,station.level_history[0],station.level_history[1],poly)
"""
if __name__ == "__main__":
    run()


'''
stations = floodsystem.stationdata.build_station_list()
station = stations[0]
dt = 2
dates, levels = floodsystem.datafetcher.fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
station.latest_level = levels[0]
station.level_history = (dates,levels)
poly, d0 = floodsystem.analysis.polyfit(station.level_history[0],station.level_history[1],4)
print(poly)
floodsystem.plot.plot_water_level_with_fit(station,station.level_history[0],station.level_history[1],poly)'''