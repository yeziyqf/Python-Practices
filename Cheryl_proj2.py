#根据某列内容决定输出到不同文件夹，输出txt名称为行id
import pandas as pd
import os
os.chdir('E:')
if not os.path.exists('1.csv'):
    exit(-1)
colname = ['ID','class','text']
nodes = pd.read_csv('idea2.csv',names = colname, header=None ,sep = ',',engine = 'python')
length = len(nodes['ID'])
print length


newDF = pd.DataFrame(columns=['text'])
for k in range(0,length):
    print(nodes['ID'][k])
    # print(nodes['class'][k])
    data = nodes['text'][k]





    if nodes['class'][k] == 0:
        print('class 0')
        newDF = nodes['text'][k]
        print(nodes['text'][k])
        # print(type(newDF))
        text_file = open('./0/' + nodes['ID'][k] + '.txt', "w")
        text_file.write(nodes['text'][k])
        text_file.close()
    if nodes['class'][k] == 1:
        print('class 1')
        newDF = nodes['text'][k]
        print(nodes['text'][k])
        # print(type(newDF))
        text_file = open('./1/' + nodes['ID'][k] + '.txt', "w")
        text_file.write(nodes['text'][k])
        text_file.close()

# print(text_file)

import json as json_import
import platform
import os
import requests
import sys
from requests.structures import CaseInsensitiveDict
import dateutil.parser as date_parser

try:
    from http.cookiejar import CookieJar  # Python 3
except ImportError:
    from cookielib import CookieJar  # Python 2

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(url= 'https://gateway.watsonplatform.net/natural-language-understanding/api', username= '75ef35e3-069e-44fe-b5d2-5f5f339d96a6', password= 'QDjWRR1WTGII',version= '2017-02-27')
response = natural_language_understanding.analyze(text='IBM is an American multinational technology company ''headquartered in Armonk, New York, United States, ''with operations in over 170 countries.',
  features=Features(
    entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2)))

print(json.dumps(response, indent=2))