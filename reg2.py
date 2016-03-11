test = """abc def-ghi jkl abc
abc"""

def calculate_word_frequency(s):
   
    words = s.split()
    freq  = {}
    for word in words:
        if freq.has_key(word):
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

m={}
m=calculate_word_frequency(test)
print m
