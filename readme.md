# Librairies
```python
> csv
> json
> pandas
> elasticsearch 
> flask
> requests
> json2html
```

# Installation example
ES must be on port 9200 & Kibana on port 5601

```bash
./elasticsearch
```
```bash
./bin/kibana
```
```bash
python Ingestion_of_data.py
Enter index name: tree
Enter file name with extension: trees.csv
```
=> Create the index pattern in "Stack Management"

```bash
python app.py
```


# Ingestion of data
Launch the python file in the same directory as trees.csv. This will convert your file form csv to json and import these data to a new ES index. Don't forget to create the index pattern after in "Stack Management". If you have an issue entering your index and file name, please change directly the value in the python file (issue regarding powershell). 

![](overview.png)

# Queries

Launch the python file in the same directory as the folder templates. This will run the web application on localhost on port 5000 by default.

![](overview2.png)

When you click on the Show Index Button, it list you all the indexes that exist on ElasticSearch.

![](overview3.png)

When you enter the name of an Index, it show you all the labels of the index.

![](overview4.png)

When you post a query like: "SELECT * FROM trees WHERE ARRONDISSEMENT = 16".

![](overview5.png)
