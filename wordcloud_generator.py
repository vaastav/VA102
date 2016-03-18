from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

text = ""
with open('cleaned_items.csv','rU') as reviews:
	reader = csv.DictReader(reviews)
	for row in reader:
		text += row['Cleaned_Review'] + " "

wordcloud = WordCloud(max_font_size=40,relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('reviews.png',bbox_inches='tight',pad_inches=0)

text = ""
with open('keyworded_items.csv','rU') as reviews:
	reader = csv.DictReader(reviews)
	for row in reader:
		text += row['Keywords'].replace(']',' ').replace('[',' ') + " "

wordcloud = WordCloud(max_font_size=40,relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('keywords.png',bbox_inches='tight',pad_inches=0)
