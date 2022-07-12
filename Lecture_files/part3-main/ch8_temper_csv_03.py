import csv

with open('temper.csv', 'r', newline='') as f_in:
    with open('temper-m.csv', 'w', newline='') as f_out:
        data = csv.reader(f_in)
        outcsv = csv.writer(f_out)
        header = next(data)	# header = ['날짜','지점','평균기온(℃)','최저기온(℃)','최고기온(℃)']
        header[2] = "중간기온(°C)"
        outcsv.writerow(header)
        for row in data:		# 첫번쨰 row = ['1907-10-01', '108', 14.3, 7.9, 20.7]
            if not row: break	# finish at end-line
            row[2] = str((float(row[3]) + float(row[4])) / 2)
            outcsv.writerow(row)


