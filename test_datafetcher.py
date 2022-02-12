# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_latest_water_level_data

def test_build_station_list():

    # Build list of stations
    stations = build_station_list()

    # Find station 'Cam'
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break

    # Assert that station is found
    assert station_cam

    # Fetch data over past 2 days
    dt = 2
    dates2, levels2 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates2) == len(levels2)

    # Fetch data over past 10 days
    dt = 10
    dates10, levels10 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates10) == len(levels10)
    assert len(dates10) > len(levels2)

def test_fetch_latest_water_level_data():
    stations = build_station_list()
    data = fetch_latest_water_level_data()
    assert data
    assert type(data) == dict

def test_fetch_measure_levels():
    stations = build_station_list()
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break
    assert station_cam
    dates2, levels2 = fetch_measure_levels(station_cam.measure_id,dt = datetime.timedelta(days = 2))
    dates10, levels10 = fetch_measure_levels(station_cam.measure_id,dt = datetime.timedelta(days = 10))
    assert dates2
    assert levels2
    assert dates10 
    assert levels10
    assert len(dates2) == len(levels2) and len(dates10) == len(levels10)
    assert len(dates2) < len(dates10)