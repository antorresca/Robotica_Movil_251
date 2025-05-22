# 🤖Laboratorio 2: Introducción al uso de sensores y ROS

## 🪶Autores

* Andres Camilo Torres Cajamarca
* Juan Camilo Gomez Robayo
* Julian Andres Gonzalez Reina
* Emily Angelica Villanueva Serna
* Elvin Andres Corredor Torres

## Indice de Entregas

[Entrega 1](#entrega-1)

[Entrega 2](#entrega-2)

---
# ENTREGA 1

## 1. 🏁Objetivos

* Familiarizarse con el uso e implementación de sensores.
* Comprender los principios de funcionamiento de diferentes tipos de sensores, así como sus implicaciones en sistemas de adquisición de datos.
* Evaluar la incertidumbre asociada a las mediciones obtenidas mediante sensores, aplicando métodos estadísticos básicos.
* Realizar el manejo de las plataformas robóticas disponibles a través del uso de ROS (Robot Operating System).

## 2. 🔧➡️🚀 Procedimiento

### 2.1. 🔍📚 Búsqueda bibliográfica

1. ¿Qué es el Vocabulario Internacional de Metrología (VIM)?
El Vocabulario Internacional de Metrología es una norma internacional que proporciona definiciones normalizadas para los conceptos fundamentales utilizados en metrología. Su objetivo es unificar el lenguaje técnico en medición para facilitar la comunicación en contextos científicos y en entornos industriales.

2.	Según el VIM, defina los siguientes conceptos:
  * Exactitud de medida: La exactitud de medida se interpreta como la proximidad entre los valores medidos atribuidos al mensurando.
  * Precisión de medida: Se refiere al grado de concordancia entre resultados de mediciones repetidas bajo condiciones específicas. Está relacionada con la repetibilidad y reproducibilidad, pero no necesariamente con la exactitud.
  * Error de medida: Diferencia entre el valor medido y el valor verdadero de una magnitud. Puede ser sistemático o puede ser aleatorio.
  * Incertidumbre de medida Parámetro asociado a una medición que caracteriza la dispersión de los valores atribuibles al mensurando.

3.	Explique la diferencia entre un error sistemático y un error aleatorio.
  * Sistemático: 	Es predecible y constante. Se debe a errores del instrumento o del método. Puede corregirse.
  * Aleatorio: Es impredecible y variable. Se debe a factores no controlados como temperatura o vibraciones. No se puede eliminar, solo minimizar.

4. De acuerdo con la teoría estadística: ¿qué es el valor medio? ¿Qué magnitudes se utilizan para medir la dispersión de los datos?
  * Valor medio: Es el resultado de la suma de todas las mediciones dividida por el número total de mediciones. Representa el valor central de una distribución.
  * Magnitudes para medir la dispersión:
      * Varianza: Promedio de las desviaciones cuadráticas respecto al valor medio.
      * Desviación estándar: Raíz cuadrada de la varianza; indica cuánto se dispersan los valores respecto a la media.
      * Rango: Diferencia entre el valor máximo y el mínimo.
      * Coeficiente de variación: Relación entre la desviación estándar y la media.

7.	Busque una definición de que es ROS y sus principales ventajas
El sistema operativo robótico (ROS) se define como un framework diseñado para el desarrollo de software robótico. ROS no funciona como un sistema operativo independiente, sino como un middleware, que aprovecha sistemas operativos convencionales como Linux y proporciona a los desarrolladores un conjunto de bibliotecas y herramientas para crear aplicaciones robóticas sofisticadas y resistentes.
  * Ventajas de ROS:
     * Arquitectura distribuida basada en nodos.
     * Reutilización de código mediante paquetes.
     * Soporte para múltiples lenguajes (Python, C++).
     * Simulación con Gazebo y visualización con Rviz.
     * Gran comunidad y paquetes disponibles (por ejemplo, navegación, SLAM, visión, etc.).
     * Escalabilidad para robots complejos.
    
6.	Investigue sobre qué comandos se pueden usar con rosnode, rostopic, rosparam, rosservice, rosmsg y rospack.
  * rosnode-> Interactúa con los nodos de ROS. Ej.: rosnode list, rosnode info
  * rostopic-> Trabaja con temas. Ej.: rostopic echo, rostopic pub, rostopic list
  * rosparam-> Administra parámetros del servidor maestro. Ej.: rosparam set/get
  * rosservice-> Llama o inspecciona servicios. Ej.: rosservice list/call
  * rosmsg-> Visualiza estructuras de mensajes. Ej.: rosmsg show
  * rospack-> Busca información sobre paquetes. Ej.: rospack find <paquete>
 7. Investigue acerca del robot TurtleBot2 y su relación con la base Kobuki.
  * TurttleBot2 es un kit de robot de bajo costo con software de codigo abierto cuya esturctura  esta conformado por la base robotica movil Kobuki que cuenta con sensores de deteccion de obstaculos, sensores de odometria y sensores de inclinacion, ademas proporciona energia al sistema esterno , sensores externos , actuadores y otros componentes.

8. ¿Para que sirve los sensores cliff en el Kobuki?
 * Los sensores Cliff en español sensores de precipicio tienen como funcion detectar desniveles o bordes en el suelo , como escaleras para evitar que el robot caiga . En sensor detecta un cambio de nivel , inmediatamente detiene cualquir moviemiento del robot , es un comando que tiene prioridad.
   
9. ¿Como leer un evento de dicho sensor?
 * Cuando el sensor detecta un desnivel , inmediatamente genera un evento , es necesario suscribirse al topico /mobile_base/events/cliff , el cual publica mensajes de tipo kobuki_msgs/CliffEvent , el mensaje tiene los siguientes campos
 * sensor : 0: izquierdo , 1: centro, 2: derecho
 * estado : 0: piso , 1: precipicio
 * bottom : valor analogico de la señal infraroja 
   
10. ¿Qué protocolo de comunicación usa el Lego Ev3 con sus sensores y actuadores?
 * El LEGO EV3 utiliza principalmente el protocolo I²C para comunicarse con sus sensores inteligentes conectados a los puertos 1-4, lo que permite el intercambio digital de datos como distancia, color o rotación. Algunos sensores también pueden usar UART o señales analógicas según el diseño. En cuanto a los actuadores (motores conectados a los puertos A-D), el EV3 emplea señales de PWM para controlar la potencia y dirección, junto con retroalimentación de encoders para medir posición y velocidad. Este sistema de comunicación es propietario y está optimizado para facilitar la conexión automática y segura de módulos LEGO.
 
11. ¿Qué opciones de conexión permiten integrar sensores no nativos al sistema LEGO EV3?
 * El sistema LEGO EV3 permite integrar sensores no nativos mediante los puertos de sensor utilizando protocolos estándar como I²C o UART, siempre que el sensor respete el voltaje y la estructura del conector. También es posible usar el pin de identificación analógica para que el EV3 reconozca el dispositivo. Otra opción es conectar sensores a través de una Raspberry Pi o una placa Arduino, comunicándose con el EV3 por Bluetooth, Wi-Fi o USB, lo que amplía las posibilidades mediante sistemas como ev3dev o entornos de programación como Python o C++.


### 3. 👀🫲🏼👂🏼🤖🧠 Sensores

#### 3.1. 🔦👀🌐🔭 Sensor HOKUYO

Para el desarrollo de estas practica se realizo el procedimiento establecido en el repositorio de GithUb, el cual indicaba que se debia verificar la funcionalidad del sensor Hokuyo por medio del software URG Benri data viewing tool. A continuacion se muestra la toma de datos realizada por el sensor con el software.

Utilizando la funcion de LidaScan se grafica las paredes detectadas por el sensor en un scanedo de 682 grados. Por otro lado, estos mismos datos son utilizados para graficar el mapa de ocupacion que se puede ver en escala de grises.

#### Pose 1 sensor HOKUYO
<div align="center">
 <img src="https://github.com/user-attachments/assets/9324871e-517c-43a6-b707-a7720c09e8ec" width="900">
</div>

#### Pose 2 sensor HOKUYO

<div align="center">
 <img src="https://github.com/user-attachments/assets/a7ebd92e-e2ea-43be-8e75-cca82f4736bf" width="900">
</div>

#### Pose 2 sensor HOKUYO

<div align="center">
 <img src="https://github.com/user-attachments/assets/1044d498-1c7e-4ebf-88f0-10853d04d28e" width="900">
</div>

Finalmente, se realiza el mapa de ocupacion completo, obtenido de cada una de las poses detallando asi el espacio en el que se encuentra el sensor.

<div align="center">
 <img src="https://github.com/user-attachments/assets/383d0009-3352-4955-ac84-bebabc73669f" width="600">
</div>

Errores identificados

* Ruido de baja densidad. En la unión de escaneos, hay puntos sueltos o ruido que no pertenece a ninguna superficie clara. Esto esta causado por:
  * Reflexiones en paredes no perfectamente mates.
  * Interferencia con fuentes de luz.
  * Valores atípicos (outliers) no filtrados del LIDAR.
  * Vibración o inestabilidad del sensor durante el escaneo

* Zonas con datos faltantes. El mapa presenta sectores oscuros o sin datos (zonas negras), especialmente hacia los extremos del ángulo de visión. Esto se debe a:
  * Objetos fuera del rango de escaneo, ya que el sensor no detenta en rangos de -120 - 120 grados.
  * Ruido o lecturas nulas del sensor que fueron descartadas.
    
#### 3.2. 🔦👀🌍📡 Sensor RPLIDAR

El sensor RPLidar es un sensor el cual utiliza luz láser para medir distancia a objetos, para esta práctica se hace una adquisición de datos utilizando los algoritmos de python puestos a nuestra disposición en el GitHub de la clase [lidar.py](archivos_matlab/lidar.py), colocando el sensor en tres poses diferentes con el fin de recrear con algoritmos de matlab el laberinto utilizado para las pruebas .

Se utiliza el comando LidarScan de matlab para graficar los datos obtenidos y el comando insertRay para graficar las paredes detectadas por el sensor y simular el láser del sensor [Codigo_LidarScan_BuildMap.m](archivos_matlab/Codigo_LidarScan_BuildMap.m). Finalmente se utiliza el comando buildMap para recrear el espacio completo donde se tomaron los datos. 
Se toma el siguiente marco de referencia fijo para poder colocar las poses, todas las poses están en Metros y radianes  

#### Marco de referencia fijo


<div align="center">
 <img src="https://github.com/user-attachments/assets/43a26d2e-3a24-4882-80e3-9d5122867280" width="500">
</div>

#### Pose 1 [0.62, 0.54, 3/2*pi]

<div align="center">
  <img src="https://github.com/user-attachments/assets/8eaa874a-1182-4444-9f86-2eb09c5760fe" width="45%" style="display:inline-block; margin-right: 10px;">
  <img src="https://github.com/user-attachments/assets/96671c00-5d7f-4a69-80fe-a4eb4ef3284f" width="45%" style="display:inline-block;">
</div>

<div align="center">
 <img src="https://github.com/user-attachments/assets/df3c0cd2-cb6f-4426-b64c-e9b083a1fecd" width="500">
</div>



#### Pose 2 [0.17, 0.32, pi/2]

<div align="center">
 <img src="https://github.com/user-attachments/assets/6c5acfdc-84ff-4cc0-8d2a-e59a2ad37467"  height="350px" width="45%" style="display:inline-block; margin-right: 10px;">
 <img src="https://github.com/user-attachments/assets/5a88a763-5b02-4d92-ad34-1cf5c41c59c3" width="46%" style="display:inline-block;">
 
</div>



<div align="center">
 <img src="https://github.com/user-attachments/assets/eea8bc5a-10bd-4615-b488-291aafc57e23" width="500">
</div>



#### Pose 3 [0.21, 0.42, pi]

<div align="center">
 <img src="https://github.com/user-attachments/assets/0e242a55-cd3e-45f3-b855-80be6060244a" height="350px" width="45%" style="display:inline-block; margin-right: 10px;">
 <img src="https://github.com/user-attachments/assets/0f47c98b-99a8-43a2-8e0f-299a64694d10" width="46%" style="display:inline-block;">
</div>

<div align="center">
 <img src="https://github.com/user-attachments/assets/f3d3e328-ac05-407e-bce0-fb0ea6f50011" width="500">
</div>

#### Mapa de Ocupacion Completo 

<div align="center">
 <img src="https://github.com/user-attachments/assets/3b11bcbf-7fd5-40fd-8043-7999582f1c95" width="500">
</div>

Errores identificados
* Rangos de Medición
  * El rango de medición de este sensor es de 0.15 metros a 12 metros en algunos casos del experimento el cable de envío de datos quedo muy cerca al sensor, debido a esto en algunas ubicaciones no se pudieron adquirir datos.
  * Al estar en rotación constante la vibración del sensor afecta con la adquisición de datos



#### 3.3. 🔊📡📏 Sensor de ultrasonido

De acuerdo a las instrucciones se realzó el montaje experimental para comprobar la presición del sensor de ultrasonido HC-SR04, se realiza la toma de muestras a 1m, 1,6m y 2,1m. Para cada distancia se realiza la toma de 100 muestras y se calcula el error absoluto, el error relativo, la distancia media y la desviación estandar. 

Montaje experimental realizado
<div align="center">
 <img src="https://github.com/user-attachments/assets/4be9b597-d38b-4d2d-a486-7953dbcfe118" width="900">
</div>

En la siguiente imagen se muestran las graficas de las mediciones para 100 cm, obteniendo una distancia media de 95.6020 cm, una desviación estandar de 7.6605 
<div align="center">
<img src="https://github.com/user-attachments/assets/105a107f-73ef-490d-9e65-1f58bb94430f" width="900">
</div>

A continuación se muestran las graficas de error absoluto y error medio en cada punto
<div align="center">
<img src="https://github.com/user-attachments/assets/28945dae-524b-40a9-9423-0e9a31b0d904" width="900">
</div>

En la siguiente imagen se muestran las graficas de las mediciones para 160 cm, obteniendo una distancia media de 156.2359 cm, una desviación estandar de 0.0195 
<div align="center">
<img src="https://github.com/user-attachments/assets/d78e7134-1ffc-4125-8e01-252676e8fbd8" width="900">
</div>

A continuación se muestran las graficas de error absoluto y error medio en cada punto
<div align="center">
<img src="https://github.com/user-attachments/assets/b855aea3-e403-492c-b116-e5de533fdb95" width="900">
</div>

En la siguiente imagen se muestran las graficas de las mediciones para 160 cm, obteniendo una distancia media de 206.0456 cm, una desviación estandar de 0.1886 
<div align="center">
<img src="https://github.com/user-attachments/assets/731d4e62-dc45-449e-8dce-71fc4229acb3" width="900">
</div>

A continuación se muestran las graficas de error absoluto y error medio en cada punto
<div align="center">
<img src="https://github.com/user-attachments/assets/4408eef4-8d43-4fae-b63b-68e482f81bb6" width="900">
</div>

**Análisis de resultados**
Como se aprecia en las gráficas, en la medida que se incrementó la distancia de medición la desviación estandar disminuyó, es decir la precisión mejoró con la distancía.
En las gráficas se presentan los mejores resultados, sin embargo, se pudo deducir que el sensor es muy susceptible al ruido y perturbaciones.
En la toma de medidas para una distancia de 100 cm, aparecieron longitudes que diferían en más de un 50% del valor real.
La diferencia de la sdistancia media con respecto a la distancia real se mantuvo entre los 4 y 5 cm independientemente de la longitud medida, lo cual nos permite pensar que el sensor mantiene la precición más sin embargo no es confiable con una sola medida, es necesario tener un conjunto de medidas para hacer una buena aproximación al valor real, resaltando que los valores medidos siempre estuvieron por debajo del valor real de distancia.


#### 3.4. 📡🧭🧱 Sensores Lego

##### 3.4.1 ↕️Linea recta

Para el procedimiento con los sensores Lego, empleando el mindstorms ev3, en primer lugar se construyó el siguiente programa [Linea_Recta.mlsp](Archivos_EV3/Linea_Recta.mlsp) en la Aplicación oficial _EV3 Classroom_ para lograr que el robot se moviera en linea recta.

<div align="center">
 <img src="https://github.com/user-attachments/assets/167502a5-a23f-4c67-873c-1f5d7fda11cd" width="300">
</div>

Este programa, hacia que el robot se moviera en linea recta hasta detectar un objeto a menos de 5 _cm_. Como se puede observar en el siguiente video,


https://github.com/user-attachments/assets/ee291814-7428-4ab5-ab27-86ec813b11f5


Ahora bien, para poder lograr que recorriera aproximadamente 1 metro se tuvo en cuenta que el objeto que iba a lograr que se deteniera estuviera a 105 cm (1.05 m) del extremo del robot. Al finalizar el recorrido, el robot mostraba la distancia inicial y la distancia final medida por el sensor ultrasonido y los grados medidos por cada una de las ruedas considerando 0 cuando empieza el recorrido. Al emplear dicho programa se obtuvo:

<div align="center">
 <img src="https://github.com/user-attachments/assets/9830f6f9-716a-446e-810a-72182d5f6d13" width="300">
</div>

Es decir,

|Dato|Unidad|Descripción|
|----|------|-----------|
|105.2|cm|Distancia inicial del sensor ultrasonico hasta el objeto|
|4.6|cm|Distancia final del sensor ultrasonico hasta el objeto|
|2071|°|Grados del encoder recorridos por rueda derecha|
|2075|°|Grados del encoder recorridos por rueda izquierda|

A apartir de dichos datos, se calculó la distancia recorrida, primero con los datos de cada rueda, para ello, se tiene en cuenta que

$$ P = 2 \cdot \pi \cdot r$$

donde $P$ es el perimeto de la rueda, es decir la distancia que recorre al girar 1 vuelta completa y $r = 0.028 \text{m}$ que es el radio de la rueda. 

$$ P = 2 \cdot \pi \cdot 0.028 = 0.1759 \text{m}$$

Ahora, para hallar la distancia teniendo en cuenta los grados se tiene que 

$$ d = m_{grados} \cdot \frac{P}{360^{o}} $$

y con los datos obtenidos se tiene que 

$$ d_1 =  2071^{o} \cdot \frac{0.1759}{360^{o}} = 1.0121 \text{m}$$
$$ d_2 =  2075^{o} \cdot \frac{0.1759}{360^{o}} = 1.0140 \text{m}$$

obteniendo un promedio de $d_{prom} = 1.0131 \text{m}$ dando un error relativo de $1.31$%

Por el lado, para ver el funcionamiento del sensor ultrasonico, se tiene que

$$ d_u = d_f - d_i = 105.2 - 4.6 =  100.6 \text{cm} = 1.006 \text{m}$$

con ello, se tiene un error relativo de $0.6$%. Colocando los datos en una tabla tenemos que,

|Sensor|Medida obtenida (cm)|Error relativo (%)|
|------|---------------|--------------|
|Ultrasónico|100.6| 0.6 |
|Encoder Rueda| 101.31 | 1.31 |

Con ello se puede decir que el sensor ultrasonico tiene una mayor exactitud que el sensor del encoder de la rueda.

##### 3.4.2 🔄️ Giro en rueda

Para este procedimiento, de igual manera que en la sección [3.4.1 ↕️Linea recta](#341-%EF%B8%8Flinea-recta) se crearon los programas [Giro_30.lmsp](Archivos_EV3/Giro_30.lmsp) y [Giro_45.lmsp](Archivos_EV3/Giro_45.lmsp) en la aplicación _EV3 Classroom_, el codigo en bloques de uno de esos programas se puede ver en la siguiente imagen

<div align="center">
 <img src="https://github.com/user-attachments/assets/16576a92-f2c8-4f55-9fad-aec63b695279" width="300">
</div>

En este programa, el robot gira el Motor conectado al puerto _B_ 30° cada 15 segundos, tiempo suficiente para tomar la medida con un instrumento externo, en este caso con un goniometro, dicho proceimiento se realizó 3 veces, como se observa en las siguientes fotos:

<div style="display: flex; justify-content: center; gap: 10px;">
 <img src="https://github.com/user-attachments/assets/5025361f-e480-42ad-8605-d7d3ace4c2b6" width="300">
 <img src="https://github.com/user-attachments/assets/48754ffe-e9a8-4ee2-8f3e-2cdbb0262e4f" width="300">
 <img src="https://github.com/user-attachments/assets/c7c5fcee-bea7-4113-b4d5-6f5e4b085461" width="300">
</div>

Para mejor comprensión, se colocaron los valores en la siguiente tabla

|No. Prueba|Angulo Encoder (°) |Distancia Goniometro (°) |Error relativo (%)|
|------|------|------|------|
|1|30|29|3.45|
|2|60|59|1.69|
|3|90|89|1.12|

Dandonos un error en promedio de $2.08$%

De igual forma se hizo el giro de 45° dando,

<div style="display: flex; justify-content: center; gap: 10px;">
 <img src="https://github.com/user-attachments/assets/33599d53-40d4-43ab-9ae0-55a553c23071" width="300">
 <img src="https://github.com/user-attachments/assets/ef313110-2b36-49d5-aea2-9cb68aa63ecd" width="300">
 <img src="https://github.com/user-attachments/assets/c0801508-86c0-4aee-a1d2-3aafa61df9a0" width="300">
</div>

|No. Prueba|Angulo Encoder (°) |Distancia Goniometro (°) |Error relativo (%)|
|------|------|------|------|
|1|45|45|0|
|2|90|89|1.12|
|3|135|44(Angulo interno)|0.74|

Y con estos datos nos dio un error en promedio de $0.62$%

---
## ENTREGA 2

### 4. 🌐🤖 ROS

#### 4.1. 🗂️🌐🤖 Uso de ROS


<div style="display: flex; justify-content: center; gap: 10px;"  align="center">
  <img src="https://github.com/user-attachments/assets/920aa521-c4bf-4183-a66f-12564db9823a" width="500" title="pysubposepy">
</div>
Publicaion de Pose con pysubposepy

<div style="display: flex; justify-content: center; gap: 10px;" align="center">
 <img src="https://github.com/user-attachments/assets/db4d8e2c-0ff0-45ff-aedd-42f41f58e203" width="500"  title="pypubvel">
</div>
Trayectoria Aleatoria de Turtlesim con pypubvel


Posiones publicada usando 



#### 4.2. 🌐🐢🤖 ROS Kuboki

#### 4.3. 🌐🧱🤖 ROS Lego EV3

1.1. Lectura de sensores



1.2. GUI teleoperacion



2. Rutina




# 5. 🪶 Referencias

* V. Mazzari, «I2C communication: Lego Mindstorms NXT brick, sonar sensor and a Saleae logic analyser», Génération Robots - Blog, 23 de febrero de 2023. Disponible en: https://www.generationrobots.com/blog/en/i2c-communication-lego-mindstorms-nxt-brick-sonar-sensor-and-a-saleae-logic-analyser/?srsltid=AfmBOoof5rZjMT62RZPMTAu3v9xz6ochArpMappM3TvVxX7Lxs3yxEUz
* ev3dev.org, «Input / Output Ports — ev3dev-jessie Linux kernel drivers 19 documentation». Disponible en: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/ports.html

