from nltk.tokenize import sent_tokenize,word_tokenize

example_text = "Hello there, how are you doing today? The weather is great and python is awesome. The sky is blue"

print(sent_tokenize(example_text))
print(word_tokenize(example_text))