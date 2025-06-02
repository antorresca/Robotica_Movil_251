#!/usr/bin/env python3

import rospy
import socket
import threading
from std_msgs.msg import Float32MultiArray, String

class EV3SocketBridge:
    def __init__(self, host='0.0.0.0', recv_port=9999, send_port=9998, ev3_ip='192.168.0.123'):
        rospy.init_node('ev3_socket_bridge', anonymous=True)

        self.recv_port = recv_port
        self.send_port = send_port
        self.ev3_ip = ev3_ip

        self.sensor_pub = rospy.Publisher('ev3/sensors', Float32MultiArray, queue_size=10)
        rospy.Subscriber('ev3/instructions', String, self.instruction_callback)

        # Para enviar instrucciones
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.sender_socket.connect((self.ev3_ip, self.send_port))
            rospy.loginfo(f"Conectado a EV3 en {self.ev3_ip}:{self.send_port} para enviar instrucciones.")
        except Exception as e:
            rospy.logerr(f"No se pudo conectar al EV3 para envío: {e}")

        # Iniciar hilo para recibir datos
        self.receiver_thread = threading.Thread(target=self.listen_to_ev3)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()

    def listen_to_ev3(self):
        """Escucha al EV3 (cliente) por TCP y publica los datos recibidos"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', self.recv_port))
        server_socket.listen(1)
        rospy.loginfo(f"Esperando conexión del EV3 en el puerto {self.recv_port}...")

        conn, addr = server_socket.accept()
        rospy.loginfo(f"Conexión establecida desde {addr}")

        while not rospy.is_shutdown():
            try:
                data = conn.recv(1024).decode().strip()  # Ej: "1.0,90.0,0.0"
                if data:
                    parts = [float(x) for x in data.split(',')]
                    if len(parts) == 3:
                        msg = Float32MultiArray(data=parts)
                        self.sensor_pub.publish(msg)
                        rospy.loginfo(f"Datos recibidos del EV3: {parts}")
                    else:
                        rospy.logwarn("Mensaje con formato incorrecto.")
            except Exception as e:
                rospy.logerr(f"Error en recepción de datos: {e}")
                break

    def instruction_callback(self, msg):
        """Envía las instrucciones al EV3"""
        try:
            self.sender_socket.sendall((msg.data + '\n').encode())
            rospy.loginfo(f"Instrucción enviada al EV3: {msg.data}")
        except Exception as e:
            rospy.logerr(f"No se pudo enviar instrucción al EV3: {e}")

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        bridge = EV3SocketBridge()
        bridge.run()
    except rospy.ROSInterruptException:
        pass
