# **Sensor Monitoring System**

This Python script is a simple sensor monitoring system that reads data 
from various sensors, checks if the data is within a specified valid range, 
and generates alerts if the data is too low or too high.

The alerts are then processed by an alert service that notifies a **Slack App** on occurrences to different channels (based on the sensor in fault).

### Settings:

* **Manager:** implements the starting point for each sensor thread and for the main thread. The manager receives data from the sensors and logs the invalid data in a message queue. (function: sensor_monitor())

* **Alert Service**: the queue is in use by the alert service which takes messages (function: start()) and deports them to "SLACK" (function: notify_slack())

* **Sensor:** three different sensors that simulate reading data from a real sensor

* **main:** starts the main thread and calls the manager.