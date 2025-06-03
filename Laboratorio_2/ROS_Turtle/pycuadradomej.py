#!/usr/bin/env python3

import rospy
from turtlesim.srv import Spawn, Kill, TeleportAbsolute

# Secuencia de posiciones por las que pasarán las tortugas
WAYPOINTS = [
    [(5, 10, 0), (3, 5, 0)],
    [(10, 10, 0), (5, 1, 0)],
    [(10, 5, 0), (5, 5, 0)],
    [(5, 5, 0), (5, 5, 0)],
]

def kill_turtle(name):
    rospy.wait_for_service('/kill')
    try:
        kill_service = rospy.ServiceProxy('/kill', Kill)
        kill_service(name)
        rospy.loginfo(f"Tortuga {name} eliminada.")
    except rospy.ServiceException:
        rospy.logwarn(f"Tortuga {name} no existe, continuará la ejecución.")

def spawn_turtle(name, x, y, theta):
    rospy.wait_for_service('/spawn')
    try:
        spawn_service = rospy.ServiceProxy('/spawn', Spawn)
        spawn_service(x, y, theta, name)
        rospy.loginfo(f"Tortuga {name} creada en ({x}, {y}, {theta}).")
    except rospy.ServiceException as e:
        rospy.logerr(f"Error al crear {name}: {e}")

def teleport_turtle(name, x, y, theta):
    rospy.wait_for_service(f'/{name}/teleport_absolute')
    try:
        teleport_service = rospy.ServiceProxy(f'/{name}/teleport_absolute', TeleportAbsolute)
        teleport_service(x, y, theta)
        rospy.loginfo(f"Tortuga {name} movida a ({x}, {y}, {theta}).")
    except rospy.ServiceException as e:
        rospy.logerr(f"Error al mover {name}: {e}")

if __name__ == '__main__':
    rospy.init_node('manage_turtles')

    # Eliminar tortugas previas si existen
    kill_turtle("turtle1")
    kill_turtle("turtle2")

    # Crear nuevas tortugas
    spawn_turtle("turtle1", 5, 5, 0.0)
    spawn_turtle("turtle2", 5, 5, 0.0)

    rospy.loginfo("Las tortugas seguirán la trayectoria definida.")

    # Recorrer la trayectoria una sola vez
    for step in WAYPOINTS:
        teleport_turtle("turtle1", *step[0])
        teleport_turtle("turtle2", *step[1])
        rospy.sleep(1)  # Espera un segundo entre cada teletransportación

    rospy.loginfo("trayectoria tortuguil hecha")


