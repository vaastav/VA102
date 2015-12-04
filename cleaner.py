import csv

def clean(review):
	return str(review).replace("<p>","").replace("</p>","").replace("<br>\n"," ").replace("<br>","").replace("&amp","&")

def readfile(filename):
	inf = open(filename,'rU')
	filereader = csv.DictReader(inf,delimiter=',')
	test = [clean(row['review']) for row in filereader]
	#print test
	print len(test)
	inf.close()
	with open(filename,'rb') as fin, open('cleaned_items.csv', 'wb') as fout:
		reader = csv.reader(fin,lineterminator='\n')
		writer = csv.writer(fout,lineterminator='\n')
		writer.writerow(next(reader) + ["Cleaned_Review"])
		for row, val in zip(reader,test):
			writer.writerow(row + [val])



def main():
	readfile("items.csv")

if __name__ == '__main__':
	main()
