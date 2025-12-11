"""
왜 이렇게 설계했는가?
1) PyTorch 모델과 바로 연결 가능
- LSTM, Transformer 모두 (batch, seq_len, feature_dim) 형태를 사용해.
- 따라서 train_x, val_x, test_x 모두 동일한 형태로 유지.
2) AutoML 파이프라인에서 공통 인터페이스로 사용
- SearchEngine, Evaluator, Orchestrator 모두 이 구조를 그대로 사용.
- 데이터 구조가 통일되면 모듈 간 연결이 쉬워짐.
3) 연구 확장성
- horizon, freq, is_multivariate 같은 정보는
ModelFamilySelector나 TemplateGenerator에서 중요한 힌트
"""
from dataclasses import dataclass

import torch


@dataclass
class TimeSeriesDataSet:
    # 학습 입력
    train_x: torch.Tensor # (N, T, D_in)
    train_y: torch.Tensor # (N, D_out) or (N, T_out)

    # 검증 입력
    val_x: torch.Tensor
    val_y: torch.Tensor

    # 테스트 입력
    test_x: torch.Tensor
    test_y: torch.Tensor


    # 메타 정보
    freq: str               # 'H', 'D', 'M' 등
    input_dim: int          # D_in
    output_dim: int         # D_out
    hoirizon: int           # 예측 길이
    is_multivariable: bool  # 다변량 여부