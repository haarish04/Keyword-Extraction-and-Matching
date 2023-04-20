from sklearn.metrics.pairwise import cosine_similarity

top_n = 7
distances = cosine_similarity(doc_embedding, candidate_embeddings)
keywords = [key_POS[index] for index in distances.argsort()[0][-top_n:]]

def matching_keywords(stdlst,keylst):
        #matched list
        res=[]
        #unmatched list
        tmpres=[]
        for x in stdlst:
            if (x in keylst):
                res.append(x)
        return res

def dictionary_with_weights(words):

# nouns are given weightage as 9
# proper nouns are given weightage as 8.5
# adjectives are given weightage as 5

    categorized_words = {'9': [], '8.5': [], '5': []}
    for word in words:
        doc = nlp(word)
        pos = doc[0].pos_
        if pos in ['NOUN', 'PRON']:
            categorized_words['9'].append(word)
        elif pos == 'PROPN':
            categorized_words['8.5'].append(word)
        elif pos == 'ADJ':
            categorized_words['5'].append(word)
    return categorized_words

keywords_scores = dictionary_with_weights(keywords)
print(keywords_scores)

total=0
count=0
df['Keyword'] = None

for i in keywords_scores['9']:
  count+=1
total=total+count*9

count=0
for i in keywords_scores['8.5']:
  count+=1
total=total+count*8.5

count=0
for i in keywords_scores['5']:
  count+=1
total=total+count*5

scores=[]
count=1
for stud_doc in stud_ans:
  if(type(stud_doc)==float):
    stud_doc=str(stud_doc)
  stud_doc=nlp(stud_doc) 
  std_POS=extract_POS(stud_doc)
#then apply match function
  matched=matching_keywords(std_POS,keywords)
  stud_score=0
#percentage of matched keywords along with weights
  for i in matched:
    if i in keywords_scores['9']:
      stud_score=stud_score+9
    elif i in keywords_scores['8.5']:
      stud_score=stud_score+8.5
    elif i in keywords_scores['5']:
      stud_score=stud_score+5
  
  
  print("Evaluation of student:",count,"'s response:")
  print("Matching percentage with keywords:",len(matched)/len(keywords))
  print("Relative score using weights:",stud_score/total) 
  score=stud_score/total
  df['Keyword'][count-1] = score

  print("Matched Special POS keywords:", matched)
  print("\n")
  count+=1
