# voltage_control.py
import random

class VoltageController:
    def __init__(self, min_voltage=3.3, max_voltage=12.0):
        self.min_voltage = min_voltage
        self.max_voltage = max_voltage
        self.current_voltage = min_voltage

    def read_voltage(self):
        # Simulate reading voltage from hardware sensor
        self.current_voltage = round(random.uniform(self.min_voltage, self.max_voltage), 2)
        return self.current_voltage

    def set_voltage(self, voltage):
        if self.min_voltage <= voltage <= self.max_voltage:
            self.current_voltage = voltage
            print(f"Voltage set to {self.current_voltage}V")
        else:
            print(f"Error: Voltage must be between {self.min_voltage}V and {self.max_voltage}V")

if __name__ == "__main__":
    controller = VoltageController()
    print("Current voltage:", controller.read_voltage())
    controller.set_voltage(5.0)
