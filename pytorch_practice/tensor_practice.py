import torch
import numpy as np

# --TENSOR--
# We use tensors to encode the inputs and outputs of a model, as well as the model’s parameters.

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

# From another tensor
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored: {tensor.device}")

# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
    print(f"Device tensor is stored on: {tensor.device}")

# Standard numpy-like indexing and slicing 
tensor = torch.ones(4, 4)
tensor[:,1] = 0
print(tensor)

# Joining tensors
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

# Multiplying tensors
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")

# This computes the matrix multiplication between two tensors
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")

# In-place operations
print(tensor, "\n")
tensor.add_(8)
print(tensor)