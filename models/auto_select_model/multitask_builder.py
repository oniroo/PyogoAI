from image_model_builder import build_image_model
from timeseries_model_builder import build_timeseries_model

def build_multitask_models(cfg, num_classes_img, num_classes_ts, input_size_ts=10):
    models, names = [], []

    # 이미지 모델 후보
    for name in cfg["Image model"]["CNN"]["models"]:
        subcfg = {"Image model": {"base": "CNN", "CNN": {"selected": name}}}
        try:
            m = build_image_model(subcfg, num_classes_img)
            models.append(m)
            names.append(name)
        except Exception:
            pass

    for name in cfg["Image model"]["ConvNeXt"]["models"]:
        subcfg = {"Image model": {"base": "ConvNeXt", "ConvNeXt": {"selected": name}}}
        try:
            m = build_image_model(subcfg, num_classes_img)
            models.append(m)
            names.append(f"convnext_{name}")
        except Exception:
            pass

    # 시계열 모델 후보
    for name in cfg["Timeseries model"]["LSTM"]["models"]:
        m = build_timeseries_model("LSTM", name, num_classes_ts, input_size=input_size_ts)
        models.append(m)
        names.append(f"LSTM_{name}")

    for name in cfg["Timeseries model"]["Transformer"]["models"]:
        m = build_timeseries_model("Transformer", name, num_classes_ts, input_size=input_size_ts)
        models.append(m)
        names.append(f"Transformer_{name}")

    return models, names