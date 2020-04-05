from multiprocessing import Pool


import nltk


from sampledata import texts


# https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/
def process_text(text):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        ne_tagged_words = nltk.ne_chunk(tagged_words)
        print(ne_tagged_words)


for text in texts:
    process_text(text)
