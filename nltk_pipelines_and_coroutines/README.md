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

## My attempts to understand _The NLP Article_. ##

**Note:** _Code displayed here will be modified to target Py3 even if the original source provides Py2 code._


The article opens with a pretty clear example of a text pipeline driven by a `for` loop:

    for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        ne_tagged_words = nltk.ne_chunk(tagged_words)
        print(ne_tagged_words)



The article suggests we can build a more reusable pipeline with coroutines. But hey, what's a coroutine anyway?


For better or for worse, I'm not going to attempt to provide a new explanation here. There's already plenty of good material in [Dave Beazley's "A Curious Course on Coroutines and Concurrency"](http://www.dabeaz.com/coroutines/Coroutines.pdf). I realize this resource is now over a decade old, but I wasn't able to find any more authoritative documentation. Plus, Dave's materials are excellent. I haven't run into any problems running his code.


Here's the ground I had to cover before understanding the coroutine example from _The NLP Article_.

**Sections:**

* Slides 1 - 14     (Intro)
* Slides 15 -23     (Refresher on generators)
* Slides 24 - 28    (Here we goooooooo!)
* Slides 34 - 41    *IMPORTANT!* (producers, filters (intermediate stages), sinks)

**Note:** _Python 3 versions of some of DB's sample code (can found under `curious_code_py3/`)_

* okay, now that I think I have my head around that, what does this code look like?
    * explanation of requisite nesting


## II.) Revisiting the original for loop in _The NLP Article_. ##

* Class-based approach:
    `NLTKPipeline/NLTKPipeline.py`
* what's this get us?
* what about performance?


## III.) Concluding Thoughts: Maybe more questions than answers? ##


