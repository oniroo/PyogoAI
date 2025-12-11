from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class SensorPayload:
    type: str
    sensor_id: Optional[str]
    timestamp: str
    value: Any
    meta_data: Dict[str, Any]