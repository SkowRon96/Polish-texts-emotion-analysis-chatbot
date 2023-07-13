import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#Load dataset
filename = 'Data/train-emotion.tsv'
df = pd.read_csv(filename, sep = "\t")
df = df.drop('conv_id', axis=1)
df = df.drop('prompt', axis=1)
df = df.drop('sentiment', axis=1)
df = df.drop('sentiment_idx', axis=1)
happiness = df.loc[(df['mood'] == 'happiness')]
happiness = happiness.iloc[:242]
happiness['emotion'] = 1
neutral = df.loc[(df['mood'] == 'neutral')]
neutral = neutral.iloc[:242]
neutral['emotion'] = 0
sadness = df.loc[(df['mood'] == 'sadness')]
sadness = sadness.iloc[:242]
sadness['emotion'] = 2
fear = df.loc[(df['mood'] == 'fear')]
fear = fear.iloc[:242]
fear['emotion'] = 3
anger = df.loc[(df['mood'] == 'anger')]
anger = anger.iloc[:242]
anger['emotion'] = 4
surprise = df.loc[(df['context'] == 'embarrassed')]
surprise = surprise.iloc[:242]
surprise['emotion'] = 6
disgust = df.loc[(df['context'] == 'disgusted')]
disgust = happiness.iloc[:242]
disgust['emotion'] = 5

final_df = pd.concat([happiness, neutral, sadness, fear, anger, surprise , disgust], axis=0)
final_df = final_df.drop('mood', axis=1)
final_df = final_df.drop('mood_idx', axis=1)
final_df = final_df.drop('context', axis=1)
final_df = final_df.rename(columns={'prompt_pl': 'text'})
new = final_df.drop_duplicates()

# Delete All NaN values from columns -> ['description','rate']
new = new[new['text'].notnull() & new['emotion'].notnull()]

# Set all strings as lower case letters
new['text'] = new['text'].str.lower()
from sklearn.utils import shuffle
df = shuffle(new)
df.to_csv('Data/cortex_dataset_test.csv', sep=',', encoding='utf-8', index=False)