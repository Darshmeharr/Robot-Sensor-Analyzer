import pandas as pd


def save_csv(distance,
             temperature,
             battery,
             speed):

    data = pd.DataFrame({

        "Distance": distance,
        "Temperature": temperature,
        "Battery": battery,
        "Speed": speed
    })

    data.to_csv(
        "sensor_data.csv",
        index=False
    )

    print("\nData saved successfully")


def print_report(
        avg_speed,
        high_temp,
        closest,
        low_battery,
        obstacles):

    print("\n")
    print("===== ROBOT SENSOR REPORT =====")

    print(
        f"\nAverage Speed: {avg_speed:.2f} km/h"
    )

    print(
        f"Highest Temperature: {high_temp}°C"
    )

    print(
        f"Closest Obstacle: {closest} cm"
    )

    print(
        f"Low Battery Alerts: {len(low_battery)}"
    )

    print(
        f"Obstacle Alerts: {len(obstacles)}"
    )

    print("\n==============================")
