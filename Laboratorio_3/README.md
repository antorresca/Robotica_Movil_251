# 🤖Laboratorio 3: Introducción a la navegación con robots

## 🪶Autores

* Andres Camilo Torres Cajamarca
* Juan Camilo Gomez Robayo
* Julian Andres Gonzalez Reina
* Emily Angelica Villanueva Serna
* Elvin Andres Corredor Torres


## 1. 🏁Objetivos

* Identificar las características de los distintos tipos de navegación.
* Reconocer los algoritmos de tipo BUG y los algoritmos de resolución de laberintos.
* Aplicar al menos dos algoritmos basados en comportamientos.

## 2. 🔧➡️🚀 Procedimiento

### 2.1. 🔍📚 Búsqueda bibliográfica

1. Menciona al menos dos características de la navegación planeada y de la navegación basada en comportamientos, y cómo influyen en el tipo de respuesta del robot.

Navegación planeada: En la navegación planeada se conoce el mapa de antemano, por lo que la trayectoria a realizar también es precalculada, esto permite la optimización de la trayectoria al configurar las distancias conocidas y una velocidad adecuada para la solución de la tarea.
Navegación basada en comportamientos: En este tipo de navegación el robot no conoce el mapa y actúa de acuerdo con la información obtenida de los sensores, esta respuesta debe ser rápida para poder reaccionar de acuerdo con el entorno, en este caso se generan las trayectorias mientras evade los obstáculos del entorno y actualiza en tiempo real.


2. Investigaciones destacadas y robots desarrollados por los robotistas Rodney Brooks y Mark Tilden (máximo dos párrafos de cada uno).

Rodney Brooks
Avanzando en el campo de la inteligencia artificial aplicada y ciencias de la computación en diversas universidades como la de Carnegie Mellon, MIT o Queensland University of Technology. Ha desarrollado robots como la aspiradora Roomba, robot hexápodo Genghis, robot de movimiento autónomo Ryder, brazos robóticos como Reacher, etc.

[Rodney Brooks Home](https://people.csail.mit.edu/brooks/)
[Home - Rethink Robotics](https://rethinkrobotics.com/)


Mark Tilden
En el campo de la robótica ha diseñado o desarrollado diversos tipos de robots B.E.A.M. (Biology Electronics Asthetics Mechanics) estos están diseñados con circuitos analógicos de manera que se mantienen lo mas simple posibles al no integrar microcontroladores, haciendolos de igual manera menos adaptativos. Tambien es conocido por desarrollar el robot robosapien un robot de entretenimiento con un movimiento fluido y variedad de gestos, así como también el robot Femisapien 

[BEAM Robotics - Robohub](https://robohub.org/robots-beam-robotics/)
[WowWee Robosapien X](https://wowwee.com/robosapien-x/)

3. Mencione al menos tres algoritmos de planificación de rutas para espacios con obstáculos.

  - Tetha*
  - A*
  - D*
  - D* Enfocado
En el siguiente video una aplicacion del algoritmo A* en los videojuegos

<p align="center">
  <a href="https://youtu.be/hQa9JTtq4Ok">
    <img src="https://img.youtube.com/vi/hQa9JTtq4Ok/0.jpg" alt="Aplicación del algoritmo A* en videojuegos" />
  </a>
</p>
  
5. Describa brevemente los algoritmos Bug 0, Bug 1 y Bug 2.
   
Un algoritmo Bug es un tipo de algoritmo de planeacion de movimiento usado en robotica , particularmente para la navegacion de robots mobiles en ambientes con obstaculos desconocidos
  - Bug 0 : Es el algoritmo bug mas sencillo y consiste en seguir el borde del obstaculo hasta que encuentre una ruta disponible a la cual llegar, sin embargo este algoritmo puede fallar en escenarios donde el robot encuentra obstaculos donde requiera un movimiento de retroceso. 
  - Bug 1 : A diferencia del algoritmo Bug 0, este algoritmo garantiza que si existe una ruta hasta la meta el robot la alcanzará y consiste en seguir completamente el borde del obstaculo registrando el punto mas cercano entre el objeto y la meta. Al momento de encontrar el punto sigue su camino hacia la meta.
  - Bug 2 : Este algoritmo es el mas eficiente de todos gracias a su capacidad de minimizar desvios innecesarios. Su funcionamiento es similar a los dos algoritmos anteriores, pero su diferencia es que este algoritmo traza una linea recta entre el inicio y la meta, esta linea es seguida por el robot hasta que encuentra un obstaculo, el robot sigue el borde del obstaculo hasta que vuelve a encontrar la linea para posteriormente seguirla hasta llegar a la meta.
 
6. Describa al menos un algoritmo de solución de laberintos (maze algorithm) aplicado en robótica móvil.
   
Uno de los algoritmos mas utilizados para la solución de laberintos es el algoritmo A*, sus principales ventajas es que siempre encuentra rutas optimas si las heuristicas son apropiadas y se ajusta segun los movimientos permitidos , tambien es capaz de de penalizar giros si se agregan a la funcion de costo, este algoritmo como se menciona anteriormente utiliza heuristicas para encontrar la ruta mas corta hasta la meta, considerando la distancia recorrida y una estimacion del camino restante. Este algoritmo modela el laberinto como un grafo donde cada nodo es una posicion y las aristas corresponden a los posibles movimientos cercanos .

La funcion de costo , esta compuesta por f(n)=g(n)+h(n) donde g(n) hace referencia al costo acumulado desde el inicio hasta el nodo (n) , h(n) es la estimacion heuristica del costo restante hasta la meta . Luego se hace un proceso iterativo con el nodo inicial, en cada paso se extrae el nodo menor, se expanden generando sus vecinos y se actualizan g y f . El proceso iterativo finaliza hasta alcanzar una meta.

### 2.2. 🏎️↪️🧱 Misión 1: Evite los obstáculos
Para la primera misión se implemento un algoritmo bug 2 con python mediante conexion SSH al robot lego EV3

<div align="center">
  <video src="https://github.com/user-attachments/assets/0f4b8e7e-829b-46dd-acc9-d15be1c27d49" />
</div>


### 2.3. 🏎️🔀🏁 Misión 2: Supere el laberinto
Para el desarrolo del algoritmo maze se implementaron dos tecnicas de programación :

La primer tecnica fue un seguidor de pared izquierda programado mediante la programación de bloques EV3, la cual es la siguiente.

<div style="display: flex; justify-content: center; gap: 10px;" align="center">
<img src="https://github.com/user-attachments/assets/c19e08f2-8c26-444b-8e37-66641ea77d77" width="500"  title="infizq">
</div>



<p align="center">
  <a href="https://youtu.be/VwreGX4NfRQ">
    <img src="https://img.youtube.com/vi/VwreGX4NfRQ/0.jpg" alt="Laboratorio 3 - Introducción a la navegación con robots" />
  </a>
</p>

La segunda tecnica fue el uso de python utilizando la conexión SSH del robot EV3

<div align="center">
  <video src="https://github.com/user-attachments/assets/b3cf9e77-22b0-431d-8fb4-1d50ca97d32f" />
</div>






