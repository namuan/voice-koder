import logging

import pyautogui

from koder.cheat_sheet import SHORTCUTS
from koder.spoken_text import sanitize


def take_action(spoken_text):
    cleanup_text = sanitize(spoken_text)
    logging.debug(f"{spoken_text=} -> {cleanup_text=}")
    action = SHORTCUTS.get(cleanup_text)
    if action:
        action()
    else:
        pyautogui.write(cleanup_text)
