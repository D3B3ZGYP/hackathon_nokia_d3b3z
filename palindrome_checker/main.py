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
    diff_charachters = []
    num_of_diff_charachters = 0
    if i == i[::-1]:
        for j in i:
            if not (j in diff_charachters):
                diff_charachters += j
                num_of_diff_charachters += 1
        print(f"YES, {num_of_diff_charachters}")
        continue
    else:
        print("NO, -1")
