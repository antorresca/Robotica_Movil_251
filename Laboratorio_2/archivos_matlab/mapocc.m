close all;clear; clc;
map = occupancyMap(540,360,5);%introducir X,Y,Pixels
maxrange = 180;%rango maximo del sensor en mm/corta datos fuera de eso
pose1 = [180,270,0];%sitio real del sensor X,Y(mm)
angN1=180;
angm1=angN1-120;
angM1=angN1+120;


pose2 = [360,270,0];%sitio real del sensor X,Y(mm)
angN2=-45;
angm2=angN2-120;
angM2=angN2+120;

pose3 = [400,145,0];%sitio real del sensor X,Y(mm)
angN3=45;
angm3=angN3-120;
angM3=angN3+120;

%% Adquisicion RAWDATA
datos1 = load('POSE11.mat'); 
datos2 = load('POSE22.mat'); 
datos3 = load('POSE33.mat'); 
campo1 = fieldnames(datos1);
campo2 = fieldnames(datos2);
campo3 = fieldnames(datos3);
LidarData1 = datos1.(campo1{1});
LidarData2 = datos2.(campo2{1});
LidarData3 = datos3.(campo3{1});

%% Scan_Pose_1 
fila11 = LidarData1(1, :);
fila12 = LidarData1(2, :);
fila13 = LidarData1(3, :);
%% Scan_Pose_2
fila21 = LidarData2(1, :);
fila22 = LidarData2(2, :);
fila23 = LidarData2(3, :);
%% Scan_Pose_3
fila31 = LidarData3(1, :);
fila32 = LidarData3(2, :);
fila33 = LidarData3(3, :);

angles1 = linspace(deg2rad(angm1), deg2rad(angM1), length(LidarData1));
angles2 = linspace(deg2rad(angm2), deg2rad(angM2), length(LidarData2));
angles3 = linspace(deg2rad(angm3), deg2rad(angM3), length(LidarData3));
%% Trazado pose 1
scan11 = lidarScan(fila11,angles1);
insertRay(map,pose1,scan11,maxrange);
scan12 = lidarScan(fila12,angles1);
insertRay(map,pose1,scan12,maxrange);
scan13 = lidarScan(fila13,angles1);
insertRay(map,pose1,scan13,maxrange);
%% Trazado pose 2
scan21 = lidarScan(fila21,angles2);
insertRay(map,pose2,scan21,maxrange);
scan22 = lidarScan(fila22,angles2);
insertRay(map,pose2,scan22,maxrange);
scan23 = lidarScan(fila23,angles2);
insertRay(map,pose2,scan23,maxrange);
%% Trazado pose 3
scan31 = lidarScan(fila31,angles3);
insertRay(map,pose3,scan31,maxrange);
scan32 = lidarScan(fila32,angles3);
insertRay(map,pose3,scan32,maxrange);
scan33 = lidarScan(fila33,angles3);
insertRay(map,pose3,scan33,maxrange);

show(map);