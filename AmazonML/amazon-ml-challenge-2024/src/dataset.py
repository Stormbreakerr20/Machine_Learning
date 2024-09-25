import requests
import pandas as pd
from PIL import Image, ImageFilter
from torch.utils.data import Dataset


class DimensionsDataset(Dataset):
    def __init__(self, csv_file_path, transform=None):
        self.data = pd.read_csv(csv_file_path)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    @staticmethod
    def transform1(image):
        image = image.convert("L")
        image = image.point(lambda p: p * 1.2)
        image = image.point(lambda p: p > 205 and 255)
        image = image.filter(ImageFilter.MinFilter(3))
        return image

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        image = Image.open(requests.get(row["image_link"], stream=True).raw)
        entity_name = row["entity_name"]
        entity_value = row["entity_value"]
        if self.transform:
            image = self.transform(image)
        return {
            "image": image,
            "qa": [
                {
                    "question": f"{entity_name} of object?",
                    "answer": entity_value,
                }
            ],
        }
