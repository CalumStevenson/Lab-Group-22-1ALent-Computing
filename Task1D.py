from floodsystem import geo
from floodsystem import stationdata
stations = stationdata.build_station_list()
print(len(geo.rivers_with_station(stations)))
print(geo.rivers_with_station(stations))
stations_by_river = geo.stations_by_river(stations)
print('\n\n')
print('River Aire:',stations_by_river['River Aire'],'\n')
print('River Cam:',stations_by_river['River Cam'],'\n')
print('River Thames: ',stations_by_river['River Thames'],'\n')