#!/usr/bin/env python

import rospy
from kobuki_msgs.msg import CliffEvent, Sound

def cliff_callback(msg):
    # Verifica el tipo de sensor que detectó el evento
    rospy.loginfo(f"Cliff event detected from sensor: {msg.sensor}")
    
    
    # Publica un sonido en el tópico /mobile_base/commands/sound
    sound_msg = Sound()
    sound_msg.value = 5
    sound_pub.publish(sound_msg)
    rospy.loginfo("Published sound command with value: 5")
    
if __name__ == '__main__':
    rospy.init_node('clifh', anonymous=True)

    # Publicador para el tópico /mobile_base/commands/sound
    rospy.loginfo("Cliff event handler node started.")
    sound_pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)

    

    # Suscribirse al tópico /mobile_base/events/cliff
    rospy.Subscriber('/mobile_base/events/cliff', CliffEvent, cliff_callback)
    rospy.spin()
    # Inicializa el publicador para el tópico /mobile_base/commands/sound


    
    
