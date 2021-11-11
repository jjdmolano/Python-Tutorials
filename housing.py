import pyautogui as pg
import keyboard as kb
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
            pg.press('`', presses=3, interval=0.7)
            pg.press('left', interval=0.1)
            pg.press('`', interval=0.7)

            if status[0] is False:
                break


if __name__ == '__main__':
    main()
