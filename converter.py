import time
from datetime import date, timedelta
import csv

def main():
    starting_date = date(2016, 9, 12) # Sep 12
    ending_day = date(2016, 12, 10) # Dec 10

    f = open('timetable.csv', 'r')
    shead = f.readline()
    sl_all_courses = []
    s = f.readline()
    while (s):
        sl = s.split(",")
        sl_all_courses.append(sl)
        s = f.readline()
    f.close()

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

    f = open('output.csv', 'w')
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    f.write(shead)

    for entry in complete_lists:
        wr.writerow(entry)
    f.close()

if __name__ == "__main__":
    main()
