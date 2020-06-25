import threading
import time


class CalCul:
    num = 0
    result = 0
    i = 0

    def __init__(self, InNum):
        num = 0
        result = 0
        i = 0
        self.num = InNum

    def calculation(self):
        for i in range(1, self.num+1):
            self.result += i

    def print_result(self):
        print('1+2+3+......+', self.num, '=', self.result)


cal1 = CalCul(1000)
cal2 = CalCul(100000)
cal3 = CalCul(10000000)

th1 = threading.Thread(target=cal1.calculation)
th2 = threading.Thread(target=cal2.calculation)
th3 = threading.Thread(target=cal3.calculation)


th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

cal1.print_result()
cal2.print_result()
cal3.print_result()
