import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# Get Device for Training
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.isavailable()
    else "cpu"
)

print(f"Using {device} device")

# Define the class
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    
model = NeuralNetwork().to(device)
print(model)
print()

X = torch.rand(1, 28, 28, device=device)
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")

# Model layers
input_image = torch.rand(3, 28, 28)
print(input_image.size())

# nn.Flatten
# We initialize the nn.Flatten layer to convert each 2D 28x28 image into a contiguous array of 
# 784 pixel values ( the minibatch dimension (at dim=0) is maintained).

flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())

#nn.Linear
# The linear layer is a module that applies a linear transformation 
# on the input using its stored weights and biases.

layer1 = nn.Linear(in_features=28 * 28, out_features=20)
hidden1 = layer1(flat_image)
print(hidden1.size())

# nn.ReLu
# Non-linear activations are what create the complex mappings between the model’s 
# inputs and outputs. They are applied after linear transformations to introduce 
# nonlinearity, helping neural networks learn a wide variety of phenomena.

print(f"Before ReLU: {hidden1} \n\n")
hidden1 = nn.ReLU()(hidden1)
print(f"After ReLU: {hidden1}")

#nn.Sequential
# nn.Sequential is an ordered container of modules. The data is passed through all the modules in the 
# same order as defined. You can use sequential containers to put together a quick network like seq_modules.

seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)

input_image = torch.rand(3, 28, 28)
logits = seq_modules(input_image)