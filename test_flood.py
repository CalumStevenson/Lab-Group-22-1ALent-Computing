import imp
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    stationList8 = stations_level_over_threshold(stations, 0.8)
    stationList4 = stations_level_over_threshold(stations, 0.4)
    assert stationList8
    assert stationList4
    assert type(stationList8) == list
    assert type(stationList4) == list
    assert len(stationList4)>= len(stationList8)
    for item in stationList8:
        assert type(item[1] == float)
        assert item[1] == item[0].relative_level
        assert item[1]>= 0.8
    for item in stationList4:
        assert type(item[1] == float)
        assert item[1] == item[0].relative_level
        assert item[1]>= 0.4
        
def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    highest2 = stations_highest_rel_level(stations,2)
    highest10 = stations_highest_rel_level(stations,10)
    assert highest2
    assert highest10
    assert len(highest2)==2 and len(highest10) == 10
    assert highest10[:2] == highest2
