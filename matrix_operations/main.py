
class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __add__(self, other):
        answ = [[]]
        for i in range(len(self.rows)):
            for j in range(len(self.rows[0])):
                answ[-1].append(self.rows[i][j] + other.rows[i][j])
            answ.append([])

        answ.pop()
        return Matrix(answ)

    def __mul__(self, other):
        answ2 = [[]]
        value = 0
        for i in range(len(self.rows)):
            for j in range(len(other.rows[0])):
                for k in range(len(self.rows[0])):
                    value += self.rows[i][k] * other.rows[k][j]
                answ2[-1].append(value)
                value = 0
            answ2.append([])

        answ2.pop()
        return Matrix(answ2)

    def read(self):
        read1 = ""
        for i in range(len(self.rows)):
            for j in range(len(self.rows[0])):
                read1 += str(self.rows[i][j]) + " "
            read1 = read1[:-1]
            read1 += "\n"
        read1 = read1[:-1]
        return read1


with open('./input.txt', 'r') as f:
    input = f.read()

l = input.split("\n")

variables = dict()
var_name = ""
value = []
for i in l[2:l.index("operations")]:
    if (not i.isnumeric()) and (i != "") and (not len(var_name)):
        variables[i] = []
        var_name = i
    elif i != "" and len(var_name):
        for j in i.split(" "):
            if j != "":
              value.append(int(j))
        variables[var_name].append(value)
        value = []
    else:
        variables[var_name] = Matrix(variables[var_name].copy())
        var_name = ""

operations = []
for i in l[l.index("operations")+2:-1]:
    operations.append(i)

final_op = "("
for i in operations:
    print(i)
    for j in i.replace(" ",""):
        if j.isalnum():
            final_op += f"variables['{j}']"
        else:
            final_op += j
    final_op += ").read()"
    exec(f"print({final_op})")
    print("")
    final_op = "("
