import os, sys, errno
import subprocess
import re
import itertools
import nltk
from nltk.stem import PorterStemmer
import bs4

sys.path.append("modules")
import questionContentSelector
import questionFromSentence
import coref
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
  path_to_article = sys.argv[1]
  num_questions = int(sys.argv[2])
  f= open("ques.txt","w")

  article_content = coref.process(path_to_article)

  selected_content = questionContentSelector.process(article_content)

  questions = questionFromSentence.process(selected_content)

  questions = questions[:num_questions]
  for question in questions:
    f.write(question+"\n")
  f.close()

