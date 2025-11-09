# import torch, torch.nn as nn
#
# class BaseModel(nn.Module):
#     def forward(self, x):
#         raise NotImplementedError
#
#     def predict(self, x):
#         self.eval()
#         with torch.no_grad():
#             return self.forward(x)
#
#     def load_pretrained(self, pretrained_path):
#         self.load_state_dict(torch.load(pretrained_path))