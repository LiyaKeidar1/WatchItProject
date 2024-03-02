import random


class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type

    def read_data(self):
        # Simulate reading data from a real sensor
        return random.uniform(-10, 120)


# Subclasses for specific sensor types
class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__("Temperature")


class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__("Humidity")


class PressureSensor(Sensor):
    def __init__(self):
        super().__init__("Pressure")

    # override function specific for pressure sensor
    def read_data(self):
        return random.uniform(850, 1100)
