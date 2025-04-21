from naoqi import ALProxy
import time


ROBOT_IP = "127.0.0.1"
PORT = 9559

def main():
    # Connect to services
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion = ALProxy("ALMotion", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    # Wake up robot (virtual robot must "wake up" too)
    motion.wakeUp()

    # Go to initial standing posture
    posture.goToPosture("StandInit", 0.5)

    # Speak
    tts.say("Hello, I am now raising my left arm.")

    # Move left arm (e.g., LShoulderPitch up)
    joint_name = "LShoulderPitch"
    target_angle = 0.5  # radians
    speed = 0.2
    motion.setStiffnesses(joint_name, 1.0)
    motion.setAngles(joint_name, target_angle, speed)

    time.sleep(2)

    # Return to rest
    motion.rest()

if __name__ == "__main__":
    main()
