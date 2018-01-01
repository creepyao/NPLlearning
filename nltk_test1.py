# -*- coding: utf-8 -*- 
from __future__ import division
from nltk.corpus import gutenberg
from nltk import FreqDist
from nltk.book import *

# print gutenberg.fileids()
'''
fd = FreqDist()
for word in gutenberg.words('austen-persuasion.txt'):
    fd[word] += 1
'''
'''
fd = FreqDist(gutenberg.words('austen-persuasion.txt'))
print fd.N()
print fd.B()
for word in sorted(fd.keys()):
    print word,fd[word]
'''

# text1.concordance("monstrous")
# text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
# text3.generate()  nltk3不支持


# print len(text3) / len(set(text3))

def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count, total):
    return 100 * count / total

fdist1 = FreqDist(text1)
print(fdist1)
print fdist1.most_common(50)
# dist1.plot(50,cumulative=True)
print len(fdist1.hapaxes())
