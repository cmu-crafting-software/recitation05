# %%

import pandas as pd

readings = pd.read_csv('readings.csv').set_index('id')
stations = pd.read_csv('stations.csv').set_index('id')
sensors = pd.read_csv('sensors.csv').set_index('id')

print(readings.columns)
print(stations.columns)
print(sensors.columns)
how_ ='left'

readings_stations = readings.join(stations, how=how_)
readings_stations_sensors = readings_stations.join(sensors, how=how_)

# print(readings_stations)
stations_sensor = stations.join(sensors, how='outer')
readings_stations_sensors = readings.join(stations_sensor, how=how_)
print(readings_stations_sensors)
# %%
