import pyautogui as pg
import keyboard as kb
pg.FAILSAFE = False

status = False

def main():
    while True:
        while status is True:
            pg.press('`', presses = 3, interval = 0.7)
            pg.press('left', interval = 0.1)
            pg.press('`', interval = 0.7)

        def start():
            global status
            status = True

        def stop():
            global status
            status = False

        kb.add_hotkey('1', start)
        kb.add_hotkey('2', stop)

if __name__ == '__main__':
    main()
