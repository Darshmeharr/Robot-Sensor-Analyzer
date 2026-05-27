from sensor_generator import *
from analyzer import *
from utils import *


distance = generate_distance()

temperature = generate_temperature()

battery = generate_battery()

speed = generate_speed()


avg_speed = average_speed(speed)

obstacles = find_obstacles(distance)

low_battery = battery_status(battery)

high_temp = highest_temperature(
    temperature
)

closest = closest_obstacle(
    distance
)


save_csv(
    distance,
    temperature,
    battery,
    speed
)

print_report(
    avg_speed,
    high_temp,
    closest,
    low_battery,
    obstacles
)


if len(obstacles) > 0:
    print("\n⚠ Robot should slow down")
else:
    print("\n✅ Path is clear")
