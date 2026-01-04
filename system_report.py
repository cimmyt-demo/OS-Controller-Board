# system_report.py
from voltage_control import VoltageController
from sensor_monitor import SensorMonitor
from datetime import datetime

def generate_report(file_path="System_Report.txt"):
    voltage_ctrl = VoltageController()
    sensor_mon = SensorMonitor()

    report = []
    report.append(f"System Report - {datetime.now()}\n")
    report.append(f"Voltage: {voltage_ctrl.read_voltage()}V\n")
    sensors = sensor_mon.read_sensors()
    report.append(f"Temperature: {sensors['temperature']}°C\n")
    report.append(f"Fan Speed: {sensors['fan_speed']} RPM\n")

    with open(file_path, "w") as f:
        f.writelines(report)

    print(f"Report saved to {file_path}")

if __name__ == "__main__":
    generate_report()
