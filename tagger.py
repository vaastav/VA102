from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag, map_tag
import nltk
import csv

keywordTags = ['ADJ','ADV','NOUN','NUM','VERB']

def isKeywordTag(tag):
	return tag in keywordTags

def find_keywords(review):
	text = word_tokenize(review.decode("utf8"))
	tagged_review = pos_tag(text)
	simplified_tagged_review = [(word,map_tag('en-ptb','universal',tag)) for word, tag in tagged_review]
	keywords = []
	for word,tag in simplified_tagged_review:
		if isKeywordTag(tag):
			keywords += [word]
	return keywords

def readfile(filename):
	inf = open(filename,'rU')
	filereader = csv.DictReader(inf,delimiter=',')
	reviews = [row["Cleaned_Review"] for row in filereader]
	
	keywords = []

	for review in reviews:
		lok = [word.encode("utf8") for word in find_keywords(review)]
		
		keywords += [lok]

	inf.close()
	with open(filename,'rb') as fin, open('keyworded_items.csv','wb') as fout:
		reader = csv.reader(fin,lineterminator='\n')
		writer = csv.writer(fout,lineterminator='\n')
		writer.writerow(next(reader) + ["Keywords"])
		for row,val in zip(reader,keywords):
			writer.writerow(row + [' '.join(val)])


def main():
	readfile("cleaned_items.csv")

if __name__ == '__main__':
	main()
