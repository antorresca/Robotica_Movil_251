% LIMPIAR OBJETOS ANTERIORES
clear lidar
delete(instrfind);  % Cierra conexiones anteriores si las hay

% CONFIGURACIÓN DEL PUERTO SERIAL
lidar = serial('COM11','BaudRate',115200);
set(lidar, 'Timeout', 5);                   % Espera hasta 5 s por línea
set(lidar, 'InputBufferSize', 40000);       % Tamaño del buffer de entrada
set(lidar, 'Terminator', 'CR');             % Hokuyo termina con Line Feed (10)

fopen(lidar);      % Abrir conexión
pause(0.1);

% CAMBIAR A PROTOCOLO SCIP2.0
fprintf(lidar, 'SCIP2.0');
pause(0.2);
flushinput(lidar);  % Limpiar buffer después del handshake

% ----- COMANDO VV -----
fprintf(lidar, 'VV');
pause(0.2);

disp('Información del sensor (VV):');
while lidar.BytesAvailable > 0
    line = fgetl(lidar);  % Leer línea completa
    disp(line)
end

% ----- COMANDO BM (Begin Measurement) -----
fprintf(lidar, 'BM');
pause(0.2);

disp('Activación del láser (BM):');
while lidar.BytesAvailable > 0
    line = fgetl(lidar);
    disp(line)
end