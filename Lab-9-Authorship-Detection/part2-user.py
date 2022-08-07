import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
stops = stopwords.words('english')
import si286

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

Ashley = input('Please write a sentence: ')
Ashley_token = nltk.word_tokenize(Ashley)
Houtz = count_words(Ashley_token)

sim_list = []
for count in counts:
    simscore = si286.cosine_sim(Houtz,count)
    sim_list.append(simscore)

#found online
max_value = max(sim_list)
max_index = sim_list.index(max_value)
#

print('Most similar:', authors[max_index], line_list[max_index])
