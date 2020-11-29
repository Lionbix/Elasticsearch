from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
import json, requests
from json2html import *

build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style" : "width:100%"}

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
url2query = 'http://localhost:9200/_xpack/sql'
url2list = 'http://localhost:9200/_cluster/health?level=indices'
headers = {
   'Content-Type': 'application/json',
}

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		details = request.form
		if details['form_type'] == 'get_query':
			return get_ES(details['queryInput'])

		if details['form_type'] == 'get_index':
			return show_index()

		if details['form_type'] == 'get_labels':
			return show_labels(details['nameIndex'])

	return render_template('index.html')

def get_ES(query2):
	query = {'query': query2}
	response = requests.post(url2query, headers=headers, data=json.dumps(query))
	data = response.content.decode('utf-8').replace("'", '')
	data2 = json.loads(data)
	data3 = json.dumps(data2, indent=2, sort_keys=True)
	data4 = json2html.convert(json = data3)
	return data4

def show_index():
	response = requests.get(url2list)
	data = json.loads(response.content)
	data2 = json2html.convert(json = data)
	return data2

def show_labels(name):
	query = {'query': "SELECT * FROM %s LIMIT 0" % (name)}
	response = requests.post(url2query, headers=headers, data=json.dumps(query))
	data = response.content.decode('utf-8').replace("'", '"')
	data2 = json.loads(data)
	data3 = json.dumps(data2, indent=2, sort_keys=True)
	data4 = json2html.convert(json = data3)
	return data4

if __name__ == "__main__":
    app.run(debug=True)