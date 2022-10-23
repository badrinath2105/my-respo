asciidict = dict()
alfapetTeller = range(97,123)
for i in alfapetTeller:
    asciidict[str(i)] = chr(i)
print(asciidict)
asciidict[chr(i)] = i


import string
d = {c: ord(c) for c in string.ascii_lowercase}  
print(d)