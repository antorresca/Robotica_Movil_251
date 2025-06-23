#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
from time import sleep, time
from ev3dev2.sensor import INPUT_4, INPUT_3

# --- Sensores y Motores ---
us = UltrasonicSensor(INPUT_4)   # Sensor ultrasónico
ir = InfraredSensor(INPUT_3)     # Sensor infrarrojo
mL = LargeMotor(OUTPUT_B)        # Motor izquierdo
mR = LargeMotor(OUTPUT_C)        # Motor derecho

# --- Parámetros de navegación ---
UMBRAL_ULTRA   = 6.0     # cm: distancia mínima a obstáculo frontal
V_AVANCE       = 30      # % velocidad de avance
T_CORREC       = 0.05    # s: intervalo en búsqueda de borde
MAX_SEARCH_SEC = 2.0     # s: tiempo máximo girando

# --- Estados ---
BOUNDARY_FOLLOW = 1
GOAL_REACHED    = 2

estado = BOUNDARY_FOLLOW

print("Iniciando navegacin")
dist_curr = 99
dist_prev = 100
try:
    while True:
        dist_us = us.distance_centimeters
        dist_ir = ir.proximity
        
        

        if estado == BOUNDARY_FOLLOW:
            print("Entrando a estado: BOUNDARY_FOLLOW")

            # Caso 1: ya no detecta obstáculo frontal → alinear
            while dist_us < 30 :
                mL.on(SpeedPercent(V_AVANCE // 2))
                mR.on(SpeedPercent(-V_AVANCE // 2))
                sleep(T_CORREC)
                dist_us =  us.distance_centimeters
            mR.off(); mL.off()
            # Caso 2: gira hasta que el infrarrojo indique que está alineado (distancia estable)
            while dist_prev - dist_curr > 0:
                print("Girando para quedar paralelo...")
                mL.on(SpeedPercent(V_AVANCE // 3))
                mR.on(SpeedPercent(-V_AVANCE // 3))
                sleep(0.1)
                dist_prev = dist_curr
                dist_curr = ir.proximity
                print("Prev:", dist_prev, " Curr:", dist_curr)

            # Seguir el borde hasta detectar fin del obstáculo o condición de parada
            while dist_curr < 20 and dist_us > 5:
                print("Siguiendo borde. Distancia IR:", dist_curr)

                if dist_curr < 7:
                    mL.on(SpeedPercent(V_AVANCE // 2))
                    mR.on(SpeedPercent(-V_AVANCE // 2))
                    sleep(0.021)
                elif dist_curr > 10:
                    mL.on(SpeedPercent(-V_AVANCE/2 // 2))
                    mR.on(SpeedPercent(V_AVANCE/2 // 2))
                    sleep(0.021)
                else:
                    mL.on(SpeedPercent(V_AVANCE // 2))
                    mR.on(SpeedPercent(V_AVANCE // 2))
                    sleep(0.021)
                dist_us = us.distance_centimeters
                dist_curr = ir.proximity

            while dist_curr > 6 and dist_us > 5 :
                mL.on(SpeedPercent(V_AVANCE/2.1 // 2))
                mR.on(SpeedPercent(V_AVANCE // 2))
                dist_us = us.distance_centimeters
                dist_curr = ir.proximity
                print("girando a izq  " + str(dist_us) + "IR:  " + str(dist_ir))
                sleep(0.01)
            mL.off(); mR.off()

        if estado == GOAL_REACHED:
            mL.off(); mR.off()
            print("Objetivo alcanzado!")
            break

except KeyboardInterrupt:
    pass

# Detener motores al salir
mL.off()
mR.off()
print("Navegacion finalizada.")

