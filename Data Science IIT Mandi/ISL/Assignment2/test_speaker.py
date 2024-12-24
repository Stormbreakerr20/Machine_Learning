import os
import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
import time
import csv

warnings.filterwarnings("ignore")

source = "Data Science IIT Mandi/ISL/Assignment2/Speaker_data-20241011T070731Z-001/Speaker_data/Testing_Audio/"   

modelpath = "Data Science IIT Mandi/ISL/Assignment2/speaker_models/"

gmm_files = [os.path.join(modelpath, fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
models = [cPickle.load(open(fname, 'rb')) for fname in gmm_files]
speakers = [fname.split("\\")[-1].split(".gmm")[0] for fname in gmm_files]

output_csv = "Data Science IIT Mandi/ISL/Assignment2/predictions.csv"
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["File", "Speaker"])

    for path in os.listdir(source):
        if not path.endswith('.wav'):
            continue

        filename = os.path.basename(path)

        sr, audio = read(os.path.join(source, path))
        vector = extract_features(audio, sr)
        
        log_likelihood = np.zeros(len(models))
        
        for i in range(len(models)):
            gmm = models[i]
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()
        
        winner = np.argmax(log_likelihood)
        
        predicted_speaker = speakers[winner].split('/')[-1]

        print(f"{filename}\tdetected as - {predicted_speaker}")
        writer.writerow([filename, predicted_speaker])
