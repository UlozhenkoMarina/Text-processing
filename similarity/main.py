#import nltk
#nltk.download()
from nltk.corpus import wordnet
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer

  
# sentence1 = input("Enter first string: ").lower() 
# sentence2 = input("Enter second string: ").lower() 
sentence1 ="I love funny books"
sentence2 ="Calm is a funny book, which I like"
sw = stopwords.words('english')  

def cousine(sentence1, sentence2):  
  sentence1_inform_words = word_tokenize(sentence1)  
  sentence2_inform_words = word_tokenize(sentence2) 
  
  l1 =[];l2 =[] # for cousine with synonims 
  s1 =[];s2 =[]

  stemmer = PorterStemmer()
  sentence1_inform_words = {w for w in sentence1_inform_words if not w in sw}   
  sentence2_inform_words = {w for w in sentence2_inform_words if not w in sw} 
  # for using stemmer on the first step of cosine similarity like in Jaccard similarity
  #sentence1_inform_words = {stemmer.stem(w) for w in sentence1_inform_words if not w in sw}   
  #sentence2_inform_words = {stemmer.stem(w) for w in sentence2_inform_words if not w in sw} 

  #rvector is a union of the unique words in both sentences
  #l1 and l2 are vectors for sentence1 and sentence2 respectively and are formed in next way
  #if word appear in the sentence we set 1 in the respective position in the vector.
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

  #s1 and s2 are vectors for sentence1 and sentence2 respectively and are formed in next way
  #if word or some of its synonims appear in the sentence we set 1 in the respective position in the vector.
  for w in rvector: 
    if w in sentence1_inform_words: s1.append(1)
    else: s1.append(0) 
    if w in sentence2_inform_words: s2.append(1) 
    else: s2.append(0) 
  return cosine_metrics(rvector, l1, l2)

# for Jaccard similarity
def Jaccard(sentence1, sentence2):
  stemmer = PorterStemmer()
  sentence1_Jaccard = set(word_tokenize(sentence1)) 
  sentence2_Jaccard = set(word_tokenize(sentence2) ) 
  sentence1_Jw = {stemmer.stem(w) for w in sentence1_Jaccard if not w in sw}
  sentence2_Jw = {stemmer.stem(w) for w in sentence2_Jaccard if not w in sw}
  return len(sentence1_Jw.intersection(sentence2_Jw))/len(sentence1_Jaccard.union(sentence2_Jaccard))
    

def cosine_metrics (rvector, l1, l2):  
  # cosine formula  
  c = 0
  for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
  return  c / float((sum(l1)*sum(l2))**0.5) 

print("cosine similarity with using synonims: ", cosine(sentence1, sentence2))
print("cosine similarity without using synonims: ", cosine(sentence1, sentence2))

print("Jaccard similarity: ", Jaccard(sentence1, sentence2))





