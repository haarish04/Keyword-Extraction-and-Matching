def extract_POS(sample_doc):
    res=[]
    for chk in sample_doc.noun_chunks:
        tmp=""
        for tkn in chk:
            if (tkn.pos_ in ['NOUN','PROPN','ADJ'] ):
                if (not(tkn.is_stop) and not(tkn.is_punct)):
                    tmp = tmp + tkn.text.lower() + " "
        if(tmp.strip()!=""):
            res.append(tmp.strip())
    return list(dict.fromkeys(res))

key_POS=extract_POS(ans_doc)
print(key_POS)
print(type(ans_doc))

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('distilbert-base-nli-mean-tokens')
doc_embedding = model.encode([key])
candidate_embeddings = model.encode(key_POS)

