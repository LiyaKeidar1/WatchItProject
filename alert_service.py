import time
from queue import Queue
from slack_sdk import WebClient
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
    def __init__(self, api_token):
        self.client = WebClient(api_token)

    def notify(self, channel, message: AlertMessage):
        try:
            response = self.client.chat_postMessage(channel=channel, text=message.__str__())
            print(f"Message sent successfully: {response['ts']}")
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")

        print(message)

    def start(self, queue: Queue):
        while True:
            if not queue.empty():
                notification = queue.get()
                sensor_type = notification.sensor
                self.notify(channel=sensor_type,  message=notification)
            time.sleep(1)





