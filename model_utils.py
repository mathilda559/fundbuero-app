import torch
from torchvision import models, transforms
from PIL import Image

# Modell laden
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

# Bildtransformation
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
])

# ImageNet Klassen laden
import json
import urllib.request

url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
classes = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

def classify_image(img: Image.Image):

    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)

    _, predicted = outputs.max(1)
    label = classes[predicted.item()].lower()

    if "jacket" in label or "coat" in label:
        return "Jacke"

    if "sweater" in label or "sweatshirt" in label:
        return "Pullover"

    return "Unbekannt"
