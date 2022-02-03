# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.average_value = (self.typical_range[1] + self.typical_range[0])/2  # I put this in so there is a easier way of doing EX 2E
        self.latest_level = None
        self.level_history = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   average value: {}".format(self.average_value)
        return d

    def typical_range_consistent(self):
        if self.typical_range != None:
            if self.typical_range[0]<=self.typical_range[1] or self.typical_range[0]<0:
                return True
        return False

def inconsistent_typical_range_stations(stations):
    inconsistent_station_list = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_station_list.append(station)
    return inconsistent_station_list
