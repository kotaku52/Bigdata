#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


class TextClassfilter():
    def __init__(self, Classfiler=MultinomialNB()):
        self.classfiler = Classfiler
        self.vectorize = CountVectorizer(analyzer="word", ngram_range=(1, 10), max_features=40000)

    def feartures(self, x):
        return self.vectorize.transform(x)

    def fit(self, x, y):
        self.vectorize.fit(x)
        self.classfiler.fit(self.feartures(x), y)

    def predict(self, x):
        return self.classfiler.predict(self.feartures([x]))

    def score(self, X, y):
        return self.classfiler.score(self.feartures(X), y)
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
