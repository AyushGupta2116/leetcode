class Solution(object):
    def dayOfYear(self, date):
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        days = [31,28,31,30,31,30,31,31,30,31,30,31]

        if leap:
            days[1] = 29

        for i in range(month - 1):
            day += days[i]

        return day