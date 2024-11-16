import joblib
import numpy as np

class FeedbackHandler:
    def __init__(self):
        self.models = {
            "engine": {
                "rul": joblib.load(r"C:\\path\\to\\engine_rul_calc.pkl"),
                "fault_detection": joblib.load(r"C:\\path\\to\\engine_fault_prediction.pkl"),
                "anomaly_detection": joblib.load(r"C:\\path\\to\\engine_anomaly_detection.pkl"),
            },
            "braking": {
                "rul": joblib.load(r"C:\\path\\to\\braking_rul_calc.pkl"),
                "fault_detection": joblib.load(r"C:\\path\\to\\braking_fault_prediction.pkl"),
                "anomaly_detection": joblib.load(r"C:\\path\\to\\braking_anomaly_detection.pkl"),
            },
            "coolant": {
                "rul": joblib.load(r"C:\\path\\to\\coolant_rul_calc.pkl"),
                "fault_detection": joblib.load(r"C:\\path\\to\\coolant_fault_prediction.pkl"),
                "anomaly_detection": joblib.load(r"C:\\path\\to\\coolant_anomaly_detection.pkl"),
            },
        }

    def reshape_input(self, sensor_data, model_features, model_type):
        data_array = np.array([sensor_data[feature] for feature in model_features])
        if model_type == "rul":
            padded_data = np.zeros((50, 26))
            padded_data[:, :len(data_array)] = np.tile(data_array, (50, 1))
            return padded_data.reshape(1, 50, 26)  # Reshape to (1, 50, 26)
        else:
            return data_array.reshape(1, -1)  # Reshape to (1, n_features)

    def make_predictions(self, sensor_data, system, model_type):
        try:
            model = self.models[system][model_type]
            model_features = DataCollector().features[system][model_type]
            reshaped_data = self.reshape_input(sensor_data, model_features, model_type)
            prediction = model.predict(reshaped_data)[0]

            if model_type == "rul":
                return {"RUL Prediction": prediction}
            elif model_type == "fault_detection":
                return {"Fault Detection": "Faulty" if prediction == 1 else "Normal"}
            elif model_type == "anomaly_detection":
                return {"Anomaly Detection": "Anomaly" if prediction == 1 else "Normal"}
        except Exception as e:
            return {"error": str(e)}
