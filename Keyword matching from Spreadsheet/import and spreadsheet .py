from google.colab import drive
drive.mount('/content/drive')

DATASET_CSV ='/content/drive/MyDrive/ProjectDataset/test.csv'

import pandas as pd

oop_dataset=pd.read_csv(DATASET_CSV, encoding="ISO-8859-1")
oop_dataset.head()
oop_dataset=oop_dataset[:1000]

df = pd.DataFrame(oop_dataset, columns = ['Question No.', 'Question', 'Student ID', 'Answer Key', 'Student Answer','Marks'])
print(df)

DATASET ='/content/drive/MyDrive/ProjectDataset/Dataset.xlsx'

!python -m spacy download en_core_web_lg
import spacy
nlp = spacy.load("en_core_web_lg")

import numpy as np
import itertools
from sklearn.cluster import KMeans
import pprint
import nltk
from nltk.tokenize import word_tokenize
oop_dataset=pd.read_excel(DATASET)
oop_dataset.head()
oop_dataset=oop_dataset[:1000]

df = pd.DataFrame(oop_dataset, columns = ['Student Answer'])
stud_ans=df['Student Answer'].tolist()
print("\nStudent answers:\n")
print(stud_ans)


df = pd.DataFrame(oop_dataset, columns = ['Answer Key'])
key=df['Answer Key'].tolist()
print("\nAnswer Key:\n")
key=key[0]
ans_doc=nlp(key)
print(ans_doc)

pip install sentence-transformers