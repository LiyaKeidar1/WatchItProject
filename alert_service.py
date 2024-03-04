import json
import time
from queue import Queue
from slack_sdk import WebClient
import requests
from consts import URL_MAP
from slack_sdk.errors import SlackApiError

class AlertMessage:
    def __init__(self, sensor, message_type, data):
        self.sensor = sensor
        self.message_type = message_type
        self.data = data

    def __repr__(self):
        return f"The {self.sensor} is too {self.message_type}: {self.data}"

    def __str__(self):
        return f"The {self.sensor} is too {self.message_type}: {self.data}"


class AlertService:
    def __init__(self):
        pass


    def notify_slack(self, channel, message: AlertMessage):

        webhook_url = URL_MAP[channel]
        headers = {'Content-type': 'application/json'}
        payload = {"text": str(message)}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            print(f"Message: {message} sent successfully!")
        else:
            print(f"Failed to send message: {message}. Status code: {response.status_code}, Response text: {response.text}")



    def start(self, queue: Queue):
        while True:
            if not queue.empty():
                notification = queue.get()
                sensor_type = notification.sensor
                self.notify_slack(channel=sensor_type, message=notification)
            time.sleep(1)





