data = readtable('lidar_data1.csv');
angle = data.angle;
distance = data.distance/1000;

scan1 = lidarScan(distance, angle);
plot(scan1)

% Creación de Mapa
map = occupancyMap(0.6, 0.6, 200);

% Pose
pose = [0.17, 0.32, pi/2];

%Rango maximo
maxRange = 0.70;

insertRay(map, pose, scan1, maxRange);

figure;
show(map)
title('Mapa de Ocupación con Datos LIDAR')



%%

poses = [0.17, 0.32, pi/2;
         0.21, 0.42, pi;
         0.6, 0.54, 3/2*pi];

% Construccion del mapa
mapa=buildMap({scan1, scan2, scan3}, poses, 200, 0.7);
show(mapa)