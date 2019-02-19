import csv


def get_csv(fname):
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        result = list(map(list, csv_reader))

        return result



rev = get_csv('../ChallengeInputs/Revenue.csv')
#print(rev)


exp = get_csv('../ChallengeInputs/Expense.csv')
#print(exp)

row_num = 0
for row in rev:
    col_num = 0
    if row_num == 0:
        row_num += 1
    else:
        for col in row:
            if col_num == 0:
                col_num += 1
            else:
                print(int(col) - int(exp[row_num][col_num]))
                col_num += 1
        row_num += 1
        # print(col)
