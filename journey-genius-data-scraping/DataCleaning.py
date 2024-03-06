import os
import csv
import pandas as pd

data = pd.read_csv('journey-genius-data-scraping/TFIDF_ML.py')

# for data['Place'] in data:

data = data.drop(data[data['Place'] == 'Krispy Kreme'].idx)
