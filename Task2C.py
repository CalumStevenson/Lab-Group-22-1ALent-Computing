from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import update_water_levels
def run():
    stations = build_station_list()
    stations = inconsistent_typical_range_stations(stations,True)
    update_water_levels(stations)
    List = stations_highest_rel_level(stations,10)
    for item in List:
        print(item[0].name,item[1])
if __name__ == "__main__":
    run()