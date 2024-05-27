with open('./input.txt', 'r') as f:
    input = f.read()

l = []
for i in input.lower().split("\n"):
    if str.isalnum(i):
        l.append(i)
        continue

    word = ""
    for j in i:
        if str.isalnum(j):
            word += j
    l.append(word)

l.pop()

for i in l:
    if i == i[::-1]:
        print(f"YES, {len(set(i))}")
    else:
        print("NO, -1")
