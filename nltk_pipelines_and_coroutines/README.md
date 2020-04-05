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



The article suggests we can build a more reusable pipeline with coroutines. But hey, what's a coroutine anyway?


For better or for worse, I'm not going to attempt to provide a new explanation here. There's already plenty of good material in [Dave Beazley's "A Curious Course on Coroutines and Concurrency"](http://www.dabeaz.com/coroutines/Coroutines.pdf). I realize this resource is now over a decade old, but I wasn't able to find any more authoritative documentation. Plus, Dave's materials are excellent. I haven't run into any problems running his code.


Here's the ground I had to cover before understanding the coroutine example from _The NLP Article_.

**Sections:**

* Slides 1 - 14     (Intro)
* Slides 15 -23     (Refresher on generators)
* Slides 24 - 28    (Here we goooooooo!)
* Slides 34 - 41    *IMPORTANT!* (producers, filters (intermediate stages), sinks)

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


I'm _certain_ there's more one can do in order to get the gist of coroutines, but this worked for me. 


## II.) Revisiting the original for loop in _The NLP Article_. ##

* Class-based approach:
    `NLTKPipeline/NLTKPipeline.py`
* what's this get us?
* what about performance?


## III.) Concluding Thoughts: Maybe more questions than answers? ##

