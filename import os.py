import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

import librosa
import soundfile as sf
from pydub import AudioSegment
from mutagen import File as MutagenFile

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

import requests
from bs4 import BeautifulSoup
# API Spotify (si utilisé)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Optionnel deep learning
import tensorflow as tf
# ou
import torch