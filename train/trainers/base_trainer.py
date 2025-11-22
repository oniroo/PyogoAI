import torch

class BaseTrainer:
    def __init__(self, model, datamodule, optimizer, loss_fn, device=None):
        if device is None:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.device = torch.device(device)

        self.model = model.to(self.device)
        self.dm = datamodule
        self.optim = optimizer
        self.loss_fn = loss_fn

    def train_one_epoch(self):
        self.model.train()
        for x, y in self.dm.train_dataloader():
            x, y = x.to(self.device), y.to(self.device)
            self.optim.zero_grad()
            logits = self.model(x)
            loss = self.loss_fn(logits, y)
            loss.backward()
            self.optim.step()