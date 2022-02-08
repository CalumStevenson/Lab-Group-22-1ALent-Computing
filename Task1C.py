from floodsystem import geo
from floodsystem import stationdata
def run():
    stations = stationdata.build_station_list()
    centre = 52.2053, 0.1218
    r = 10
    closest_stations = geo.stations_within_radius(stations, centre, r)

    closest_stations.sort()
    print(closest_stations)

if __name__ == "__main__":
    run()