#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
import pandas as pd
from elasticsearch import helpers, Elasticsearch


# In[2]:


index_name = input("Enter index name: ")
filename =  input("Enter file name with extension: ")

print("index :", index_name + "!")
print("file :", filename + "!")


# In[3]:


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
cpt=1
df = pd.read_csv(filename, sep=';')

def csv_to_json(file,df,cpt):
    cpt+=1
    df = df.iloc[cpt-1:cpt,:]
    json_data = df.to_json(orient='records')
    json_data = json.loads(json_data)
    with open(file+'.json', 'w+') as outfile:
        json.dump(json_data, outfile,indent=4)
    return (str(file)+".json")

def csv_reader(file_name,cpt,index_name):
    with open(file_name) as json_file:
        json_docs = json.load(json_file)[0]
        es.index(index=index_name, doc_type='type', id=cpt, body=json_docs)
        print(cpt,"line to ES done")
        
for i in range(0,len(df)-1):
    csv_reader(csv_to_json(filename.split(".")[0],df,cpt),cpt,index_name)
    cpt+=1


# In[ ]:




