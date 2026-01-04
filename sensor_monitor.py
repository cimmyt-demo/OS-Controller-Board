# sensor_monitor.py
import random
import time

class SensorMonitor:
    def __init__(self):
        self.sensors = {
            "temperature": 25.0,
            "fan_speed": 1000
        }

    def read_sensors(self):
        # Simulate sensor readings
        self.sensors["temperature"] = round(random.uniform(20, 80), 1)
        self.sensors["fan_speed"] = random.randint(800, 3000)
        return self.sensors

    def log_sensors(self):
        data = self.read_sensors()
        print(f"Temperature: {data['temperature']}°C, Fan Speed: {data['fan_speed']} RPM")

if __name__ == "__main__":
    monitor = SensorMonitor()
    for _ in range(5):
        monitor.log_sensors()
        time.sleep(1)
