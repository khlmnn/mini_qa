"""
mini_qa.py
~~~~~~~~~~

Toy question-answering program.
"""

#### Library imports

# standard library
from collections import defaultdict
import pickle as pickle
import json
import re
import sys
from xml.etree import ElementTree

from google import search


#### Config

try:
    import config
except ImportError:
    print ("Failed to import config.  Enter configuration data into\n"
           "config.py.example, and rename it to config.py.")
    sys.exit()

#### Parameters used to score results returned from the Google-based
#### system
CAPITALIZATION_FACTOR = 2.2
QUOTED_QUERY_SCORE = 5
UNQUOTED_QUERY_SCORE = 2


def pretty_qa(question, num=10):
    """Wrapper for the `qa` function.  `pretty_qa` queries Google to
    answer `question`. Only the top `num` are printed (with scores in
    parentheses).

    """
    print("\nQ: "+question)
    for (j, (answer, score)) in enumerate(qa(question)[:num]):
        print("%s. %s (%s)" % (j+1, answer, score))

def qa(question):
    """Return a list of tuples whose first entry is a candidate answer to
    `question`, and whose second entry is the score for that answer.
    The tuples are ordered in decreasing order of score.

    """
    answer_scores = defaultdict(int)
    for query in rewritten_queries(question):
        for summary in search(query.query):
            for sentence in sentences(summary):
                for ngram in candidate_answers(sentence, query.query):
                    answer_scores[ngram] += ngram_score(
                        ngram, query.score)
    ngrams_with_scores = sorted(iter(answer_scores.items()), 
                                key=lambda x: x[1], 
                                reverse=True)
    return [(" ".join(ngram), score) 
            for (ngram, score) in ngrams_with_scores]

def rewritten_queries(question):
    """Return a list of RewrittenQuery objects, containing the search
    queries (and corresponding weighting score) generated from
    `question`.

    """
    rewrites = [] 
    tq = tokenize(question)
    verb = tq[1] # the simplest assumption, something to improve
    rewrites.append(
        RewrittenQuery("\"%s %s\"" % (verb, " ".join(tq[2:])), 
                       QUOTED_QUERY_SCORE))
    for j in range(2, len(tq)):
        rewrites.append(
            RewrittenQuery(
                "\"%s %s %s\"" % (
                    " ".join(tq[2:j+1]), verb, " ".join(tq[j+1:])),
                QUOTED_QUERY_SCORE))
    rewrites.append(RewrittenQuery(" ".join(tq[2:]), UNQUOTED_QUERY_SCORE))
    return rewrites

def tokenize(question):
    """Return a list containing a tokenized form of `question`.  Works by
    lowercasing, splitting around whitespace, and stripping all
    non-alphanumeric characters.

    """
    return [re.sub(r"\W", "", x) for x in question.lower().split()]


class RewrittenQuery():
    """Given a question we rewrite it as a query to send to Google.
    Instances of the RewrittenQuery class are used to store these
    rewritten queries.  Instances have two attributes: the text of the
    rewritten query, which is sent to Google; and a score, indicating
    how much weight to give to the answers.  The score is used because
    some queries are much more likely to give highly relevant answers
    than others.

    """

    def __init__(self, query, score):
        self.query = query
        self.score = score


def sentences(summary):
    """Return a list whose entries are the sentences in the
    BeautifulSoup.BeautifulSoup object `summary` returned from Google.
    Note that the sentences contain alphabetical and space characters
    only, and all punctuation, numbers and other special characters
    have been removed.

    """
    text = remove_spurious_words(text_of(summary))
    sentences = [sentence for sentence in text.split(".") if sentence]
    return [re.sub(r"[^a-zA-Z ]", "", sentence) for sentence in sentences]

def text_of(soup):
    """Return the text associated to the BeautifulSoup.BeautifulSoup
    object `soup`.

    """
    return ''.join([str(x) for x in soup.findAll(text=True)])

def remove_spurious_words(text):
    """Return `text` with spurious words stripped.  For example, Google
    includes the word "Cached" in many search summaries, and this word
    should therefore mostly be ignored.

    """
    spurious_words = ["Cached", "Similar"]
    for word in spurious_words:
        text = text.replace(word, "")
    return text

def candidate_answers(sentence, query):
    """Return all the 1-, 2-, and 3-grams in `sentence`.  Terms appearing
    in `query` are filtered out.  Note that the n-grams are returned
    as a list of tuples.  So a 1-gram is a tuple with 1 element, a
    2-gram is a tuple with 2 elements, and so on.

    """
    filtered_sentence = [word for word in sentence.split() 
                         if word.lower() not in query]
    return sum([ngrams(filtered_sentence, j) for j in range(1,4)], [])

def ngrams(words, n=1):
    """Return all the `n`-grams in the list `words`.  The n-grams are
    returned as a list of tuples, each tuple containing an n-gram, as
    per the description in `candidate_answers`.

    """
    return [tuple(words[j:j+n]) for j in range(len(words)-n+1)]

def ngram_score(ngram, score):
    """Return the score associated to `ngram`.  The base score is
    `score`, but it's modified by a factor which is
    `CAPITALIZATION_FACTOR` to the power of the number of capitalized
    words.  This biases answers toward proper nouns.

    """
    num_capitalized_words = sum(
        1 for word in ngram if is_capitalized(word)) 
    return score * (CAPITALIZATION_FACTOR**num_capitalized_words)

def is_capitalized(word):
    """Return True or False according to whether `word` is capitalized.

    """
    return word == word.capitalize()


if __name__ == "__main__":
    pretty_qa("Who ran the first four-minute mile?")
    pretty_qa("Who makes the best pizza in New York?")
    pretty_qa("Who invented the C programming language?")
    pretty_qa("Who wrote the Iliad?")
    pretty_qa("Who caused the financial crash of 2008?")
    pretty_qa("Who caused the Great Depression?")
    pretty_qa("Who is the most evil person in the world?")
    pretty_qa("Who wrote the plays of Wiliam Shakespeare?")
    pretty_qa("Who is the world's best tennis player?")
    pretty_qa("Who is the richest person in the world?")
