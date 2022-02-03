import datetime
from tqdm import tqdm
from floodsystem.datafetcher import fetch_measure_levels
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def fetch_station_list_levels(stations,dt,N):
	topNStations = []
	for station in tqdm(stations, desc = "Loading: "):
		dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
		
		count = 0
		try:
			station.latest_level = levels[0]
		except:
			if type(levels) == int:
				station.latest_level = levels
				
			elif type(levels) == str:
				if levels.isdigit():
					station.latest_level = int(levels)
				else:
					station.latest_level = station.average_value   
			else:
				station.latest_level = station.average_value
			levels = []
			while len(levels) < len(dates):
				levels.append(station.latest_level) 
		station.level_history = (dates,levels)

		if len(topNStations) == 0:
			topNStations.append(station)
		else:
			for i in range(len(topNStations)):
				if (station.latest_level - station.average_value) > (topNStations[i].latest_level - topNStations[i].average_value):
					topNStations.insert(i,station)
					count = 1
					break
			if len(topNStations) <= N and count == 0:
				topNStations.append(station)
			elif len(topNStations)> N:
				topNStations.pop(len(topNStations)-1)
	return topNStations
