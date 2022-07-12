with open('temper.csv', 'r', newline='') as f_in:
    with open('temper-m.csv', 'w', newline='') as f_out:
        #skiplines = [next(f_in) for x in range(6)]
        header = f_in.readline()
        #print(header)
        newheader = header.replace("평균","중간")
        #print(newheader)
        f_out.write(newheader)

        for row in f_in:
            if row == '\n': break	# finish at end-line
            rowLst = row.split(',')
            rowLst[2] = str((float(rowLst[3]) + float(rowLst[4])) / 2)
            f_out.write(','.join(rowLst))
