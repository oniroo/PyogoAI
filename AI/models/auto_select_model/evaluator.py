import torch
from torch.utils.data import DataLoader

def evaluate_model(model, dataset, device="cpu"):
    model.eval()
    loader = DataLoader(dataset, batch_size=32)
    correct, total = 0, 0
    with torch.no_grad():
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            outputs = model(x)
            preds = outputs.argmax(dim=1)
            correct += (preds == y).sum().item()
            total += y.size(0)
    return correct / total if total > 0 else 0.0