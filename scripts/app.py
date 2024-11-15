from data_collector import DataCollector
from feedback_handler import FeedbackHandler
import time

class PredictiveMaintenanceApp:
    def __init__(self):
        self.data_collector = DataCollector()
        self.feedback_handler = FeedbackHandler()

    def run(self):
        while True:
            # Step 1: Collect real-time sensor data
            sensor_data = self.data_collector.get_real_time_sensor_data()
            print(f"Received Data: {sensor_data}")

            # Step 2: Make predictions
            result = self.feedback_handler.make_predictions(sensor_data)
            print(f"Prediction Results: {result}")

            # Step 3: Simulate real-time loop with delay
            time.sleep(1)  # Adjust as needed

if __name__ == "__main__":
    app = PredictiveMaintenanceApp()
    app.run()



