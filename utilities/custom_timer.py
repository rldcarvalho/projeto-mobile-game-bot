import random
import time


class CustomTimer:
    @staticmethod
    def sleep(base_time, variation=0):
        sleep_time = base_time + random.uniform(0, variation)
        time.sleep(sleep_time)