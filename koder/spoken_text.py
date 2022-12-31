from nltk import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = {"an", "the", "a"}
stop_words.update(
    ["-", ".", ",", '"', "'", "?", "!", ":", ";", "(", ")", "[", "]", "{", "}"]
)  # remove it if you need punctuation


def stem_words(sentence):
    stemmed_words = []
    for word in sentence.split():
        stemmed_word = stemmer.stem(word)
        stemmed_words.append(stemmed_word)
    return " ".join(stemmed_words)


def remove_stop_words(text):
    return " ".join([i for i in word_tokenize(text) if i not in stop_words])


def clean(spoken_text):
    return spoken_text.strip().lower()


def sanitize(spoken_text):
    return remove_stop_words(clean(spoken_text))
