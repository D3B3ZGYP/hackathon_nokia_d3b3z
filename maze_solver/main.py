import time
start = time.time()

with open('./input.txt', 'r') as f:
    input = f.read()

labs1 = input.split("B")[0].replace(" ","").split("\n")
labs1.pop(0)
labs1.pop(len(labs1)-1)
labs1.pop(len(labs1)-1)

labs2 = input.split("C")[0].replace(" ","").split("B")[1].split("\n")
labs2.pop(0)
labs2.pop(len(labs2)-1)
labs2.pop(len(labs2)-1)

labs3 = input.split("C")[1].replace(" ","").split("\n")
labs3.pop(0)
labs3.pop(len(labs3)-1)

print(labs1)
print(labs2)
print(labs3)


def maze_solver(map:list):
    pos = []
    answ = [""]
    check_around_nums = [-1,1]
    check_around_directions = ["U","L","D","R"]
    check_around_elements = []  # fent, bal, lent, jobb

    for i,e in enumerate(map):
        if e.count("S") > 0:
            pos.append([e.index("S"), i])
            break

    for i in pos:
        for k in check_around_nums:
            check_around_elements.append(map[i[1]+k][i[0]])
            check_around_elements.append(map[i[1]][i[0]+k])
        if check_around_elements.count(".") == 1:
            answ[0] += check_around_directions[check_around_elements.index(".")]
            pos[0]




maze_solver(labs1)

end = time.time()