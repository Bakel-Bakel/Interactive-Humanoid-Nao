from speech.recognizer import setup_speech_recognition
from utils.callbacks import create_callback
from naoqi import ALProxy

ROBOT_IP = "127.0.0.1"
PORT = 9559


def main():
    print("[INFO] Starting NAO Talking behavior...")
    
    callback = create_callback(ROBOT_IP, PORT)
    
    #asr = setup_speech_recognition(ROBOT_IP, PORT, callback)
    print("[INFO] Speech recognition started. Say your command!")

    #Inject test: Simulate the word "hello" being recognized
    memory = ALProxy("ALMemory", ROBOT_IP, PORT)
    memory.raiseEvent("WordRecognized", ["hello", 0.9])
    print("[INFO] Greet recognized..")


    tts = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    motion = ALProxy("ALMotion", ROBOT_IP, PORT)

    tts.say("Simulating hello recognition..")
    
    # Manually simulate the 'hello' behavior
    from motion.gestures import left_arm_on_chest
    from system.rest import rest_robot

    tts.say("Hello, My name is Nao")
    left_arm_on_chest(motion)
    rest_robot(ROBOT_IP, PORT)


if __name__ == "__main__":
    main()
