from dataclasses import dataclass


@dataclass
class DataReader:
    file_path: str

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path)
        self.is_end_of_file = False

    def __iter__(self):
        return self

    def __next__(self):
        string = ''
        if self.is_end_of_file:
            self.file.close()
            raise StopIteration()
        while True:
            char = self.file.read(1)
            self.is_end_of_file = char == ''
            if char != ',' and not self.is_end_of_file:
                string += char
            else:
                break
        return float(string)


reader = DataReader('datafile.txt')

for number in reader:
    print(number)
