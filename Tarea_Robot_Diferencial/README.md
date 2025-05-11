# 👾Tarea: Cinemática Robot Diferencial

## 🏁Objetivos

## 📖Fundamentos Teóricos 

Para el cálculo teórico se siguió la presentación *XX* disponible en el Moodle del curso, de allí se extrajo las siguientes ecuaciones para cinemática directa de robots con ruedas:

$$ \dot{X}_M = 
\begin{bmatrix}
v \\ 
\omega 
\end{bmatrix} = \begin{bmatrix} 
\frac{r}{2} & \frac{r}{2} \\ 
0 & 0 \\ 
\frac{r}{2l}&  \frac{r}{2l}\\ 
\end{bmatrix} \cdot \begin{bmatrix} 
\dot{\phi_1} \\ 
\dot{\phi_2} \end{bmatrix} $$

En las que se relaciona la velocidad angular de las ruedas (en $rad/s$) con la velocidad lineal (en $m/s$) y angular (en $rad/s$) del robot. Por otro lado, si se necesita la velocidad con respecto al marco fijo se puede obtener mediente

$$ \dot{X}_F = R_{M}^{F} \cdot \dot{X}_F  $$

## 🎢Procedimiento

### Trayectoria Recta

Tomando $r = 0.028 \text{m}$ y $l = 0.059 \text{m}$ y que $\dot{\phi}_n = 2.85 \text{rad/s}$ considerando la velocidad máxima de los motores Lego, y que se usó el 20% de este velocidad. A partir de dichos valores, se realizaron los calculos de la velocidad lineal y angular del robot

$$ v = 0.0798 \text{m/s} $$
$$ \omega = 0 \text{rad/s} $$


#### Datos Reales con MatLab

Para la trayectoria recta se le asignó la velocidad del 20% a los motores derecho e izquierdo; y con el programa descrito en el archivo [TomaDeDatos.m](scripts/TomaDeDatos.m) se obtuvo la siguiente gráfica que describe la posición angular de cada una de las ruedas mientras el robot está en movimiento

<div align="center">
  <img src="https://github.com/user-attachments/assets/6411f9c7-7d30-48d5-9515-2808b80c6be7" width="500">
</div>

Una vez teniendo en cuenta estos datos tomados directamente del robot se realizó el cálculo de la derivada implicita para la velocidad, dichos datos se pueden observar acontinuación

<div align="center">
  <img src="https://github.com/user-attachments/assets/48b7a9f5-8661-45c9-82a5-b03dcdc354c2" width="500">
</div>

Debido a el ruido que se genera al realizar la derivada implicita, se le realizó un filtrado a los datos con un filtro *XX* y los datos se pueden observar acontinuación. 

*GOLAY 3 21*
<div align="center">
  <img src="https://github.com/user-attachments/assets/1bfaae1a-63f5-4ed7-b617-91b7d0590c5c" width="500">
</div>

*MEDIA MOVIL 20*
<div align="center">
  <img src="https://github.com/user-attachments/assets/2e96bab6-0bb0-49ee-b066-d2d2447f2d28" width="500">
</div>

*EXPONENCIAL 0.1*
<div align="center">
  <img src="https://github.com/user-attachments/assets/4e94e11f-f543-447a-9f44-c17893af876d" width="500">
</div>


Una vez calculada la velocidad angular de cada rueda se realizó el cálculo de la cinematica directa para hallar la velocidad lineal y angular del robot con las formulas descritas en la sección [Fundamentos Teóricos](#fundamentos-teóricos) obteniendo las siguientes gráficas

*Lineal*

*GOLAY 3 21*
<div align="center">
  <img src="https://github.com/user-attachments/assets/48f9e80a-df8a-4b33-95ab-91ddc34bbbb7" width="500">
</div>

*MEDIA MOVIL 20*
<div align="center">
  <img src="https://github.com/user-attachments/assets/dd40fd26-c1d6-4129-9cc0-4f97cde77531" width="500">
</div>

*EXPONENCIAL 0.1*
<div align="center">
  <img src="https://github.com/user-attachments/assets/0345980b-78b8-489f-a8df-9d44cf1f4b71" width="500">
</div>

*Angular*

*GOLAY 3 21*
<div align="center">
  <img src="https://github.com/user-attachments/assets/26c16de6-f5fe-4c34-b145-f66fe3c64d1f" width="500">
</div>

*MEDIA MOVIL 20*
<div align="center">
  <img src="https://github.com/user-attachments/assets/c96a6503-47e7-4b79-a648-b2c3a210c649" width="500">
</div>

*EXPONENCIAL 0.1*
<div align="center">
  <img src="https://github.com/user-attachments/assets/16edb166-3f00-43ae-9a33-a17dcb93dde6" width="500">
</div>

De allí se pudo obtener que la Velocidad lineal promedio es *(0.0874, 0.0874, 0.0867)* $m/s$ y la Velocidad Angular promedio es *(0.0019, 0.0019, 0.0021)* $rad/s$

#### Datos reales con Tracker

Para este procedimiento, se tomó un video en simultaneo a la toma de datos descrita en [Datos Reales con Matlab](#datos-reales-con-matlab) y se empleó el programa [Tracker](https://opensourcephysics.github.io/tracker-website/). En dicho programa se montó el video y se realizaron las correspondientes configuraciones para la toma de datos como se ve en la siguiente imagen

<div align="center">
  <img src="https://github.com/user-attachments/assets/b94dbe5f-0937-47e4-a7c7-9d4ad0ab28a0" width="500">
</div>

Con ello, se obtuvieron 96 datos en 480 fotogramas. Debido a que el programa toma los datos teniendo en cuenta el punto de origen (marco fijo) y se necesitan los del robot (marco movil). 

<div align="center">
  <img src="https://github.com/user-attachments/assets/84d62b29-2ff1-4481-9955-2621c2c74d8f" width="500">
</div>

Para la posición

<div align="center">
  <img src="https://github.com/user-attachments/assets/c29288c2-3e19-4bfe-a994-12878cf57eed" width="400">
</div>

Para la orientación

<div align="center">
  <img src="https://github.com/user-attachments/assets/1242fef2-8993-4854-8e3f-ab7396af209d" width="400">
</div>

hallando

$$R_{M}^{F} = \begin{bmatrix}
cos(\theta) & -sin(\theta) & 0 & x\\
sin(\theta) & cos(\theta) & 0 & y \\
 0 & 0 & 1 & 0 \\
 0 & 0 & 0 & 1 \\
\end{bmatrix}$$

ya con esto, se empleó el script [DatosTracker.m](scripts/DatosTracker.m) y se obtuvo

<div align="center">
  <img src="https://github.com/user-attachments/assets/d0b6102e-c449-4fbd-9819-97e5cf6d83d4" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/33c48224-0d57-4c74-8fdf-e47fc131dcb5" width="500">
</div>

Cabe aclarar que debido a la posición de la cámara y la forma en la que se toma el video (con ojo de pez) provoca ciertos errores puesto que los ejes de tracker no seguiran las lineas guias de las bandosas provocando que hayan ciertas variaciones en los datos recolectados

#### Comparación

### Trayectoria Curva
