from naoqi import ALProxy
from config.vocabulary import CONFIDENCE_THRESHOLD
from motion.gestures import left_arm_on_chest, both_arms_up
from system.rest import rest_robot

def create_callback(robot_ip, port):
    tts = ALProxy("ALTextToSpeech", robot_ip, port)
    motion = ALProxy("ALMotion", robot_ip, port)

    def on_word_recognized(event_name, value, subscriber_identifier):
        if len(value) < 2:
            return

        word = value[0]
        confidence = value[1]

        if confidence < CONFIDENCE_THRESHOLD:
            print("[INFO] Word not recognized confidently enough.")
            return

        print("[INFO] Recognized: {} ({})".format(word, confidence))


        if word == "hello":
            tts.say("Hello")
            left_arm_on_chest(motion)
            rest_robot(robot_ip, port)
        elif word == "goodbye":
            tts.say("Goodbye")
            both_arms_up(motion)
            rest_robot(robot_ip, port)

    return on_word_recognized
