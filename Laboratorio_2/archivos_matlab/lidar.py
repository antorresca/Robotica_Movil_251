# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:42:31 2023
"""

import csv
from rplidar import RPLidar #pip install rplidar-roboticia o en https://github.com/Roboticia/RPLidar

import matplotlib.pyplot as plt
from math import radians

lidar = RPLidar('com3') #revisar puerto de comunicación

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

lidar.clean_input()  

angles = []
distances = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0, 1000) #1 metro de radio

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Numero %d datos:' % (i, len(scan)))

    # Coordenadas polares
    angles += [radians(measurement[1]) for measurement in scan]
    distances += [measurement[2] for measurement in scan]

    # Plot 
    ax.scatter(angles, distances, s=1)

    if i > 1: #Entre mayor cantidad de i, mayor cantidad de scans. 
    #(i no es igual a número de escaneos, en i=1, se lograr aprox casi 3 escaneos)
        break

# Exportar los datos a un archivo CSV
with open('lidar_data3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['angle', 'distance'])
    writer.writerows(zip(angles, distances))

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

plt.show()