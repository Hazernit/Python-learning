import nltk

nltk.download('punkt')

sentence = """We cannot solve our problems 
with the same thinking 
we used when we created them."""

tokens = nltk.word_tokenize(sentence)
print(tokens)
