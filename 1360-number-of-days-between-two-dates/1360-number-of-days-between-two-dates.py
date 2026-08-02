class Solution(object):
    def daysBetweenDates(self, date1, date2):

        year1 = int(date1[:4])
        month1 = int(date1[5:7])
        day1 = int(date1[8:])

        year2 = int(date2[:4])
        month2 = int(date2[5:7])
        day2 = int(date2[8:])

        total1 = 0
        for y in range(1, year1):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                total1 += 366
            else:
                total1 += 365

        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
            days[1] = 29

        for i in range(month1 - 1):
            total1 += days[i]
        total1 += day1

        total2 = 0
        for y in range(1, year2):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                total2 += 366
            else:
                total2 += 365

        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0):
            days[1] = 29

        for i in range(month2 - 1):
            total2 += days[i]
        total2 += day2

        return abs(total2 - total1)