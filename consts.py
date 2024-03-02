from sensors import *

SENSORS_MAP = {
    "TemperatureSensor": TemperatureSensor(),
    "HumiditySensor": HumiditySensor(),
    "PressureSensor": PressureSensor()
}

VALID = 1
TOO_LOW = -1
TOO_HIGH = 0


