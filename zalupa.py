import prettytable as pt

N = int(input('Введите количество работ: '))
index = []
a_b_m_i = []
for i in range(N):
    index.append(i+1)
    a_i = float(input('Введите а_' + str(i+1) + ':'))
    m_i = float(input('Введите m_' + str(i+1) + ':'))
    b_i = float(input('Введите b_' + str(i+1) + ':'))
    a_b_m_i.append([a_i,m_i,b_i])

i = 1
answer = []
for item in a_b_m_i:
    t_i = (item[0]+4*item[1]+item[2])/6
    D_i = ((item[2]-item[0])/6)**2
    answer.append([chr(64+i), t_i, D_i])
    i += 1


row = ['N', 't_i', 'D_i']
table = pt.PrettyTable()
table.field_names = row
for row in answer:
    table.add_row(row)
print(table)

