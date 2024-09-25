import torch
import random
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from tqdm import tqdm

model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    revision=revision,
    trust_remote_code=True,
    torch_dtype=torch.float16,
).eval().to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

trnhdf = pd.read_csv("test.csv")
wat = trnhdf[trnhdf["entity_name"] == "wattage"]


for index, row in tqdm(wat.iterrows()):
    url = row["image_link"]
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    enc_image = model.encode_image(image).to('cuda')
    predicted_value = model.answer_question(enc_image, "wattage?", tokenizer)
    wat.at[index, 'prediction'] = predicted_value
    
    wat.to_csv("moon_wattage_predictions.csv", index=False)
    

volt = trnhdf[trnhdf["entity_name"] == "voltage"]
for index, row in tqdm(volt.iterrows()):
    url = row["image_link"]
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    enc_image = model.encode_image(image).to('cuda')
    predicted_value = model.answer_question(enc_image, "voltage?", tokenizer)
    volt.at[index, 'prediction'] = predicted_value
    volt.to_csv("moon_voltage_predictions.csv", index=False)
    

wt = trnhdf[trnhdf["entity_name"] == "weight"]

for index, row in tqdm(wt.iterrows()):
    url = row["image_link"]
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    enc_image = model.encode_image(image).to('cuda')
    predicted_value = model.answer_question(enc_image, "weight?", tokenizer)
    wt.at[index, 'prediction'] = predicted_value
    wt.to_csv("moon_weight_predictions.csv", index=False)