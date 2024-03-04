from queue import Queue
from alert_service import AlertService
import threading
from manager import Manager

if __name__ == "__main__":
    alert_queue = Queue()

    # Initialize alert service and starting the alert receiving process
    alert_service = AlertService(alert_queue)
    threading.Thread(target=alert_service.start).start()

    manager = Manager("config.json", alert_queue)
    manager.start()
