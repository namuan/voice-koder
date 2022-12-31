import logging

import speech_recognition as sr

from koder.common_utils import timing
from koder.ide_actions import take_action


def init_setup():
    logging.debug(f"Speech recognition version ${sr.__version__}")
    logging.debug(f"Microphone list: ${sr.Microphone.list_microphone_names()}")
    return sr.Recognizer()


def start_listening(speech_rec):
    while True:
        with sr.Microphone() as source:
            logging.debug("Waiting for the next command...")
            try:
                speech_rec.pause_threshold = 0.5
                speech_rec.phrase_threshold = 0.3
                speech_rec.adjust_for_ambient_noise(source)
                audio = speech_rec.listen(source)
                whisper_spoken_text = audio_to_text(speech_rec, audio)
                take_action(whisper_spoken_text)
            except Exception as e:
                logging.error(f"Error: {e}")


@timing
def audio_to_text(speech_rec, audio):
    logging.debug("🤖 Starting audio to text conversion")
    return speech_rec.recognize_whisper(audio, model="base", language="en")


def main(args):
    speech_rec = init_setup()
    start_listening(speech_rec)
