import joblib
import numpy as np

class FeedbackHandler:
    def __init__(self):
        self.models = {
            "rul": joblib.load(r"C:\\Users\\Manibharathi\\Downloads\\AI-based-Predictive-Maintenance\\models\\engine_rul_calc.pkl"),
            "fault_detection": joblib.load(r"C:\\Users\\Manibharathi\\Downloads\\AI-based-Predictive-Maintenance\\models\\engine_fault_prediction.pkl"),
            "anomaly_detection": joblib.load(r"C:\\Users\\Manibharathi\\Downloads\\AI-based-Predictive-Maintenance\\models\\engine_anomaly_detection.pkl"),
        }
        self.features = {
            "rul": ['ENGINE_RPM ()', 'COOLANT_TEMPERATURE ()', 'ENGINE_LOAD ()', 'FUEL_TANK ()'],
            "anomaly_detection": ['ENGINE_RPM ()', 'COOLANT_TEMPERATURE ()', 'ENGINE_LOAD ()', 'FUEL_TANK ()'],
            "fault_detection": ['Engine rpm', 'Lub oil pressure', 'Fuel pressure', 'Coolant pressure', 'lub oil temp', 'Coolant temp']
        }

def reshape_input(self, sensor_data, model_features, model_name):
    data_array = np.array([sensor_data[feature] for feature in model_features])

    if model_name == "rul":  # Example: RUL model might expect time-series (3D) input
        padded_data = np.zeros((50, 26))
        padded_data[:, :len(data_array)] = np.tile(data_array, (50, 1))
        return padded_data.reshape(1, 50, 26)  # Reshape to (1, 50, 26)
    else:
        return data_array.reshape(1, -1)  # Reshape to (1, n_features)

def make_predictions(self, sensor_data):
    results = {}
    try:
        for model_name, model in self.models.items():
            model_features = self.features[model_name]
            reshaped_data = self.reshape_input(sensor_data, model_features, model_name)
            prediction = model.predict(reshaped_data)[0]

            if model_name == "rul":
                results["RUL Prediction"] = prediction
            elif model_name == "fault_detection":
                results["Fault Detection"] = "Faulty" if prediction == 1 else "Normal"
            elif model_name == "anomaly_detection":
                results["Anomaly Detection"] = "Anomaly" if prediction == 1 else "Normal"
    except Exception as e:
        results["error"] = str(e)
    return results