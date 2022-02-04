"""Unit test for the geo module"""

from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    Cam = None
    for river in rivers:
        if river == "River Cam":
            Cam = river
            break
    assert Cam
    assert len(rivers) <= len(stations)

def test_stations_by_river():
    stations = build_station_list()
    RiverDictionary = stations_by_river(stations)
    rivers = rivers_with_station(stations)
    assert len(rivers) == len(RiverDictionary)
    assert type(RiverDictionary) == dict
    for river in RiverDictionary:
        assert type(river) == str
        assert type(RiverDictionary[river]) == list
        for i in RiverDictionary[river]:
            assert type(i) == MonitoringStation

def test_rivers_by_station_number():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    for i in range(len(stations)):
        riverList = rivers_by_station_number(stations,i)
        if i == 0: 
            assert len(riverList) == len(rivers)
        else:
            if len(riverList)!= i:
                for j in range(1,len(riverList)-i):
                    assert riverList[len(riverList)-j] == riverList[len(riverList)-j-1]
            else:
                assert len(riverList) == i

