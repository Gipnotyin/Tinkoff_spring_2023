string = input()
dct = dict()
for c in 'sheriff':
    dct[c] = 0
for c in string:
    if c in 'sheriff':
        dct[c] += 1

dct['f'] //= 2
print(min(dct.values()))
