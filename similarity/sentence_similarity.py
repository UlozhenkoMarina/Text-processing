#import nltk
#nltk.download()
from nltk.corpus import wordnet
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# sentence1 = input("Enter first string: ").lower() 
# sentence2 = input("Enter second string: ").lower() 
sentence1 ="I love funny books"
sentence2 ="Calm is a funny book, which I like"
  
sentence1_inform_words = word_tokenize(sentence1)  
sentence2_inform_words = word_tokenize(sentence2) 
  
sw = stopwords.words('english')  
l1 =[];l2 =[] 
s1 =[];s2 =[]
  
sentence1_inform_words = {w for w in sentence1_inform_words if not w in sw}  
sentence2_inform_words = {w for w in sentence2_inform_words if not w in sw} 
rvector = sentence1_inform_words.union(sentence2_inform_words)  
for w in rvector: 
    if len((sentence1_inform_words).difference({w}.union(set(wordnet.synsets(w))))) < len(sentence1_inform_words): 
      l1.append(1)
    else: 
      l1.append(0) 
    if  len((sentence2_inform_words).difference({w}.union(set (wordnet.synsets(w))))) < len({w}.union(set (wordnet.synsets(w)))): 
      l2.append(1) 
    else: 
      l2.append(0) 

for w in rvector: 
    if w in sentence1_inform_words: s1.append(1)
    else: s1.append(0) 
    if w in sentence2_inform_words: s2.append(1) 
    else: s2.append(0) 


def cousine (rvector, l1, l2):  
  # cosine formula  
  c = 0
  for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
  return  c / float((sum(l1)*sum(l2))**0.5) 

print("similarity: ", cousine(rvector, l1, l2))
print("similarity: ", cousine(rvector, s1, s2))




