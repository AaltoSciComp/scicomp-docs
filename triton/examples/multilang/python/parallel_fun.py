import torch 
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
import os

maxprocesses = int(os.getenv('SLURM_CPUS_PER_TASK'))

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

train_dataloader = DataLoader(training_data, num_workers=maxprocesses, batch_size=64, shuffle=True)

for train_feature, train_label in train_dataloader:    
    print(train_label)