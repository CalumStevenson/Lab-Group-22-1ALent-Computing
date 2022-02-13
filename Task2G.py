from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.utils import assess_flood_risk
def run():
    stations = build_station_list()
    stations = inconsistent_typical_range_stations(stations,True,True)
    Towns = assess_flood_risk(stations)
    print(Towns)


if __name__ == "__main__":
    run()