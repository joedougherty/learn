import nltk


from sampledata import texts


from NLTKPipeline import NLTKPipeline


pipeline = NLTKPipeline(
    texts, steps=[nltk.word_tokenize, nltk.pos_tag, nltk.ne_chunk,],
)

pipeline.run()
