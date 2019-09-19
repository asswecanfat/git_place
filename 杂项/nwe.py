R = [i*2+8 for i in range(20)]
S = [i**2 for i in range(10)]
new = []
n = 0
i = 0
while i < len(R):
    if n >= len(S):
        new.append(R[i])
        i += 1
    else:
        if R[i] >= S[n]:
            new.append(S[n])
            n += 1
        else:
            new.append(R[i])
            i += 1

print(new)


