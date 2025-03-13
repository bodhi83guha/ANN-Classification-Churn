#import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import pandas as pd
import numpy as np

## load trained model, scalar, onehot
model = load_model('model.h5')

## load scalar and onehot
with open('Label_Encoder_gender.pkl', 'rb') as file:
    Label_Encoder_gender = pickle.load(file)

with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file) 

with open('scalar.pkl', 'rb') as file:
    scalar = pickle.load(file)