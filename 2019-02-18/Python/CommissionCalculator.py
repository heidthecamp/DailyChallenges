import csv


def get_csv(fname):
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        result = list(map(list, csv_reader))

        return result



rev = get_csv('../ChallengeInputs/Revenue.csv')


exp = get_csv('../ChallengeInputs/Expense.csv')


final = [[] for _ in range(2)]


row_num = 0
for row in rev:
    col_num = 0
    for col in row:
        if col_num == 0:
            col_num += 1
        else:
            if row_num == 0:
                final[0].append(col)
                final[1].append(0)
            else:
                num = int(col) - int(exp[row_num][col_num])
                if num > 0:
                    final[1][col_num - 1] += num
                col_num += 1
    row_num += 1
        # print(col)

for i in range(len(final[1])):
    final[1][i] = final[1][i] * .062

print(final)
