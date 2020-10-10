from dataclasses import dataclass


@dataclass
class DataReader:
    file_path: str

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path)

    def __iter__(self):
        return iter(self.file.read().split(','))


reader = DataReader('datafile.txt')

for number in reader:
    print(number)
