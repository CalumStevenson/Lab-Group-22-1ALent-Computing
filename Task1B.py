from floodsystem import geo
from floodsystem import stationdata
stations = stationdata.build_station_list()
stations_by_distance = geo.stations_by_distance(stations)
p = 52.2053, 0.1218
print("10 closest are: ", stations_by_distance[:10])
print("10 farthest are: ", stations_by_distance[-10:])