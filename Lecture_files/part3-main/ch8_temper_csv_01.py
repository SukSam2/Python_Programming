
f_in = open('temper.csv', 'r', newline='')
f_out = open('temper-m.csv', 'w', newline='')

#head = [next(f_in) for x in range(6)]
#print(head)

header = f_in.readline()
#print('header: ', header)
newheader = header.replace("평균","중간")
#print('newheader: ', newheader)
f_out.write(newheader)

for row in f_in:
    if row == '\n': 
        break	# finish at end-line
    #print(row)
    rowLst = row.split(',')
    #print(rowLst)
    rowLst[2] = str((float(rowLst[3]) + float(rowLst[4])) / 2)
    f_out.write(','.join(rowLst))

f_in.close()
f_out.close()
