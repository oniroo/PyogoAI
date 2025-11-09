import torch
from torch.utils.data import TensorDataset

from config_loader import load_config
from multitask_builder import build_multitask_models
from candidate_filter import select_candidates_by_data
from model_selector import ModelSelector
from evaluator import evaluate_model

if __name__ == "__main__":
    cfg = load_config()

    # 후보 모델 자동 생성
    all_models, model_names = build_multitask_models(cfg, num_classes_img=10, num_classes_ts=5, input_size_ts=10)

    # 더미 데이터셋 (실제는 CIFAR10, 센서 데이터 등 사용)
    img_X = torch.randn(200, 3, 224, 224)
    img_y = torch.randint(0, 10, (200,))
    img_dataset = TensorDataset(img_X, img_y)

    ts_X = torch.randn(300, 50, 10)
    ts_y = torch.randint(0, 5, (300,))
    ts_dataset = TensorDataset(ts_X, ts_y)

    # 데이터 크기 자동 측정
    data_sizes = {"image": len(img_dataset), "timeseries": len(ts_dataset)}

    # threshold는 YAML에서 읽음
    thresholds = cfg["Thresholds"]

    # 필터링
    eligible_models, eligible_names = select_candidates_by_data(
        all_models, model_names, max(data_sizes.values()), thresholds
    )

    # 이미지/시계열 후보 분리
    image_models, image_names, ts_models, ts_names = [], [], [], []
    for m, n in zip(eligible_models, eligible_names):
        if "ResNet" in n or "convnext" in n:
            image_models.append(m)
            image_names.append(n)
        else:
            ts_models.append(m)
            ts_names.append(n)

    # 이미지 모델 평가 및 선택
    if image_models:
        img_scores = [evaluate_model(m, img_dataset) for m in image_models]
        img_selector = ModelSelector(image_models, image_names)
        best_img_model, best_img_name, best_img_score = img_selector.select(img_scores)
        print(f"[이미지] 최종 선택된 모델: {best_img_name}, 점수: {best_img_score:.4f}")
    else:
        print("[이미지] 후보 모델 없음")

    # 시계열 모델 평가 및 선택
    if ts_models:
        ts_scores = [evaluate_model(m, ts_dataset) for m in ts_models]
        ts_selector = ModelSelector(ts_models, ts_names)
        best_ts_model, best_ts_name, best_ts_score = ts_selector.select(ts_scores)
        print(f"[시계열] 최종 선택된 모델: {best_ts_name}, 점수: {best_ts_score:.4f}")
    else:
        print("[시계열] 후보 모델 없음")

    print(f"데이터 크기: {data_sizes}")