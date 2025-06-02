#!/usr/bin/env python3

import socket
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor, TouchSensor
from ev3dev2.sound import Sound
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3

# Configuración
SERVER_IP = '192.168.0.10'   # Cambia esto por la IP del PC con ROS
PORT_SEND = 9999             # Enviar datos de sensores
PORT_RECEIVE = 9998          # Recibir instrucciones

# Inicializar sensores y actuadores
us = UltrasonicSensor(INPUT_1)
gyro = GyroSensor(INPUT_2)
touch = TouchSensor(INPUT_3)

motor_a = LargeMotor(OUTPUT_A)
motor_d = LargeMotor(OUTPUT_D)
sound = Sound()

# Función para enviar datos de sensores
def send_sensor_data(sock):
    distance = us.distance_centimeters
    angle = gyro.angle
    touch_state = 1 if touch.is_pressed else 0
    msg = f"{distance:.1f},{angle},{touch_state}\n"
    sock.sendall(msg.encode())

# Función para procesar instrucciones recibidas
def handle_instruction(msg):
    msg = msg.strip().lower()
    print(f"Recibido: {msg}")

    if "sonido" in msg:
        sound.speak("Ahi te voy san Pedro")

    elif "adelante" in msg:
        motor_a.on(SpeedPercent(25))
        motor_d.on(SpeedPercent(25))

    elif "detenerse" in msg:
        motor_a.off()
        motor_d.off()

    elif "girar" in msg:
        gyro.reset()
        motor_a.on(SpeedPercent(25))
        motor_d.on(SpeedPercent(-25))
        while abs(gyro.angle) < 88:
            time.sleep(0.05)
        motor_a.off()
        motor_d.off()

    elif "retroceder" in msg:
        motor_a.on(SpeedPercent(-25))
        motor_d.on(SpeedPercent(-25))

    elif "avanzar" in msg:
        motor_a.on(SpeedPercent(25))
        motor_d.on(SpeedPercent(25))
        time.sleep(2)
        motor_a.off()
        motor_d.off()

# Crear sockets
sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar sockets
print("Conectando con el servidor para envío...")
sock_send.connect((SERVER_IP, PORT_SEND))
print("Conectando con el servidor para recepción...")
sock_recv.connect((SERVER_IP, PORT_RECEIVE))

sock_recv.settimeout(0.5)  # No bloquea eternamente al esperar instrucciones

try:
    while True:
        # Enviar datos de sensores
        send_sensor_data(sock_send)

        # Intentar recibir una instrucción
        try:
            data = sock_recv.recv(1024).decode()
            if data:
                handle_instruction(data)
        except socket.timeout:
            pass  # No hay nueva instrucción aún

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Finalizando programa...")
finally:
    motor_a.off()
    motor_d.off()
    sock_send.close()
    sock_recv.close()
