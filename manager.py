import threading
from queue import Queue
from alert_service import AlertMessage
from consts import TOO_LOW, TOO_HIGH
from sensors import *
from utils import load_json, data_in_range


class Manager:
    SENSORS_MAP = {
        "TemperatureSensor": TemperatureSensor(),
        "HumiditySensor": HumiditySensor(),
        "PressureSensor": PressureSensor(),
    }

    def __init__(self, config_file: str, alert_queue):
        self.config = load_json(config_file)
        self.alert_queue = alert_queue

        # Create threads for each sensor
        self.sensor_threads = []

    def sensor_monitor(self, sensor, valid_range, queue: Queue):
        while True:
            data = sensor.read_data()
            range_validity = data_in_range(data, valid_range)

            if range_validity == TOO_LOW:
                queue.put(AlertMessage(sensor=sensor.sensor_type, message_type="low", data=data))

            elif range_validity == TOO_HIGH:
                queue.put(AlertMessage(sensor=sensor.sensor_type, message_type="high", data=data))

    def start(self):
        for sensor_config in self.config['sensors']:
            sensor_type = sensor_config['type']
            valid_range = sensor_config['valid_range']

            sensor = self.SENSORS_MAP.get(sensor_type, None)

            if sensor:
                thread = threading.Thread(target=self.sensor_monitor, args=(sensor, valid_range, self.alert_queue))
                self.sensor_threads.append(thread)
                thread.start()
            else:
                print("No sensor found")

        for thread in self.sensor_threads:
            thread.join()