from naoqi import ALProxy
import time

ROBOT_IP = "127.0.0.1"  
PORT = 9559

def main():
    # Connect to services
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    # Wake up
    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)
    tts.say("Initializing motion sequence.")

    # Raise left arm
    tts.say("Raising left arm.")
    motion.setStiffnesses("LShoulderPitch", 1.0)
    motion.setAngles("LShoulderPitch", 0.5, 0.2)
    time.sleep(1.5)

    tts.say("Left arm up.")

    # Raise right arm
    motion.setStiffnesses("RShoulderPitch", 1.0)
    motion.setAngles("RShoulderPitch", 0.5, 0.2)
    time.sleep(1.5)

    tts.say("Now both arms are up.")

    # Perform head shake (like "no")
    names = ["HeadYaw"]
    angles = [0.5, -0.5, 0.5, -0.5, 0.0]
    times = [0.5, 1.0, 1.5, 2.0, 2.5]
    motion.angleInterpolation(names, angles, times, True)

    tts.say("I am done with my demo.")

    # Rest
    motion.rest()

if __name__ == "__main__":
    main()
