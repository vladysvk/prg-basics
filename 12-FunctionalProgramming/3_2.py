sentence = 'I completely agree with you'
sentence = sentence.split()
result = list(map(lambda word: len(word) , sentence))
print(result)