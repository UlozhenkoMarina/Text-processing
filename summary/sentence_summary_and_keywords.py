
import nltk
nltk.download()
#from nltk import text
from nltk.text import TextCollection
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

text1 = "The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania. NLTK includes graphical demonstrations and sample data. It is accompanied by a book that explains the underlying concepts behind the language processing tasks supported by the toolkit, plus a cookbook. NLTK is intended to support research and teaching in NLP or closely related areas, including empirical linguistics, cognitive science, artificial intelligence, information retrieval, and machine learning. NLTK has been used successfully as a teaching tool, as an individual study tool, and as a platform for prototyping and building research systems. There are 32 universities in the US and 25 countries using NLTK in their courses. NLTK supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning functionalitiest"

sentences = sent_tokenize(text1)
sent_num = 2
sent_scores = []
for i in sentences: 
  word_score_sum = 0
  for j in list(word_tokenize(i)):
    if j not in stopwords.words('english'):
      word_score_sum += TextCollection(text1).tf_idf(term = j, text = text1 )
  sent_scores.append(word_score_sum)
res = ""
while sent_num > 0 and sent_num <len(sentences):
  res += " " + sentences[sent_scores.index(max(sent_scores))]
  sent_scores[sent_scores.index(max(sent_scores))] = min(sent_scores) - 1
  sent_num -= 1
print("result: ", res)
print()
words_num = 4
words_list = word_tokenize(text1)
words = list(set(words_list).difference(set(stopwords.words('english'))))
new_words= [word for word in words if word.isalnum()]
words = new_words
words_score = []
for word in words:
  words_score.append(TextCollection(text1).tf(term = word, text = text1 ))
keywords = ""
while words_num > 0 and words_num < len(words_list):
  keywords +=" " + words[words_score.index(max(words_score))] + ","
  words_score[words_score.index(max(words_score))] = min(words_score) - 1
  words_num -= 1
keywords = keywords[0 : -1]
print("keywords: ", keywords)
  






  


