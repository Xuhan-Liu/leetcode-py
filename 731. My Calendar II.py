class MyCalendarTwo:

    def __init__(self):
        self.calendars = []
        self.intersectedPeriod = []

    def book(self, start: int, end: int) -> bool:
        for [s, e] in self.intersectedPeriod:
            if end > s and start < e:
                return False
        for [s, e] in self.calendars:
            if start < e and end > s:
                self.intersectedPeriod.append([max(s, start), min(e, end)])
        self.calendars.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
