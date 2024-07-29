from time import sleep
from pyautogui import keyDown, keyUp


def main() -> None:
    while True:
        try:
            keyDown('z')
            keyUp('z')
            keyDown('ctrl')
            sleep(8.4)
        finally:
            keyUp('ctrl')


if __name__ == '__main__':
    main()