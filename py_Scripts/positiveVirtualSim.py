from naoqi import ALProxy
from utils.callbacks import create_callback

ROBOT_IP = "127.0.0.1"
PORT = 9559

def main():
    print("[INFO] Starting NAO Talking behavior...")

    # Only set up callback, no ALSpeechRecognition
    callback = create_callback(ROBOT_IP, PORT)

    # Simulate word being recognized
    memory = ALProxy("ALMemory", ROBOT_IP, PORT)
    memory.raiseEvent("WordRecognized", ["hello", 0.95])  # or "goodbye"

if __name__ == "__main__":
    main()
    memory = ALProxy("ALMemory", ROBOT_IP, PORT)
    memory.raiseEvent("WordRecognized", ["hello", 0.95])
