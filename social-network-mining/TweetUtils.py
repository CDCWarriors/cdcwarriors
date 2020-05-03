import re
import Utils

ANXIETY_FILTERS_FILE = "./data/mental_anxiety_filters.txt" 
COVID_FILTER_FILE = "./data/covid_filter.txt" 

def process_tweet(tweet_text):
    tweet_text = tweet_text.lower() # convert text to lower-case
    tweet_text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet_text) # remove URLs
    tweet_text = re.sub('@[^\s]+', '', tweet_text) # remove usernames
    tweet_text = re.sub('@[^\s]+', '', tweet_text)
    tweet_text = re.sub('rt ', '', tweet_text) # trim 'rt ' string from begining
    # tweet_text = re.sub(r'#([^\s]+)', r'\1', "et_text) # remove the # in #hashtag
    return tweet_text

def get_anxiety_words():
    return Utils.get_words_from_file(ANXIETY_FILTERS_FILE)

def get_covid_words():
    return Utils.get_words_from_file(COVID_FILTER_FILE)
    
def is_anxiety(tweet_text):
    words = get_anxiety_words()
    return Utils.has_word_in_text(tweet_text, words)

def is_covid(tweet_text):
    words = get_covid_words()
    return Utils.has_word_in_text(tweet_text, words)


if __name__ == "__main__":
    assert process_tweet("www.google see") == " see"
    assert is_anxiety("I am Worried") == True
    assert is_covid("covid19 isvery dangerous") == True
    assert is_covid("corona is bad") == False