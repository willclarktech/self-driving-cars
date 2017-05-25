#!/usr/bin/env python
import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record():
    last_time = time.time()
    while True:
        # 800x600 windowed mode
        printscreen_pil = ImageGrab.grab(bbox=(0, 40, 800, 640))
        printscreen_numpy = np.array(printscreen_pil)
        print 'loop took {} seconds'.format(time.time() - last_time)
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    screen_record()

