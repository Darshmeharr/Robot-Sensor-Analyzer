import numpy as np


def average_speed(speed):
    return np.mean(speed)


def find_obstacles(distance):
    return distance[distance < 30]


def battery_status(battery):
    return battery[battery < 50]


def highest_temperature(temp):
    return np.max(temp)


def closest_obstacle(distance):
    return np.min(distance)
