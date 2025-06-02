#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()

SERVER_IP = '192.168.1.226'
SERVER_PORT = 9999

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Intentar conectar
    while True:
        try:
            s.connect((SERVER_IP, SERVER_PORT))
            print("Conectado al servidor")
            break
        except:
            print("Esperando conexion...")
            time.sleep(1)

    while True:
        estado = '1' if ts.is_pressed else '0'
        s.send(estado.encode())
        time.sleep(0.1)

if __name__ == '__main__':
    main()
