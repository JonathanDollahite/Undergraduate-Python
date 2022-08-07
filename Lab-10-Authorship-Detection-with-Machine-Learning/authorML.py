import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
stops = stopwords.words('english')
import si286
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.feature_extraction import DictVectorizer as DV
from sklearn.naive_bayes import MultinomialNB as MNB

def count_words(text):
	"""counts the words in a given string and returns a dictionary with the words as the key and the frequency of occurence as the value"""
	counter = dict()
	for word in text:
		word = word.lower()
		if word not in stops:
			if word in counter:
				counter[word] = counter[word] + 1
			else:
				counter[word] = 1
		if word in stops:
			continue
	return counter

#------------------------------------------------
#------------------------------------------------

# Creates dictionaries of authors and counts with author names and words with their counts in different text samples to train
authors = []
counts = []
line_list = []
fh = open('train-snippets.tsv')
for line in fh:
	line_list.append(line)
	tokens = nltk.word_tokenize(line)
	authors.append(tokens[0])
	Piper = count_words(tokens)
	counts.append(Piper)

# Does the same as previous, but for the test smaples
authors2 = []
counts2 = []
line_list2 = []
f = open('test-snippets.tsv')
for line in f:
	line_list2.append(line)
	tokens2 = nltk.word_tokenize(line)
	authors2.append(tokens2[0])
	Piper2 = count_words(tokens2)
	counts2.append(Piper2)

# Uses Label sklearn to hand off my dictionaries for analysis.
LE = LE()
LE.fit(authors)
train_y = LE.transform(authors)

v = DV()
v.fit(counts)
train_x = v.transform(counts)

classifier = MNB()
classifier.fit(train_x, train_y)

t = DV()
t.fit(counts2)
test_x = v.transform(counts2)
predictions = classifier.predict(test_x)
print(predictions)
print(LE.inverse_transform(predictions))

print(authors2)
si286.accuracy(LE.inverse_transform(predictions), authors2)
