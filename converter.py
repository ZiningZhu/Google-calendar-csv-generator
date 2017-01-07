import time
from datetime import date, timedelta
import csv

def main():
    starting_date = date(2017, 1, 9) # Sep 12
    ending_day = date(2017, 4, 7) # Dec 10

    f = open('timetable.csv', 'r')
    shead = f.readline()
    sl_all_courses = []
    s = f.readline()
    while (s):
        sl = s.split(",")
        sl_all_courses.append(sl)
        s = f.readline()
    f.close()

    '''
    complete_lists = []
    d = starting_date # The starting date of each week
    week = 1
    while(d < ending_day):
        print "week #%d" %week
        for elem in sl_all_courses:
            entry = []
            entry[:] = elem[:]

            if entry[1] == 'M':
                dtp = d
            elif entry[1] == 'T':
                td = timedelta(days=1)
                dtp = d + td
            elif entry[1] == 'W':
                td = timedelta(days=2)
                dtp = d + td
            elif entry[1] == 'R':
                td = timedelta(days=3)
                dtp = d + td
            else:
                #entry[1] == 'F'
                td = timedelta(days=4)
                dtp = d + td

            ds = format("%02d/%02d/%02d" %(dtp.month, dtp.day, dtp.year))
            entry[1] = ds
            entry[3] = ds
            complete_lists.append(entry)
        week += 1
        td = timedelta(days=7)
        d += td
    '''
    complete_lists = []
    d = starting_date
    m2d = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4}
    while (d < ending_day):
        #print "d.weekday()=", str(d.weekday())
        day = d.weekday()
        for elem in sl_all_courses:
            entry = []
            entry[:] = elem[:]
            if (m2d[entry[1]] == d.weekday()):
                ds = format("%02d/%02d/%02d" %(d.month, d.day, d.year))
                entry[1] = ds
                entry[3] = ds
                complete_lists.append(entry)
        d += timedelta(days=1)

    f = open('output.csv', 'w')
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    f.write(shead)

    for entry in complete_lists:
        wr.writerow(entry)
    f.close()

if __name__ == "__main__":
    main()
