import json
import os

from hardwares.enums import SensorType

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SAVE_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(SAVE_DIR, exist_ok=True)


def save_json(sensor_type: SensorType, sensor_data: dict):
    sensor_name = sensor_type.value
    file_name = f"{sensor_name}_{sensor_type.name}_sensor_data.json"
    file_path = os.path.join(SAVE_DIR, file_name)

    print(f"Saving data to {file_path}")
    with open(file_path, 'w') as f:
        json.dump(sensor_data, f)


def load_json(sensor_type: SensorType) -> dict:
    sensor_name = sensor_type.value
    file_name = f"{sensor_name}_{sensor_type.name}_sensor_data.json"
    file_path = os.path.join(SAVE_DIR, file_name)

    print(f"Loading data from {file_path}")

    if not os.path.exists(file_path):
        return {}

    with open(file_path, 'r') as f:
        return json.load(f)