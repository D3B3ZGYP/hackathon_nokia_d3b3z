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

            if not new_answ[i][-1] == "S":
                previous_move = new_answ[-1][-1]
                index_of_direction_of_previous_move = check_around_directions.index(previous_move)
                if index_of_direction_of_previous_move > 1:
                    opposite_of_previous_move = check_around_directions[index_of_direction_of_previous_move - 2]
                else:
                    opposite_of_previous_move = check_around_directions[index_of_direction_of_previous_move + 2]
                check_around_elements[check_around_directions.index(opposite_of_previous_move)] = "O"

            if check_around_elements.count("G") == 1:
                new_answ[-1] += check_around_directions[check_around_elements.index("G")] + "G"
                print(new_answ[-1])
                done = True

            if check_around_elements.count(".") == 1:
                new_answ[-1] += check_around_directions[check_around_elements.index(".")]
                l = check_around_pos_num[check_around_directions.index(new_answ[-1][-1])]
                new_positions.append([e[0] + l[0], e[1] + l[1]])

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

            check_around_elements.clear()

        if done:
            break
        answ = new_answ.copy()
        positions = new_positions.copy()
        new_positions.clear()
        new_answ.clear()


print("A")
maze_solver(labs1)
print("B")
maze_solver(labs2)
print("C")

end = time.time()
