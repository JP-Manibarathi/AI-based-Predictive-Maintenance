import random

class DataCollector:
    def __init__(self):
        self.features = {
            "engine": {
                "rul": ['ENGINE_RPM ()', 'COOLANT_TEMPERATURE ()', 'ENGINE_LOAD ()', 'FUEL_TANK ()'],
                "anomaly_detection": ['ENGINE_RPM ()', 'COOLANT_TEMPERATURE ()', 'ENGINE_LOAD ()', 'FUEL_TANK ()'],
                "fault_detection": ['Engine rpm', 'Lub oil pressure', 'Fuel pressure', 'Coolant pressure', 'lub oil temp', 'Coolant temp']
            },
            "braking": {
                "rul": ['BRAKE_PRESSURE ()', 'BRAKE_PAD_THICKNESS ()'],
                "anomaly_detection": ['BRAKE_TEMPERATURE ()', 'BRAKE_FORCE ()'],
                "fault_detection": ['BRAKE_PAD_THICKNESS ()', 'BRAKE_PRESSURE ()', 'BRAKE_FORCE ()']
            },
            "coolant": {
                "rul": ['COOLANT_LEVEL ()', 'COOLANT_TEMPERATURE ()', 'COOLANT_FLOW_RATE ()'],
                "anomaly_detection": ['COOLANT_TEMPERATURE ()', 'COOLANT_PRESSURE ()'],
                "fault_detection": ['COOLANT_LEVEL ()', 'COOLANT_TEMPERATURE ()', 'COOLANT_PRESSURE ()']
            }
        }

    def get_real_time_sensor_data(self, system):
        data = {}
        for model, features in self.features[system].items():
            for feature in features:
                data[feature] = round(random.uniform(0.0, 100.0), 2)  # Generate random sensor values
        return data
