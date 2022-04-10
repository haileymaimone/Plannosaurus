class StartingDates:
    def __init__(self, day1, day2, day3, day4, day5, day6, day7):
        self._day1 = day1
        self._day2 = day2
        self._day3 = day3
        self._day4 = day4
        self._day5 = day5
        self._day6 = day6
        self._day7 = day7
    
    @property
    def day1(self):
        return self._day1

    @day1.setter
    def day1(self, val):
        self._day1 = val
    
    @property
    def day2(self):
        return self._day2

    @day2.setter
    def day2(self, val):
        self._day2 = val
    
    @property
    def day3(self):
        return self._day3

    @day3.setter
    def day3(self, val):
        self._day3 = val

    @property
    def day4(self):
        return self._day4

    @day4.setter
    def day4(self, val):
        self._day4 = val

    @property
    def day5(self):
        return self._day5

    @day5.setter
    def day5(self, val):
        self._day5 = val
    
    @property
    def day6(self):
        return self._day6

    @day6.setter
    def day6(self, val):
        self._day6 = val

    @property
    def day7(self):
        return self._day7

    @day7.setter
    def day7(self, val):
        self._day7 = val
