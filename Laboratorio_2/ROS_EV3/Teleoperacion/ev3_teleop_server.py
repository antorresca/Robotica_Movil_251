#!/usr/bin/env python3
import socket
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
from time import sleep

LEFT = LargeMotor(OUTPUT_B)
RIGHT = LargeMotor(OUTPUT_C)

HOST = ''  # Escucha en todas las interfaces
PORT = 9998

def ejecutar(comando):
    if comando == 'forward':
        LEFT.on(SpeedPercent(40))
        RIGHT.on(SpeedPercent(40))
    elif comando == 'backward':
        LEFT.on(SpeedPercent(-40))
        RIGHT.on(SpeedPercent(-40))
    elif comando == 'left':
        LEFT.on(SpeedPercent(-30))
        RIGHT.on(SpeedPercent(30))
    elif comando == 'right':
        LEFT.on(SpeedPercent(30))
        RIGHT.on(SpeedPercent(-30))
    elif comando == 'stop':
        LEFT.off()
        RIGHT.off()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    print("Esperando conexión para teleoperación...")
    conn, addr = s.accept()
    print("Teleoperación conectada desde:", addr)

    buffer = ""
    while True:
        data = conn.recv(1024).decode()
        buffer += data

        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            ejecutar(line.strip())

    conn.close()
    s.close()

if __name__ == '__main__':
    main()
