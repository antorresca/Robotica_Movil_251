#!/usr/bin/env python3
import socket
import json
import rospy
from std_msgs.msg import Float32MultiArray

HOST = ''  # Escucha en todas las interfaces
PORT = 9999

def main():
    rospy.init_node('ev3_sensor_server')

    pub_sensors = rospy.Publisher('ev3/sensors', Float32MultiArray, queue_size=10)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()
    print(f"Conexión desde: {addr}")

    buffer = ""
    while not rospy.is_shutdown():
        data = conn.recv(1024).decode()
        buffer += data

        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            try:
                msg = json.loads(line)
                sensor_data = Float32MultiArray()
                # Orden: touch (0 o 1), gyro (angle), ultrasonic (cm)
                sensor_data.data = [
                    float(msg.get("touch", 0)),
                    float(msg.get("gyro", 0.0)),
                    float(msg.get("ultrasonic", 0.0))
                ]
                pub_sensors.publish(sensor_data)
            except Exception as e:
                rospy.logwarn(f"Error procesando mensaje: {e}")

    conn.close()
    s.close()

if __name__ == '__main__':
    main()
