class BaseTrainer:
    def __init__(self, model, datamodule, optimizer, loss_fn, device='cpu'):
        self.model = model.to(device)
        self.dm = datamodule
        self.optim = optimizer
        self.loss_fn = loss_fn
        self.device = device

    def train_one_epoch(self):
        self.model.train()
        for x, y in self.dm.train_dataloader():
            x, y = x.to(self.device), y.to(self.device)
            self.optim.zero_grad()
            logits = self.model(x)
            loss = self.loss_fn(logits, y)
            loss.backward()
            self.optim.step()