import pyautogui as pg
pg.FAILSAFE = False


def main():
    while True:
        pg.click(interval=5, button='left')


if __name__ == '__main__':
    main()
