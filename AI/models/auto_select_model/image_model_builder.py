r"""모델 생성 담당"""
from torchvision import models
from classifier_patch import patch_classifier

def build_image_model(cfg, num_classes: int):
    base = cfg["Image model"]["base"]
    selected = cfg["Image model"][base]["selected"]

    if base == "CNN":
        if selected == "ResNet50":
            m = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
        elif selected == "ResNet101":
            m = models.resnet101(weights=models.ResNet101_Weights.DEFAULT)
        else:
            raise ValueError(f"Unsupported CNN variant: {selected}")
        return patch_classifier(m, num_classes)

    elif base == "ConvNeXt":
        model_name = f"convnext_{selected}"
        if not hasattr(models, model_name):
            raise ValueError(f"Unsupported ConvNeXt variant: {selected}")
        m = getattr(models, model_name)(weights="DEFAULT")
        return patch_classifier(m, num_classes)

    else:
        raise ValueError(f"Unsupported image model base: {base}")