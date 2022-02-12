"""Unit test for the utils module"""

from distutils.command.build import build
import floodsystem.utils
from floodsystem.stationdata import build_station_list
from floodsystem.utils import fetch_station_list_levels
from floodsystem.station import MonitoringStation
def test_sort():
    """Test sort container by specific index"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2)
    assert list1[0] == b
    assert list1[1] == a
    assert list1[2] == c


def test_reverse_sort():
    """Test sort container by specific index (reverse)"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2, reverse=True)
    assert list1[0] == c
    assert list1[1] == a
    assert list1[2] == b

def test_fetch_station_list_levels():
    stations = build_station_list()
    stations = stations[:10]
    top2Stations = fetch_station_list_levels(stations,1,2)
    top5Stations = fetch_station_list_levels(stations,1,5)
    assert top2Stations
    assert top5Stations
    assert type(top2Stations) == list
    assert type(top5Stations) == list
    assert len(top2Stations)<= len(top5Stations)
    for i in top2Stations:
        assert type(i) ==MonitoringStation
    for i in top5Stations:
        assert type(i) == MonitoringStation
