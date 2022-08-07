import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
stops = stopwords.words('english')

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

########################################################
########################################################

fh = open('short-snippets.tsv')
for line in fh:
	tokens = nltk.word_tokenize(line)
	Piper = count_words(tokens)
	print(tokens[0], Piper)
