from naoqi import ALProxy

def rest_robot(robot_ip, port):
    motion = ALProxy("ALMotion", robot_ip, port)
    motion.rest()
