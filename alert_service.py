import json
import requests
from consts import URL_MAP


# class for creating a message
class AlertMessage:
    def __init__(self, sensor, message_type, data):
        self.sensor = sensor
        self.message_type = message_type
        self.data = data

    def __repr__(self):
        return f"The {self.sensor} is too {self.message_type}: {self.data}"


# class for starting the alert service system and for Slack notification
class AlertService:
    def __init__(self, alert_queue):
        self.alert_queue = alert_queue

    def notify_slack(self, channel, message: AlertMessage):
        webhook_url = URL_MAP[channel]
        headers = {'Content-type': 'application/json'}
        payload = {"text": str(message)}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            print(f"Message: {message} sent successfully!")
        else:
            print(f"Failed to send message: {message}. Status code: {response.status_code}, Response text: {response.text}")

    def start(self):
        while True:
            if not self.alert_queue.empty():
                notification = self.alert_queue.get()
                sensor_type = notification.sensor
                self.notify_slack(channel=sensor_type, message=notification)

