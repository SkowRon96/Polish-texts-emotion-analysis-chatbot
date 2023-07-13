import pandas as pd

filename = 'data_generator/generated_datatset.csv'
dataset = pd.read_csv(filename, delimiter = ",", nrows=200000)
new = dataset.drop_duplicates()

# Delete All NaN values from columns -> ['description','rate']
new = new[new['text'].notnull() & new['emotion'].notnull()]

# Set all strings as lower case letters
new['text'] = new['text'].str.lower()
new.to_csv('data_generator/generated_datatset_new.csv', sep=',', encoding='utf-8', index=False)