#!/usr/bin/env python3
import socket
import rospy
import sys
import termios
import tty

SERVER_IP = '192.168.1.123'  # IP del EV3
SERVER_PORT = 9998           # Puerto diferente al de sensores

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def main():
    rospy.init_node('ev3_teleop_client')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    print("Conectado al EV3. Usa WASD para mover. Q para salir.")

    while not rospy.is_shutdown():
        key = get_key()
        if key == 'w':
            s.sendall(b'forward\n')
        elif key == 's':
            s.sendall(b'backward\n')
        elif key == 'a':
            s.sendall(b'left\n')
        elif key == 'd':
            s.sendall(b'right\n')
        elif key == 'x':
            s.sendall(b'stop\n')
        elif key == 'q':
            s.sendall(b'stop\n')
            break

    s.close()

if __name__ == '__main__':
    main()
