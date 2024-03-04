# **Sensor Monitoring System**

This Python script is a simple sensor monitoring system that reads data 
from various sensors, checks if the data is within a specified valid range, 
and generates alerts if the data is too low or too high.

The alerts are then processed by an alert service that notifies a **Slack App** on occurrences to different channels (based on the sensor in fault).

### Settings:

* **Threads:** each sensor generates information and creates alerts messages simultaneously on three different thread,
while the main thread pulls the alerts from the queue (explained below).

* **Messaging Queue:** the communication between the different threads happens
using a message queue
that's being filled with messages from the function *sensor_monitor* 
on 3 different threads and emptied from messages with 
the *AlertService.start()* on the main thread.
