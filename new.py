import json

with open('sample.json') as json_data:
	data = json.load(json_data)
	fo = open("output1.sh","wb")
	fo.write("sudo apt-get install python-pip")
	fo.write("\n")
	for r in data['Dependencies']:
		fo.write("pip install -U " + r['name'] + " "+ r['version'])
		fo.write("\n")
		fo.close	
