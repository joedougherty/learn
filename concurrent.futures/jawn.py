"""
https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor

THE GOAL:
========

Figure out if I can use something in concurrent.futures to parallelize the `check_link` function in WRDSCrawler.

PROPOSED ARCHITECTURE CHANGE:
=============================

# Why in the **butt** am I crafting this weird object hierarchy for LINKS of all things?

class Link(object):
    def __init__(url, context, text, **kwargs):
        self.url = url
        self.context = context
        self.text = text
        self.associated_set = ref_to_set

    def register(self):
        self.associated_set.add(self.url)


class BrokenLink(Link):
    def __init__(self, *args, **kwargs):
        super().__init__() # Ha that can't be right
        # ???


## for page in visit_queue:

def check_link(self, link):
    try:
        resp = self.session.get(link)
        if resp.status_code not in (200, 201, 300, 302):
            return BrokenLink(url=link, context=self.url, status_code=resp.status_code)
    except Exception as e:
        return ExceptionLink(url=link, context=self.url, exception_msg=e)
    return False 


def visit_page(self, page):
    gathered_links = gather_links(page, *etc)
    links_to_be_checked = filter(arbitrary_criteria, gathered_links)

    check_results = list()
    
    # It's just this portion that benefits from parallelization
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for result in executor.map(self.check_link, links_to_be_checked):
            check_results.append(result)

    for result_link in filter(lambda i: i != False, check_results):
        result_link.register()

"""
