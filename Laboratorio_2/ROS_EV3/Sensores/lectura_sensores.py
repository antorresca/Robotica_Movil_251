#!/usr/bin/env python3
import socket
import json
from ev3dev2.sensor.lego import TouchSensor, GyroSensor, UltrasonicSensor
from time import sleep

SERVER_IP = '192.168.1.226'  # Cambia por la IP del PC
SERVER_PORT = 9999

ts = TouchSensor()
gyro = GyroSensor()
us = UltrasonicSensor()

def main():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, SERVER_PORT))
            break
        except:
            print("Reintentando conexión...")
            sleep(1)

    print("Conectado al servidor.")

    while True:
        try:
            data = {
                "touch": ts.is_pressed,
                "gyro": gyro.angle,
                "ultrasonic": us.distance_centimeters
            }
            s.sendall((json.dumps(data) + '\n').encode())
            sleep(0.1)
        except Exception as e:
            print(f"Error: {e}")
            break

    s.close()

if __name__ == '__main__':
    main()
