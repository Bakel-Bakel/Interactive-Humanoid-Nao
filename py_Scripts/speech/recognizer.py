from naoqi import ALProxy
from config.vocabulary import VOCABULARY, ENABLE_WORD_SPOTTING

def setup_speech_recognition(robot_ip, port, callback_func):
    asr = ALProxy("ALSpeechRecognition", robot_ip, port)
    memory = ALProxy("ALMemory", robot_ip, port)

    asr.setVocabulary(VOCABULARY, ENABLE_WORD_SPOTTING)
    memory.subscribeToEvent("WordRecognized", "TestModule", callback_func)

    return asr
