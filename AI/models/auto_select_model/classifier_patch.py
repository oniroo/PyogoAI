"""마지막 분류기 패치 담당"""
import torch.nn as nn

def patch_classifier(model, num_classes: int):
    r"""모델 마지막 레이어를 num_classes에 맞게 교체"""

    if hasattr(model, "fc"):
        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, num_classes)
    elif hasattr(model, "classifier"):
        last_layer = model.classifier[-1]
        if isinstance(last_layer, nn.Linear):
            in_features = last_layer.in_features
            model.classifier[-1] = nn.Linear(in_features, num_classes)
        else:
            for i, layer in enumerate(model.classifier):
                if isinstance(layer, nn.Linear):
                    in_features = layer.in_features
                    model.classifier[i] = nn.Linear(in_features, num_classes)
                    break
            else:
                raise ValueError("No Linear layer found in classifier")
    else:
        raise ValueError("Unknown classifier structure (no fc or classifier)")

    return model