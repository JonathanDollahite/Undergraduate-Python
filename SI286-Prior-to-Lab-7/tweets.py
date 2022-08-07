import gzip
import matplotlib.pyplot as plt #this one is a returner
from wordcloud import WordCloud   # new for WordCloud

with gzip.open('tweets_big_file.txt.gz', 'rt', errors='replace') as f:
    tweets = f.readlines()

search_term = input('Enter your search term: ')
#print(lines[26])

while search_term != 'quit':
    search_term = ' ' + search_term + ' '
    search_term = search_term.lower()
#tweets is list of tweets
#query is a string search query
#return how many tweets that query appears in
    def tweet_count(tweets, query):
        count = 0
        #query = input('Enter your query: ')
        for tweet in tweets:
            if query in tweet:
                count = count + 1
        return count

#clean up tweet
    def clean_tweet(tweet, query):
        tweet = tweet.lower()
        tweet = tweet.replace(query, ' ')
        tweet = tweet.replace('!', ' ')
        tweet = tweet.replace('?', ' ')
        tweet = tweet.replace('.', ' ')
        tweet = tweet.replace(',', ' ')
        tweet = tweet.replace(';', ' ')
        tweet = tweet.replace(':', ' ')
        tweet = tweet.replace('&amp', ' ')
        tweet = tweet.replace('https', ' ')
        #print(tweet)
        return tweet

    #same arguments as tweet_count
    #return a single string which concatenates all tweets that contain query string
    def build_doc(tweets, query):
        concat = ''
        for tweet in tweets:
            if query in tweet:
                #print(tweet)
                cleaned_tweet = clean_tweet(tweet, query)
                #print(cleaned_tweet)
                concat = concat + cleaned_tweet
        return concat

    doc = build_doc(tweets, search_term)
    if doc == '':
        search_term = input('No matches, please try another query: ')
    else:
        print('Seen: ', tweet_count(tweets, search_term))
        #print('Concat: ', build_doc(tweets, search_term))

        #The cloud!
        cloud = WordCloud(width=480, height=480, margin=0).generate(doc)    # 'doc' is the constructed tweet string

        # Now popup the display of our generated cloud image.
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.show()
        search_term = input('Enter your search term: ')


quit()
