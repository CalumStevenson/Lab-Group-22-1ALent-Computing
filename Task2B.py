from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import update_water_levels
def run():
    stations = build_station_list()
    stations = inconsistent_typical_range_stations(stations,True)
    update_water_levels(stations)
    List = stations_level_over_threshold(stations,0.8)
    for item in List:
        print(item[0].name,item[1])

if __name__ == "__main__":
    run()