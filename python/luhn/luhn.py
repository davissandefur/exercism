class Luhn(object):
    def __init__(self, number):
        self.number = number

    def addends(self):
        old = [int(digit) for digit in str(self.number)]
        transform = lambda n: (2 * n - 9) if (n > 4) else (2 * n)
        return [(transform(n) if (i % 2 == 0) else n)
                for i, n in enumerate(old, start=len(old) % 2)]

    def checksum(self):
        return sum(self.addends()) % 10

    def is_valid(self):
        return self.checksum() == 0

    @staticmethod
    def create(n):
        diff = (10 - Luhn(n * 10).checksum()) % 10
        return 10 * n + diff
