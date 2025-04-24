def ReverseWord(sentence):
    return" ".join(word[::-1] for word in sentence.split())
sentence = "MY Name is Anant Chauhan"
print(ReverseWord(sentence))
