#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, InfraredSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
from time import sleep, time
from ev3dev2.sensor import INPUT_4, INPUT_2,INPUT_3

# --- Sensores y Motores ---
cs = ColorSensor(INPUT_2)        # sensor de color en el puerto por defecto
us = UltrasonicSensor(INPUT_4)   # sensor ultrasonico en el puerto por defecto
ir = InfraredSensor(INPUT_3)     # sensor infrarrojo en el puerto por defecto
mL = LargeMotor(OUTPUT_B) # motor izquierdo en el puerto B
mR = LargeMotor(OUTPUT_C) # motor derecho en el puerto C

# --- Parametros de navegacion ---
UMBRAL_ULTRA   = 6.0    # cm: distancia minima a obstaculo frontal
UMBRAL_IR      = 10.0    # mm: distancia minima para pegarse al obstaculo
V_AVANCE       = 30      # % velocidad de avance
T_CORREC       = 0.05    # s: intervalo en busqueda de linea
MAX_SEARCH_SEC = 2.0     # s: tiempo maximo girando a la izquierda

# --- Estados de la maquina de estados ---
FOLLOW_LINE     = 0    # seguir la linea negra
BOUNDARY_FOLLOW = 1    # bordear el obstaculo

estado = FOLLOW_LINE

print("Iniciando navegacion desde P1 hacia P2...")


try:
    while True:
        # Lectura de sensores
        color   = cs.color                  # 1 = negro
        dist_us = us.distance_centimeters   # en cm
        dist_ir = ir.proximity              # valor de proximidad IR

        # --- PRIORIDAD MAXIMA: si ve linea negra, va a FOLLOW_LINE ---
        if color == ColorSensor.COLOR_BLACK:
            estado = FOLLOW_LINE
        dist_prev = 100
        dist_curr= 99
        # --- Logica por estado ---
        if estado == FOLLOW_LINE:
            # 1) Si obstaculo frontal, cambiar a BOUNDARY_FOLLOW
            print("color")
            print (cs.color)
            if dist_us < UMBRAL_ULTRA:
                estado = BOUNDARY_FOLLOW

            # 2) Si pierde la linea en tramo libre, buscarla
            elif (color != ColorSensor.COLOR_BLACK
                  and dist_us >= UMBRAL_ULTRA):
                # Intento girar a la izquierda hasta MAX_SEARCH_SEC
                start = time()
                print("Control de Linea")
                while cs.color != ColorSensor.COLOR_BLACK and time() - start < MAX_SEARCH_SEC:
                    mL.on(SpeedPercent(V_AVANCE // 2))  # izquierda marcha atras
                    mR.on(SpeedPercent(-V_AVANCE // 2))   # derecha adelante
                    sleep(T_CORREC)
                mL.off(); mR.off()
                # Si aun no encontro, gira a la derecha hasta hallar
                if cs.color != ColorSensor.COLOR_BLACK:
                    while cs.color != ColorSensor.COLOR_BLACK:
                        mL.on(SpeedPercent(-V_AVANCE // 2))
                        mR.on(SpeedPercent(V_AVANCE // 2))
                        sleep(T_CORREC)
                    mL.off(); mR.off()
                # Vuelve a FOLLOW_LINE
                estado = FOLLOW_LINE

            # 3) Si sobre la linea y sin obstaculos, avanzar recto
            else:
                mL.on(SpeedPercent(V_AVANCE))
                mR.on(SpeedPercent(V_AVANCE))
            
            if cs.color == 5:
                 estado = 2

        if estado == BOUNDARY_FOLLOW:
            print("entro al estado boundary_follow")
            # Caso 1: ya no detecta obstáculo frontal -> girar a la derecha suavemente
            while dist_us < 30:
                print("Obstaculo despejado. Alineando...")
                mL.on(SpeedPercent(V_AVANCE/2 // 2))
                mR.on(SpeedPercent(-V_AVANCE/2 // 2))
                sleep(T_CORREC)
                dist_us = us.distance_centimeters

            mL.off(); mR.off()

            # Caso 2: sigue el borde hasta que empiece a alejarse (ir.proximity aumente)

            while dist_prev-dist_curr > 0:
                    print("Girando hasta quedar paralelo...")
                    # girar a la derecha mientras se alinea
                    mL.on(SpeedPercent(V_AVANCE // 3))
                    mR.on(SpeedPercent(-V_AVANCE // 3))
                    sleep(0.1)
                    dist_prev = dist_curr
                    dist_curr = ir.proximity
                    print(dist_prev, + dist_curr)
            #mL.off(); mR.off()
            #sleep(0.05)
            #color = cs.color
            print( "Prev" + str(dist_prev) + "\n" + "Curr: " + str( dist_curr ))
            while ( dist_curr < 50 and cs.color != ColorSensor.COLOR_BLACK):
                   print("Disrancia IR = "+ str(dist_curr) + "color:  " + str( color))
                   if dist_curr < 4:
                        mL.on(SpeedPercent(V_AVANCE/3 // 2))
                        mR.on(SpeedPercent(-V_AVANCE/3 // 2))
                        sleep(0.021  ) 
                   if dist_curr > 10:
                        mL.on(SpeedPercent(-V_AVANCE/3 // 2))
                        mR.on(SpeedPercent(V_AVANCE/3 // 2 ))
                        sleep(0.021)
#                   color = ColorSensor.COLOR_BLACK
                   dist_curr= ir.proximity
                   mL.on(SpeedPercent(V_AVANCE //2))
                   mR.on(SpeedPercent(V_AVANCE //2))
                   sleep(0.021)
            mL.off(); mR.off()
            #sleep(5)


            # Volver a buscar la línea
            estado = FOLLOW_LINE

        if estado == 2:
            mL.off(); mR.off
            print ( "Objetivo Alcalnzado!!!")
            break

except KeyboardInterrupt:
    pass

# Parar ambos motores al final
mL.off()
mR.off()
print("Navegacion finalizada.")

#ESTE ES EL CODIGO QUE QUIERO QUE TENGAS EN CUENTA
