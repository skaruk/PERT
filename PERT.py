import prettytable as pt


def Fix (num, digist=0):
    #return float(f"{num:.digits}f}")
    return f"{num:.{digist}f}"

def main ():
    char_const = 65
    N = int(input('Введите кол-во работ: '))
    amb = []
    for i in range(N):
        a_tmp = float(input('Введите a' + str(i+1) + ' : '))
        m_tmp = float(input('Введите m' + str(i+1) + ' : '))
        b_tmp = float(input('Введите b' + str(i+1) + ' : '))
        amb.append([a_tmp, m_tmp, b_tmp])
    result = []
    for item in amb:
        index_tmp = amb.index(item)
        t_tmp = Fix(((item[0] + 4*item[1] + item[2])/6),2)
        D_tmp = Fix(((item[2] - item[0])/6)**2,2)
        result.append ([chr(index_tmp + char_const), t_tmp, D_tmp])
    header = ['Работа', 't', 'D']
    table = pt.PrettyTable()
    table.field_names = header
    for row in result:
        table.add_row(row)
    print (table)


if __name__ == '__main__':
    main()
