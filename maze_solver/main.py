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


def maze_solver(map:list):
    positions = []
    new_positions = []
    answ = ["S"]
    new_answ = []
    check_around_nums = [-1,1]
    check_around_pos_num = [[0,-1],[-1,0],[0,1],[1,0]]
    check_around_directions = ["U","L","D","R"]
    check_around_elements = []  # fent, bal, lent, jobb
    done = False

    for i,e in enumerate(map):
        if e.count("S") > 0:
            positions.append([e.index("S"), i])
            break

    while True:
        for i,e in enumerate(positions):
            for k in check_around_nums:
                check_around_elements.append(map[e[1]+k][e[0]])
                check_around_elements.append(map[e[1]][e[0]+k])

            new_answ.append(answ[i])

            if check_around_elements.count("G") == 1:
                new_answ[-1] += check_around_directions[check_around_elements.index("G")] + "G"
                return new_answ[-1]

            if check_around_elements.count(".") == 1:
                new_answ[-1] += check_around_directions[check_around_elements.index(".")]
                l = check_around_pos_num[check_around_directions.index(new_answ[-1][-1])]
                new_positions.append([e[0] + l[0], e[1] + l[1]])
                map_row = map[new_positions[-1][1]]
                map[new_positions[-1][1]] = map_row[:new_positions[-1][0]] + "F" + map_row[new_positions[-1][0]+1:]

            elif check_around_elements.count(".") > 1:
                new_pos_not_needed = True
                for i_,e_ in enumerate(check_around_elements):
                    if e_ == ".":
                        if new_pos_not_needed:
                            new_answ[-1] += check_around_directions[i_]
                            l = check_around_pos_num[check_around_directions.index(new_answ[-1][-1])]
                            new_positions.append([e[0] + l[0], e[1] + l[1]])
                            new_pos_not_needed = False
                        else:
                            new_positions.append(e)
                            new_answ.append(new_answ[-1][:-1] + check_around_directions[i_])
                            l = check_around_pos_num[check_around_directions.index(new_answ[-1][-1])]
                            new_positions[-1] = [e[0] + l[0], e[1] + l[1]]
                        map_row = map[new_positions[-1][1]]
                        map[new_positions[-1][1]] = map_row[:new_positions[-1][0]] + "F" + map_row[new_positions[-1][0] + 1:]

            else:
                new_answ.pop(-1)

            check_around_elements.clear()

        if done:
            break
        answ = new_answ.copy()
        positions = new_positions.copy()
        new_positions.clear()
        new_answ.clear()


print(f"A\n{maze_solver(labs1)}\n\nB\n{maze_solver(labs2)}\n\nC\n{maze_solver(labs3)}")
