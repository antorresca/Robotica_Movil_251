#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray, String

class EV3InstructionNode:
    def __init__(self):
        rospy.init_node('ev3_instruction_node', anonymous=True)
        self.sub = rospy.Subscriber('ev3/sensors', Float32MultiArray, self.sensor_callback)
        self.pub = rospy.Publisher('ev3/instructions', String, queue_size=10)
        rospy.loginfo("Nodo EV3 Instruction iniciado.")

    def sensor_callback(self, msg):
        if len(msg.data) != 3:
            rospy.logwarn("Mensaje de sensores inválido.")
            return

        x, y, z = msg.data
        instruction = "sonido"  # valor por defecto, aunque será reemplazado según las condiciones

        # Máquina de estados (evaluar en orden de prioridad)
        if x > 5:
            instruction = "adelante"
        elif x < 5:
            instruction = "giro 90"
        elif y == 90:
            instruction = "retroceder"
        elif z == 1:
            instruction = "detenerse"
        else:
            instruction = "avanzar"

        rospy.loginfo(f"[Sensores] x={x}, y={y}, z={z} -> [Instrucción] {instruction}")
        self.pub.publish(instruction)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        node = EV3InstructionNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
