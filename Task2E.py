
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.utils import fetch_station_list_levels
#You must pip install tqdm!!!
def run():
    stations = build_station_list()
    topTenStations = fetch_station_list_levels(stations,10,10)
    for station in topTenStations:
        plot_water_levels(station,station.level_history[0],station.level_history[1])
    
if __name__ == "__main__":
    run()
