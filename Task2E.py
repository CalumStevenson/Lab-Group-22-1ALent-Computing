
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import fetch_station_list_levels
import datetime
from tqdm import tqdm
#You must pip install tqdm!!!

def run():
    stations = build_station_list()
    stations = inconsistent_typical_range_stations(stations,True,True)
    update_water_levels(stations)
    topStations = stations_highest_rel_level(stations,5)
    print(topStations)
    for item in tqdm(topStations, desc= "Loading plots for Task 2E: "):
        station = item[0]
        dates,levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days = 10))
        station.level_history = (dates,levels)
        plot_water_levels(station,station.level_history[0],station.level_history[1])
"""
def run():
    stations = build_station_list()
    topFive = fetch_station_list_levels(stations,2,5)
    for station in topFive:
        plot_water_levels(station,station.level_history[0],station.level_history[1])
"""
if __name__ == "__main__":
    run()
