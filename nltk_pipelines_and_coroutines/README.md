### Coroutines and NLTK and Pipelines, Oh My! ###

A recent work Slack conversation:


    Colleague: have you used coroutines before?

    Me: Nope! What's the use case?

    Colleague: speeding up NLP pipelines (like in this article: https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/)

    Me: **looks at article** **breaks out into cold sweat** **head explodes**


Seriously though, this really grabbed my interest. I've never tried NLTK or using coroutines (let alone both), so I wanted to jot down some notes to myself to try to retain what I was able to learn. These are those notes! 


If you want to follow along, this look like:

    I.) My attempts to understand [this article](https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/), hereafter referred to as _The NLP Article_.

    II.) Revisiting the original for loop in _The NLP Article_.

    III.) Concluding Thoughts: Maybe more questions than answers?
    
 
    I.) My attempts to understand [this article](https://nlpforhackers.io/building-a-nlp-pipeline-in-nltk/), hereafter referred to as _The NLP Article_.
        * what's a couroutine anyway?
        * I reference [Dave Beazley's "A Curious Course on Coroutines and Concurrency"](http://www.dabeaz.com/coroutines/Coroutines.pdf):
            * Sections:

                * slides 1 - 14     (Intro)
                * slides 15 -23     (Refresher on generators)
                * slides 24 - 28    (Here we goooooooo!)
                * slides 34 - 41    *IMPORTANT* (producers, filters (intermediate stages), sinks)

                * Python 3 versions of some of DB's sample code (found under `curious_code_py3/`)

        * okay, now that I think I have my head around that, what does this code look like?
            * explanation of requisite nesting

    II.) Revisiting the original for loop in _The NLP Article_.
        * Class-based approach:
            `NLTKPipeline/NLTKPipeline.py`
        * what's this get us?
        * what about performance?

    III.) Concluding Thoughts: Maybe more questions than answers?
