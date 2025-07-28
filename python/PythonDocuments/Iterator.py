class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Iterator object itself

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


counter = Counter(5, 1)
for num in counter:
    print(num)
