import csv
import urllib
import json

def call_nltk_api(text):
	labs = []
	probs_pos = []
	probs_neg = []
	probs_neu = []
	for review in text:
		data = urllib.urlencode({"text":review})
		u = urllib.urlopen("http://text-processing.com/api/sentiment/",data)
		obj = json.loads(u.read())
		labs += [obj["label"]]
		probs_pos += [obj["probability"]["pos"]]
		probs_neg += [obj["probability"]["neg"]]
		probs_neu += [obj["probability"]["neutral"]]

def readfile(filename):
	inf = open(filename,'rU')
	filereader = csv.DictReader(inf,delimiter=',')
	text = [row["Cleaned_Review"] for row in filereader]
	print len(text)
	call_nltk_api(text)

def main():
	readfile("cleaned_items.csv")

if __name__ == '__main__':
	main()
