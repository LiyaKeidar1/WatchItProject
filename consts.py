
from sensors import *


SENSORS_MAP = {
    "TemperatureSensor": TemperatureSensor(),
    "HumiditySensor": HumiditySensor(),
    "PressureSensor": PressureSensor()
}

VALID = 1
TOO_LOW = -1
TOO_HIGH = 0


URL_MAP = {
    "humidity" : "https://hooks.slack.com/services/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",
    "temperature" : "https://hooks.slack.com/services/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",
    "pressure" : "https://hooks.slack.com/services/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"
}

