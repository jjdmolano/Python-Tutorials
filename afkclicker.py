import pyautogui as pg
import keyboard as kb
import random as r
pg.FAILSAFE = False

status = [False]


def start():
    status[0] = True


def stop():
    status[0] = False


kb.add_hotkey('1', start)
kb.add_hotkey('2', stop)


def main():
    while True:
        while status[0] is True:
            random = r.randint(0,9)

            if random in range(0,4):
                pg.press('left', interval=1)
            if random in range(5,9):
                pg.press('right', interval=1)

            if status[0] is False:
                break


if __name__ == '__main__':
    main()

