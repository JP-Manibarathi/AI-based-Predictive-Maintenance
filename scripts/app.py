from data_collector import DataCollector
from feedback_handler import FeedbackHandler
import time
import threading

class PredictiveMaintenanceApp:
    def __init__(self):
        self.data_collector = DataCollector()
        self.feedback_handler = FeedbackHandler()
        self.systems = ["engine", "braking", "coolant"]  # Systems to monitor

    def run_rul_predictions(self):
        while True:
            for system in self.systems:
                sensor_data = self.data_collector.get_real_time_sensor_data(system)
                result = self.feedback_handler.make_predictions(sensor_data, system, model_type="rul")
                print(f"[RUL] {system.capitalize()} System Prediction: {result}")
            time.sleep(2 * 60 * 60)  # 2 hours

    def run_anomaly_and_fault_predictions(self):
        while True:
            for system in self.systems:
                sensor_data = self.data_collector.get_real_time_sensor_data(system)
                anomaly_result = self.feedback_handler.make_predictions(sensor_data, system, model_type="anomaly_detection")
                fault_result = self.feedback_handler.make_predictions(sensor_data, system, model_type="fault_detection")
                print(f"[Anomaly] {system.capitalize()} System Prediction: {anomaly_result}")
                print(f"[Fault] {system.capitalize()} System Prediction: {fault_result}")
            time.sleep(5 * 60)  # 5 minutes

    def run(self):
        rul_thread = threading.Thread(target=self.run_rul_predictions, daemon=True)
        anomaly_fault_thread = threading.Thread(target=self.run_anomaly_and_fault_predictions, daemon=True)
        rul_thread.start()
        anomaly_fault_thread.start()
        rul_thread.join()
        anomaly_fault_thread.join()

if __name__ == "__main__":
    app = PredictiveMaintenanceApp()
    app.run()
