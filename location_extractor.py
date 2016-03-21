import csv

countries = []
with open('classified_items.csv') as inf:
	reader = csv.reader(inf)
	row0 = next(reader)
	for row in reader:
		if len(row[6].split(',')) == 1:
			countries += ['']
		else:
			countries += [row[6].split(',')[1]]

with open('classified_items.csv','r') as inf, open('classified_items_country.csv','w') as outf:
	reader = csv.reader(inf)
	writer = csv.writer(outf)
	writer.writerow(next(reader) + ['Country'])
	for row,country in zip(reader,countries):
		writer.writerow(row + [country])	
