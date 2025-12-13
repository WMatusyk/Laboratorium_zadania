class LogReader:
    def __init__(self, filename, keyword):
        self.file = open(filename)
        self.keyword = keyword
    def __iter__(self):
        return self
    def __next__(self):
        for line in self.file:
            if self.keyword in line:
                return line
        raise StopIteration

lr = LogReader("plik_testowy.txt", "optymalizacja")
for line in lr:
    print(line)