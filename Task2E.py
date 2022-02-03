
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.utils import fetch_station_list_levels
import datetime
from tqdm import tqdm

stations = build_station_list()
topTenStations = fetch_station_list_levels(stations,10,10)
for station in topTenStations:
    plot_water_levels(station,station.level_history[0],station.level_history[1])
"""   
station = stations[0]
dt = 2
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
plot_water_levels(station,dates,levels)"""