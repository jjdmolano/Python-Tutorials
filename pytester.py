import pyautogui as pg
import time
import random
from datetime import datetime

pg.FAILSAFE = False
numMin = None
xMax, yMax = pg.size()
moveTypes = [pg.easeInQuad, pg.easeOutQuad, pg.easeInOutQuad, pg.easeInBounce, pg.easeInOutElastic]


def main():
    while True:
        numMin = random.randint(1,5)
        x = 60*numMin
        time.sleep(x)
        xMove = random.randint(1, xMax - 1)
        yMove = random.randint(1, yMax - 1)
        duration = random.randint(1, 3)
        chosenType = random.choice(moveTypes)
        pg.moveTo(xMove, yMove, duration, chosenType)
        print(f'Movement made at {datetime.now().time()} to ({xMove},{yMove}) with {chosenType.__name__}')


if __name__ == '__main__':
    main()
