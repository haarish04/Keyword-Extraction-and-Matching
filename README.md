# Keyword-Extraction-and-Matching

KeyBERT is a powerful library for keyword extraction and embedding generation. It can be used to perform keyword matching by comparing the embeddings of a given text and a set of keywords. Here we extract keywords, specifically --> nouns, proper nouns and adjective 


*************************************************************************************************************************************************************************

The main objective of this project is to extract keywords from a given answer text and is then matched with the student's answer text and a score is given to the student based on the matching of keywords between their answer and th eoriginal answer.

We have used sentence transformers and applied cosine similarity in order to extract keywords from the given original answer text

match keywords() function checks for keywords that are present in both the original answer and the student answer.

dictionary_with_weights(words) is used to assign weights to the POS 

  nouns are given weightage as 9
  proper nouns are given weightage as 8.5
  adjectives are given weightage as 5

Finally scoring is done and the student is given a score based on the presence of keywords and the score is appended to the dataframe (df)
