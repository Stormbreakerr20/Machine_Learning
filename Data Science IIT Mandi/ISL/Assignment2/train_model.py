import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn import mixture
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")


source = "Data Science IIT Mandi/ISL/Assignment2/Speaker_data-20241011T070731Z-001/Speaker_data/Voice_Samples_Training/"   

dest = "Data Science IIT Mandi/ISL/Assignment2/speaker_models/"

train_file = "train.txt"        

file_paths = open("Data Science IIT Mandi/ISL/Assignment2/train.txt",'r')

count = 1

features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print(path)
    
    # read the audio
    sr,audio = read(source + path)
    
    vector = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    if count == 5:    
        gmm =  mixture.GaussianMixture(n_components=16, max_iter=200, covariance_type='diag', n_init=3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        picklefile = path.split("-")[0]+".gmm"
        cPickle.dump(gmm,open(dest + picklefile,'wb'))
        print('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)
        features = np.asarray(())
        count = 0
    count = count + 1
    