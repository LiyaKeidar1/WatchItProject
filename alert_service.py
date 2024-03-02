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


class AlertService:
    def __init__(self, api_token):
        self.client = WebClient(api_token)

    def start(self, queue: Queue):
        while not queue.empty():
            notification = queue.get()
            sensor_type = notification.sensor
            self.notify(channel = sensor_type,  message = notification)

    def notify(self, channel, message: AlertMessage):
        try:
            response = self.client.chat_postMessage(channel, message)
            print(f"Message sent successfully: {response['ts']}")
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")
        print(message)




# Function to send a message to Slack
# def send_slack_message(api_token, channel, message):
#
#
#
#
# # Example usage
# if __name__ == "__main__":
#     # Set your Slack API token and channel
#     slack_api_token = 'your_slack_api_token'
#     slack_channel = '#your_channel_name'
#
#     # Message to be sent
#     alert_message = "Invalid data detected in the sensor!"
#
#     # Send the message to Slack
#     send_slack_message(slack_api_token, slack_channel, alert_message)
