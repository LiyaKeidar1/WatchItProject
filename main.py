from queue import Queue
from alert_service import AlertService, AlertMessage
import json, time, threading
from consts import SENSORS_MAP, TOO_LOW, TOO_HIGH, VALID



def load_configuration(path) -> json:
    with open(path, 'r') as file:
        return json.load(file)


def data_in_range(data, valid_range) -> int:
    if valid_range[0] <= data <= valid_range[1]:
        return VALID
    if data < valid_range[0]:
        return TOO_LOW
    if data > valid_range[1]:
        return TOO_HIGH


def sensor_monitor(sensor, valid_range, queue: Queue):
    while True:
        data = sensor.read_data()
        range_validity = data_in_range(data, valid_range)

        if range_validity == TOO_LOW:
            queue.put(AlertMessage(sensor=sensor.sensor_type, message_type="low", data=data))

        elif range_validity == TOO_HIGH:
            queue.put(AlertMessage(sensor=sensor.sensor_type, message_type="high", data=data))

        time.sleep(1)




if __name__ == "__main__":

    alert_queue = Queue()

    # Load configuration
    configuration = load_configuration('config.json')

    # Initialize alert service
    alert_service = AlertService(api_token="xoxe.xoxp-1-Mi0yLTY3MzkzMDEyNjc0NjAtNjc0OTUwMzk4OTY0OS02NzMzOTM1MzQ1MTczLTY3Mzk1MjMwMTIzNTYtZjI0YmIyMWMwZmRhZjQzZmNkNWU5MWE1YmVhMjcyNmQzNGYyODI2OTkyN2IwMGUzMjJmZmU0NjVlNjUxYjJkZA")

    threading.Thread(target=alert_service.start, args=(alert_queue,)).start()



    # Create threads for each sensor

    threads = []
    for sensor_config in configuration['sensors']:
        sensor_type = sensor_config['type']
        valid_range = sensor_config['valid_range']

        sensor = SENSORS_MAP.get(sensor_type, None)

        if sensor:
            # Create a thread for each sensor
            thread = threading.Thread(target=sensor_monitor, args=(sensor, valid_range, alert_queue))
            threads.append(thread)
            thread.start()
        else:
            print("No sensor found")
            pass

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
