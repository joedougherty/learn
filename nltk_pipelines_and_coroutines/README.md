### Coroutines and NLTK and Pipelines, Oh My! ###

A recent work Slack conversation:


    Colleague: have you used coroutines before?

    Me: Nope! What's the use case?

    Colleague: speeding up NLP pipelines (like in this article: https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/)

    Me: **looks at article** **breaks out into cold sweat** **head explodes**


Seriously though, this really grabbed my interest. I've never tried NLTK or using coroutines (let alone both), so I wanted to jot down some notes to myself to try to retain what I was able to learn. These are those notes! 


If you want to follow along, this will look like:


**I.) My attempts to understand [this article](https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/), hereafter referred to as _The NLP Article_.**

**II.) Revisiting the original `for` loop in _The NLP Article_.**

**III.) Concluding Thoughts: Maybe more questions than answers?**

---

## I.) My attempts to understand _The NLP Article_. ##

**Note:** _Code displayed here will be modified to target Py3 even if the original source targets Py2._


The article opens with a pretty clear example of a text pipeline driven by a `for` loop:

    for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        ne_tagged_words = nltk.ne_chunk(tagged_words)
        print(ne_tagged_words)

    [Source: https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/]

The article suggests we can build a more reusable pipeline with coroutines. But hey, what's a coroutine anyway?


For better or for worse, I'm not going to attempt to provide a new explanation here. There's already plenty of good material in [Dave Beazley's "A Curious Course on Coroutines and Concurrency"](http://www.dabeaz.com/coroutines/Coroutines.pdf). I realize this resource is now over a decade old, but I wasn't able to find any more authoritative documentation. Plus, Dave's materials are excellent. I haven't run into any problems running his code.


Here's the ground I had to cover before understanding the coroutine example from _The NLP Article_.

**Sections:**

* Slides 1 - 14     (Intro)
* Slides 15 -23     (Refresher on generators)
* Slides 24 - 28    (Here we *goooooooo*!)
* Slides 34 - 41    **IMPORTANT!** ("producers", "filters" (intermediate stages), "sinks")

**Note:** _Python 3 versions of some of DB's sample code (can found under `curious_code_py3/`)_

 
Here are some things I did to convince myself I understood some parts of this.

I recreated the following components:

* The `coroutine` decorator (slide 27)
* The `grep` coroutine (slide 29)
* The `follow` producer (slide 38)
* The `printer` sink (slide 38)
* The `grep` filter (slide 41)

I hooked them up to understand the data flow. I noticed that when I ran the follow routine on line 41, there was no ouput on my console. Looking at the code comment, I see the call to `.seek(0,2)` reads from the end of the file.

In order to convince myself this was working as expected, I wrote a function to write some new data to the log file that `follow` was reading from. 

    import time


    def slow_write(from_file, to_file, pause=1):
    with open(from_file, "r") as source:
        source_lines = source.readlines()

    for line in source_lines:
        with open(to_file, "a") as dest:
            dest.write(line)
        time.sleep(pause)


I had the two processes open in separate tabs and I was able to what the filtered lines get picked up by `grep` as they were coming in live.


I'm _certain_ there's more one can do in order to get the gist of coroutines, but this works for me for now.


Using the terminology above, I can now identify a few parts of the pipleline as proposed by _The NLP Article_.


* `source` is the producer
* `sent_tokenize_pipeline`, `word_tokenize_pipeline`, `pos_tag_pipeline`, `ne_chunk_pipeline`: are the filters
* `printer` is the sink


Most importantly, I have a somewhat easier time seeing that flow when I look at this:

    #
    # Now I can see that the pipeline goes:
    #   sent_tokenize_pipeline -> word_tokenize_pipeline -> pos_tag_pipeline -> ne_chunk_pipeline ( -> printer )
    #
    source(texts, targets=[
        sent_tokenize_pipeline(targets=[
            word_tokenize_pipeline(targets=[
                pos_tag_pipeline(targets=[
                    ne_chunk_pipeline(targets=[printer()]),
                ])
            ])
        ])
    ])

    [Source: https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/]



## II.) Revisiting the original `for` loop in _The NLP Article_. ##


The very first question posed by the article is: "_Wouldn’t it be nice to make this a bit more reusable?_"


The coroutine-based solution we've been looking at is, of course, the solution prescribed. 

Here's a small class I whipped up that tries to achive the same functional goals while being a little easier on the eyes.

Instead of this:

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


There is a sample implementation of this in `NLTKPipeline/NLTKPipeline.py`. See also: `NLTKPipeline/pipeline_example.py`.

It seems to me this might be more ergonomic from a developer's perspective.

**Q**: Is this as performant as using coroutines?

**A**: I have no idea!!! I *assume* not, but ¯\_(ツ)_/¯


## III.) Concluding Thoughts: Maybe more questions than answers? ##


