import pyautogui

pyautogui.FAILSAFE = True

SHORTCUTS = {
    "find file": lambda: pyautogui.hotkey("command", "shift", "n"),
    "enter": lambda: pyautogui.press("enter"),
    "undo": lambda: pyautogui.hotkey("command", "z"),
    "close": lambda: pyautogui.press("escape"),
    "delete": lambda: pyautogui.press("backspace"),
    "select all": lambda: pyautogui.hotkey("command", "a"),
    "go to": lambda: pyautogui.hotkey("command", "e"),
    "help": lambda: pyautogui.hotkey("command", "shift", "a"),
    "left": lambda: pyautogui.press("left"),
    "right": lambda: pyautogui.press("right"),
    "up": lambda: pyautogui.press("up"),
    "down": lambda: pyautogui.press("down"),
}
