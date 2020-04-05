import nltk


from FunctionChain import FunctionChain


class NLTKPipeline:
    """
    A Class-based attempt at a configurable pipeline.

    For example, instead of this:

        def process_texts(texts):
            for text in texts:
                sentences = nltk.sent_tokenize(text)
                for sentence in sentences:
                    words = nltk.word_tokenize(sentence)
                    tagged_words = nltk.pos_tag(words)
                    ne_tagged_words = nltk.ne_chunk(tagged_words)
                    print(ne_tagged_words)

   
    One would do this:

        pipeline = NLTKPipeline(
            texts, 
            steps=[
                nltk.word_tokenize, 
                nltk.pos_tag, 
                nltk.ne_chunk
            ],
            sink=print,
        )

        pipeline.run()

    
    The final function in the pipeline (`print`, in this case) is referred to as the `sink`. 
    """

    def __init__(self, texts, steps=None, sink=print):
        self.texts = texts
        if steps and isinstance(steps, FunctionChain):
            self.fn_chain = steps
        elif steps:
            self.fn_chain = FunctionChain(*steps)
        else:
            raise TypeError(
                """Please pass either an iterable of functions, or an instance of FunctionChain obj to `steps`.""",
            )
        self.sink = sink

    def run(self):
        for t in self.texts:
            for sentence in nltk.sent_tokenize(t):
                self.sink(self.fn_chain(sentence))
