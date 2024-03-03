import secrets
from sensors import *
from secrets import *

SENSORS_MAP = {
    "TemperatureSensor": TemperatureSensor(),
    "HumiditySensor": HumiditySensor(),
    "PressureSensor": PressureSensor()
}

VALID = 1
TOO_LOW = -1
TOO_HIGH = 0

API_TOKEN = API_TOKEN_VAR
