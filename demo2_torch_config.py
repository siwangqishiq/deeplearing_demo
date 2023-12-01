import torch

def ShowTorchInfo():
    print("Torch Info:")
    print("version:", torch.__version__)
    print("cuda support:", torch.cuda.is_available())
    print("device:", torch.device.__name__)

def testGrad():
    x = torch.ones(2,2 , requires_grad=True)
    x = x * 2
    x.requires_grad_(True)
    y = x ** 2
    print(y)
    # print(y.grad())

# print(__name__)
if(__name__ == "__main__"):
    ShowTorchInfo()
    testGrad()