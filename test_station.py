# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import set_relative_water_levels

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    latest_level = 3.6
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.average_value == (trange[0] + trange[1])/2
    s.latest_level = latest_level
    assert s.latest_level
    relative = s.relative_water_level()
    assert relative
    assert s.relative_level
    assert s.relative_level == relative

def test_inconsistent_range_station():
    stations = build_station_list()
    inconsistentBasic = inconsistent_typical_range_stations(stations[:10])
    consistentBasic = inconsistent_typical_range_stations(stations[:10],True)
    consistentBasic20 = inconsistent_typical_range_stations(stations[:20],True)
    inconsistentBasic20 = inconsistent_typical_range_stations(stations[:20])
    assert type(inconsistentBasic) == list
    assert type(consistentBasic) == list
    assert type(inconsistentBasic20) == list
    assert type(consistentBasic20) == list
    assert len(consistentBasic) <= len(consistentBasic20)
    assert len(inconsistentBasic) <= len(inconsistentBasic20)

def test_set_relative_levels():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    trange2 = (1.2,4.6652)
    river = "River X"
    town = "My Town"
    latest_level = 3.6
    latest_level2 = 4.1
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s.latest_level = latest_level
    s2.latest_level = latest_level2
    set_relative_water_levels([s,s2])
    assert s.relative_level
    assert s.relative_level
    assert s2.relative_level
    assert s2.latest_level
    assert s.relative_level == (s.latest_level-s.typical_range[0])/s.typical_range[1]
    assert s2.relative_level == (s2.latest_level-s2.typical_range[0])/s2.typical_range[1]