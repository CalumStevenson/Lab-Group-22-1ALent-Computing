"""Unit test for the geo module"""

from numpy import sort
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from haversine import haversine

def test_rivers_by_distance():
    stations = build_station_list()
    tuples = []
    p = 52.2053, 0.1218
    for station in stations:
        coords = station.coord
        distance = haversine(p, station.coord)
        tuples.append((station.name, distance))
    tuples = sort(tuples, 1)
    close = tuples[:10]
    far = tuples[-10:]
    closest = close[0]
    farthest = far[9]
    assert closest[1] == 0.840237595667494
    assert farthest[1] == 440.00325604140033

#def test_rivers_within_radius():
    #stations = build_station_list()
    #rivers = rivers_with_station(stations)
    #Cam = None
    #for river in rivers:
     #   if river == "River Cam":
      #      Cam = river
       #     break
    #assert Cam
    #assert len(rivers) <= len(stations)

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
