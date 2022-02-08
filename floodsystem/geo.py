# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from re import X
from .utils import sorted_by_key # noqa

from haversine import haversine
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    """This function creates tuples with station name and distance from p"""
    stations = build_station_list()
    tuples = []
    for station in stations:
        coords = station.coord
        distance = haversine(p, station.coord)
        tuples.append((station.name, distance))
    tuples = sorted_by_key(tuples, 1)
    return tuples

def stations_within_radius(stations, centre, r):
    """This function returns a list of all stations within radius r of a geographic coordinate x."""
    stations = build_station_list()
    close_stations = []
    for station in stations:
        coords = station.coord
        distance = haversine(centre, station.coord)
        if distance < r:
            close_stations.append(station.name)
    return close_stations

def rivers_with_station(stations):
    """This function creates a set containing all the river names which have a station on it. 
    It is set up so each river only occurs onece """
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return rivers

def stations_by_river(stations):
    """This function creates a dictionary with river names as a key and a list of all the 
    station names on the respective river"""
    rivers = rivers_with_station(stations)
    river_dictionary = {}
    for river in rivers:
        river_dictionary[river] = [] #Generating Empty Dictionary with all river names
    for station in stations:
        river_dictionary[station.river].append(station.name) #Assigning values to each specific river
    return river_dictionary

def rivers_by_station_number(stations,N):
    """This Function generates a list of tuples (River Name, Number of Stations) 
    ordered from highest number to lowest number of stations. It then takes the first N rivers and outputs their 
    names and numbers. Including extra rivers if they have the same number of stations as the Nth one"""
    riverList = stations_by_river(stations)
    riverStationCount = []
    for river in riverList:
        riverStationCount.append((river,len(riverList[river]))) 
    riverStationCount = sorted_by_key(riverStationCount,1,True) #RiverStation count is a list of tuples
    if N>0 and N <= len(riverStationCount): #Error Handling
        outputList = riverStationCount[0:N]
        count = 0
        if len(outputList) < len(riverStationCount): #Error Handling
            while outputList[len(outputList)-1][1] == riverStationCount[N][1]+count:
                outputList.append(riverStationCount[N+count])
                count +=1
        return outputList
    return riverStationCount #If N is not valid the whole list will be returned