# 👾Tarea: Cinemática Robot Diferencial

## 📖Fundamentos Teóricos 

Para el cálculo teórico se siguió la presentación *Robots con ruedas 2* disponible en el Moodle del curso, de allí se extrajeron las siguientes ecuaciones para cinemática directa de robots con ruedas:

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

En las que se relaciona la velocidad angular de las ruedas (en $rad/s$) con la velocidad lineal (en $m/s$) y angular (en $rad/s$) del robot. Por otro lado, si se necesita la velocidad con respecto al marco fijo se puede obtener mediante

$$ \dot{X_F} =  
R_{M}^{F} \cdot \dot{X}_{M}  $$

## 🎢Procedimiento

### Trayectoria Recta

Tomando $r = 0.028 \text{m}$ y $l = 0.059 \text{m}$ y que $\dot{\phi}_n = 2.85 \text{rad/s}$ considerando la velocidad máxima de los motores Lego, y que se usó el 20% de este velocidad. A partir de dichos valores, se realizaron los calculos de la velocidad lineal y angular del robot

$$ v = 0.0798 \text{m/s} $$
$$ \omega = 0 \text{rad/s} $$

#### Datos Reales con MATLAB

Para la trayectoria recta se le asignó la velocidad del 20% a los motores derecho e izquierdo; y con el programa descrito en el archivo [TomaDeDatos.mlx](Scripts/TomaDeDatos.mlx) se obtuvo la siguiente gráfica que describe la posición angular de cada una de las ruedas mientras el robot está en movimiento

<div align="center">
  <img src="https://github.com/user-attachments/assets/6411f9c7-7d30-48d5-9515-2808b80c6be7" width="500">
</div>

Una vez teniendo en cuenta estos datos tomados directamente del robot se realizó el cálculo de la derivada implícita para la velocidad, dichos datos se pueden observar a continuación

<div align="center">
  <img src="https://github.com/user-attachments/assets/48b7a9f5-8661-45c9-82a5-b03dcdc354c2" width="500">
</div>

Debido a el ruido que se genera al realizar la derivada implícita, se le realizó un filtrado a los datos con un filtro de suavizado exponencial con un coeficiente de 0.1 y los datos se pueden observar a continuación. 

<div align="center">
  <img src="https://github.com/user-attachments/assets/4e94e11f-f543-447a-9f44-c17893af876d" width="500">
</div>

