import torch
import torchvision
import torchvision.transforms as transforms

# 데이터 전처리
transform = transforms.Compose([
    transforms.Resize((128, 128)),  # 이미지 크기 조정
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 학습 데이터셋
trainset = torchvision.datasets.CIFAR10(
    root='./data', train=True, download=True, transform=transform
)

train_loader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)

# 테스트 데이터셋
test_set = torchvision.datasets.CIFAR10(
    root='./data', train=False, download=True, transform=transform
)

test_loader = torch.uails.data.DataLoader(test_set, batch_size=32, shuffle=False)