from naoqi import ALProxy
import time

def left_arm_on_chest(motion):
    motion.setStiffnesses("LShoulderPitch", 1.0)
    motion.setAngles("LShoulderPitch", 0.5, 0.2)
    time.sleep(2)

def both_arms_up(motion):
    motion.setStiffnesses(["LShoulderPitch", "RShoulderPitch"], 1.0)
    motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [0.5, 0.5], 0.2)
    time.sleep(2)