from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.utils import fetch_station_list_levels
import random
from numpy import poly1d

def test_polyfit():
    stations = build_station_list()
    random.shuffle(stations)
    testList = fetch_station_list_levels(stations[:5],10,len(stations[:5]))
    for test in testList:
        poly,d0 = polyfit(test.level_history[0],test.level_history[1],4)
        assert poly
        assert type(poly) == poly1d
test_polyfit()