from floodsystem import geo
from floodsystem import stationdata
from floodsystem import station
def run():
    stations = stationdata.build_station_list()
    List = station.inconsistent_typical_range_stations(stations)
    print(List)
    ListOfNames = []
    for Station in List:
        ListOfNames.append(Station.name)
    print(ListOfNames)

if __name__ == '__main__':
    run()