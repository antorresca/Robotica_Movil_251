clear;close all;clc;
datos = load('POSE22.mat'); 
campo = fieldnames(datos); 
LidarData = datos.(campo{1});
LidarData(4:50, :) = [];%eliminacion valores 0, filas 4-50
%LidarData(LidarData < 10) = NaN;%filtro de valores menores a 10

%% Muros y plano cartesiano
function agrupar_y_graficar(ejex, ejey)
    % Verificar que los vectores tengan la misma longitud
    if length(ejex) ~= length(ejey)
        error('Los vectores ejex y ejey deben tener la misma longitud.');
    end

    % Parámetros de agrupación
    ventana_inicial = 15;%cant de datos inciales
    incremento = 3;%valor de agrandamiento de grupo
    umbral_diferencia = 10;%refina el tamaño del grupo

    n = length(ejex);
    idx_inicio = 1;
    grupos = {}; % Guardará los grupos formados

    while idx_inicio <= n
        idx_fin = min(idx_inicio + ventana_inicial - 1, n); % Definir ventana inicial
        
        while idx_fin < n
            % Evaluar diferencia entre el primer y último valor en ejex
            diferencia = abs(ejex(idx_fin) - ejex(idx_inicio));
            
            if diferencia < umbral_diferencia
                % Si la diferencia es menor al umbral, agregar más valores
                idx_fin = min(idx_fin + incremento, n);
            else
                % Si la diferencia es mayor, detener expansión
                break;
            end
        end
        
        % Guardar el grupo actual con sus valores correspondientes en ejey
        grupos{end+1} = struct('x', ejex(idx_inicio:idx_fin), 'y', ejey(idx_inicio:idx_fin));
        idx_inicio = idx_fin + 1;
    end

    % Graficar los grupos con distintos colores
    figure;
    hold on;
    colors = lines(length(grupos));
    
    for i = 1:length(grupos)
        scatter(grupos{i}.x, grupos{i}.y, 50, colors(i,:), '.', 'DisplayName', sprintf('Grupo %d', i));
        %inicio muros
        p = polyfit(grupos{i}.x, grupos{i}.y, 1);
        % Generar valores para la línea de ajuste en el rango del grupo
        x_fit = linspace(min(grupos{i}.x), max(grupos{i}.x), 100);
        y_fit = polyval(p, x_fit);
        % Graficar la línea de regresión
        plot(x_fit, y_fit, 'Color', colors(i,:), 'LineWidth', 4);
    end
    
    title('Visualizacion Hokuyo Coordenadas Cartesianas');
    xlabel('X');
    ylabel('Y');
    axis equal;
    grid on;
    hold off;
end

%% Coordenadas Polares
angulo = linspace(deg2rad(-75), deg2rad(165), length(LidarData)); % Ángulos en radianes
radio = LidarData; % Distancias medidas

figure;
polarplot(angulo, radio, 'r.'); 
title('Visualizacion Hokuyo Coordenadas Polares');
hold on;

%% Coordenadas Cartesianas 
% Convertir coordenadas polares a cartesianas
[x,y] = pol2cart(angulo,LidarData);

ordx = reshape(x,1,[]);
ordy = reshape(y,1,[]);

matrizxy=[ordx;ordy];
[ejex, indices] = sort(matrizxy(1, :)); % Ordena los valores del eje x y le da un indicce
ejey = matrizxy(2, indices);  % ordena el ejey con ls indices
matrizord = [ejex; ejey];

% Llamar la función para agrupar y graficar
agrupar_y_graficar(ejex, ejey);
