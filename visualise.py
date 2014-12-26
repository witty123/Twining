import pandas as pd

DATA_FILES = ['tweets_microsoft.json', 'tweets_sony.json', 'tweets_galaxys5.json', 'tweets_iphone6.json']
data_frames = dict()

for data_file in DATA_FILES:
    data = "[{0}]".format(",".join([line for line in open(data_file).readlines()]))
    data_frames[data_file.split('_')[1].split('.')[0]] = pd.read_json(data, orient='records')
    
# All the values should be of data frame type
print {k:type(v) for k,v in data_frames.items()}

# to see an individual sample data frame
print data_frames['microsoft']
