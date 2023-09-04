size = int(input())
seq1 = input()
seq2 = input()
l, r = 0, size - 1
while l < size - 1 and seq1[l] == seq2[l]:
    l += 1

while r > 0 and seq1[r] == seq2[r]:
    r -= 1

if r == 0 and l == size - 1:
    print('YES')
else:
    dct = dict()
    for i in range(l, r + 1):
        dct[seq1[i]] = dct.get(seq1[i], 0) + 1
    if dct.get(seq2[l], 'err') != 'err':
        dct[seq2[l]] -= 1
        if dct[seq2[l]] == 0:
            del dct[seq2[l]]
    flag = False
    for index in range(l + 1, r + 1):
        if seq2[index - 1] <= seq2[index]:
            if dct.get(seq2[index], 'err') != 'err':
                dct[seq2[index]] -= 1
                if dct[seq2[index]] == 0:
                    del dct[seq2[index]]
            else:
                flag = True
                break
        else:
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')
