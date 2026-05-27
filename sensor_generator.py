import numpy as np
from config import *

def generate_distance():
    return np.random.randint(
        DISTANCE_MIN,
        DISTANCE_MAX,
        NUM_READINGS
    )


def generate_temperature():
    return np.random.randint(
        TEMP_MIN,
        TEMP_MAX,
        NUM_READINGS
    )


def generate_battery():
    return np.random.randint(
        BATTERY_MIN,
        BATTERY_MAX,
        NUM_READINGS
    )


def generate_speed():
    return np.random.randint(
        SPEED_MIN,
        SPEED_MAX,
        NUM_READINGS
    )
