from floodsystem import geo
from floodsystem import stationdata
def run():
    stations = stationdata.build_station_list()
    p = 52.2053, 0.1218
    stations_by_distance = geo.stations_by_distance(stations,p)

    print("10 closest are: ", stations_by_distance[:10])
    print("10 farthest are: ", stations_by_distance[-10:])
if __name__ == "__main__":
    run()