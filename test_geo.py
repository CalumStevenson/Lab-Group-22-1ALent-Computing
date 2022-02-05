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
    assert close == [('Cambridge Jesus Lock', 0.840237595667494), ('Bin Brook', 2.502277543239629), ("Cambridge Byron's Pool", 4.07204948005424), ('Cambridge Baits Bite', 5.115596582531859), ('Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 7.0443978959918025), ('Oakington', 7.12825901765745), ('Stapleford', 7.265704342799649), ('Comberton', 7.735085060177142), ('Dernford', 7.993872393303291)]
    assert far == [('Boscadjack', 440.00325604140033), ('Gwithian', 442.0555261735786), ('Helston County Bridge', 443.3788620846717), ('Loe Pool', 445.0724593420217), ('Relubbus', 448.6500629265487), ('St Erth', 449.0347773512542), ('St Ives Consols Farm', 450.07409071624505), ('Penzance Tesco', 456.38638836619003), ('Penzance Alverton', 458.57727568406375), ('Penberth', 467.53431870130544)]

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
