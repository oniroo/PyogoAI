from abc import ABC, abstractmethod
from typing import Dict, Any

class SensorHandler(ABC):
    """
    1. 센서 데이터 형식: 전부 JSON으로 통일
    2. 종류: CO2, 온습도, 토양 습도, 이미지
    3. 데이터 읽기
    4. 데이터 저장: JSON(Time Series), png(Image)
    """
    @abstractmethod
    def handle(self, data: Dict[str, Any]) -> None:
        """
        payload 처리 수 결과 리턴
        """
        raise NotImplementedError