Una vez calculada la velocidad angular de cada rueda se realizó el cálculo de la cinematica directa para hallar la velocidad lineal y angular del robot con las formulas descritas en la sección [Fundamentos Teóricos](#fundamentos-teóricos) obteniendo las siguientes gráficas

<div align="center">
  <img src="https://github.com/user-attachments/assets/0345980b-78b8-489f-a8df-9d44cf1f4b71" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/49a9bfd7-eb54-4839-b5e7-7774959f48a7" width="500">
</div>

De allí se pudo obtener que la Velocidad lineal promedio es 0.0867 $m/s$ y la Velocidad Angular promedio es 0.0021 $rad/s$

#### Datos reales con Tracker

Para este procedimiento, se tomó un video en simultaneo a la toma de datos descrita en [Datos Reales con MATLAB](#datos-reales-con-MATLAB) y se empleó el programa [Tracker](https://opensourcephysics.github.io/tracker-website/). En dicho programa se montó el video y se realizaron las correspondientes configuraciones para la toma de datos como se ve en la siguiente imagen

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

ya con esto, se empleó el script [TomaDeDatos](Scripts/TomaDeDatos.mlx) y se obtuvo

<div align="center">
  <img src="https://github.com/user-attachments/assets/74be3c3e-588c-4820-81ba-00884b592c84" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/65dfb822-0f2d-42a4-8c8c-7f78a1d5a91b" width="500">
</div>

Cabe aclarar que debido a la posición de la cámara y la forma en la que se toma el video (con ojo de pez) provoca ciertos errores puesto que los ejes de tracker no seguiran las lineas guias de las baldosas provocando que hayan ciertas variaciones en los datos recolectados

#### Comparación

Una vez hecho los diferentes procedimientos, se procedió a comparar los resultados teóricos, los datos con el encoder y MATLAB y los datos tomados en Tracker. Para ello se realizaron las siguientes gráficas

<div align="center">
  <img src="https://github.com/user-attachments/assets/1d06ec37-4dad-4135-a790-0af8676bb2fb" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/15dc35c7-1287-48ac-ac92-9b8049a57901" width="500">
</div>

Se calcularon los promedios en cada uno y se calculó el error relativo con respecto al teórico

| Procedimiento | Promedio V.Lineal ($m/s$)| Error (%) | Promedio V.Angular ($rad/s$)|
|---------------|--------------------------|-----------|-----------------------------|
| Teórico       | 0.0798                   | -         | 0                           |
| MATLAB        | 0.0867                   | 8.65      | 0.0021                      |
| Tracker       | 0.0837                   | 4.89      | 0.1610                      |

**Nota:** Por ser el teórico $0 \text{rad/s}$ no se puede hallar el error relativo

### Trayectoria Curva

Tomando $r = 0.028 \text{m}$ y $l = 0.059 \text{m}$ y que $\dot{\phi}_1 = 2.85 \text{rad/s}$ y $\dot{\phi}_2 = 2.14 \text{rad/s}$ considerando la velocidad máxima de los motores Lego, que el motor izquierdo ($\dot{\phi}_1$) usó un 20% de la velocidad máxima y que el motor derecho ($\dot{\phi}_2$) usó un 15% de la velocidad máxima. A partir de dichos valores, se realizaron los cálculos de la velocidad lineal y angular del robot

$$ v = 0.0698 \text{m/s} $$
$$ \omega = -0.1690 \text{rad/s} $$

#### Datos con MATLAB

Para la trayectoria recta se le asignó la velocidad del 20% al motor izquierdo y 15% al derecho; y con el programa descrito en el archivo [TomaDeDatos.mlx](Scripts/TomaDeDatos.mlx) se obtuvo la siguiente gráfica que describe la posición angular de cada una de las ruedas mientras el robot está en movimiento

<div align="center">
  <img src="https://github.com/user-attachments/assets/7d74e99b-f784-4f0d-aa44-f06bf39d3cc1" width="500">
</div>

Una vez teniendo en cuenta estos datos tomados directamente del robot se realizó el cálculo de la derivada implícita para la velocidad, dichos datos se pueden observar a continuación

<div align="center">
  <img src="https://github.com/user-attachments/assets/ac887c21-667b-48aa-a7d7-a299f796fb10" width="500">
</div>

Como sucedió en la [Trayectoria Recta](#trayectoria-recta) se tuvo que filtrar los datos con un filtro de suavizado exponencial con coeficiente de 0.1 obteniendo

<div align="center">
  <img src="https://github.com/user-attachments/assets/8e0336c6-de73-4cc8-a941-c682e9503426" width="500">
</div>

Ya con estos datos, se realizó el cálculo de la velocidad lineal y angular del robot

<div align="center">
  <img src="https://github.com/user-attachments/assets/dc7ef7dd-babc-4b49-aa4f-1a5c5c086b00" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/73082409-d8e2-4349-8233-cf08d171bfc2" width="500">
</div>

Dando como promedio de la velocidad lineal $0.0782\text{m/s}$ y de la velocidad angular $-0.1311\text{rad/s}$

#### Datos con Tracker

Para este procedimiento, se siguió el mismo procedimiento descrito en [Datos reales con Tracker](#datos-reales-con-tracker) como se ve en la siguiente imagen

<div align="center">
  <img src="https://github.com/user-attachments/assets/e663ff38-d2a3-46dc-b82c-2cc7185224c4" width="500">
</div>

**Nota:** La imagen se ve de esa manera puesto que se le puso un filtro al video para la perspectiva y así lograr que los ejes coincidieran con las lineas de ortogonales de las baldosas y mejorar la precisión de los datos.

Posteriormente, se empleó la misma matriz de transformación homogenea desarrollada en [Datos reales con Tracker](#datos-reales-con-tracker) obteniendo

<div align="center">
  <img src="https://github.com/user-attachments/assets/c4317ebe-63ed-492e-90e6-071b00175385" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/a4614d59-e172-4772-a247-1a380eba91f4" width="500">
</div>

#### Comparación de datos

Una vez hecho los diferentes procedimientos, se procedió a comparar los resultados teóricos, los datos con el encoder y MATLAB y los datos tomados en Tracker. Para ello se realizaron las siguientes gráficas

<div align="center">
  <img src="https://github.com/user-attachments/assets/ce0828a2-ef35-4223-8ef0-33fc44c1cf88" width="500">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/afb1d618-d697-4e20-a358-aa508d918359" width="500">
</div>

Se calcularon los promedios en cada uno y se calculó el error relativo con respecto al teórico

| Procedimiento | Promedio V.Lineal ($m/s$)| Error (%) | Promedio V.Angular ($rad/s$)| Error (%)|
|---------------|--------------------------|-----------|-----------------------------|----------|
| Teórico       | 0.0698                   | -         |-0.1690                      | -        |
| MATLAB        | 0.0782                   | 12.05     |-0.1311                      | 22.41    |
| Tracker       | 0.0556                   | 20.37     | 0.1961                      | 216.07   |

## Conclusiones

* Los sensores tienen cierta incertidumbre que generan desviaciones en los datos registrados, por lo cual, es necesario realizar un correcto postprocesado de los mismos.
* Las herramientas como *MATLAB* y *Tracker* permiten comprender y visualizar el movimiento de los robots moviles durante el tiempo.
* A pesar del postprocesado que se le realice a los datos que se obtengan en pruebas experimentales, es podible que aun asi halla errores relativos altos en los resultados esto debido a que si se filtran demasiado los datos se pierde información y si no se filtran correctamente, el ruido de medición genera mayores errores.

## Notas adicionales

En la carpeta [Scripts](Scripts) estan los diferentes archivos *.mat* de los datos obtenidos y empleados. Y en la carpeta [Tracker](Tracker) estan los archivos *.trk* empleados
