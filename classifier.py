from textblob.classifiers import NaiveBayesClassifier
import csv


train = []
with open('classifier-train.csv','r') as inf:
	reader = csv.DictReader(inf)
	for row in reader:
		if row['Review_Label'] != "":
			x = (row['Cleaned_Review'],row['Review_Label'])
			train += [x]
print("Starting classification...")
c1 = NaiveBayesClassifier(train)
print("Finished classification...")

test = []
with open('classifier-test.csv','r') as inf:
	reader = csv.DictReader(inf)
	for row in reader:
		x = (row['Cleaned_Review'],row['Review_Label'])
		test += [x]

accuracy = c1.accuracy(test)
