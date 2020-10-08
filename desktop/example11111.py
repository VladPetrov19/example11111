from dataclasses import dataclass


@dataclass
class DataReader:

    def __init__(self, f=open('datafile.txt')):
        self.f = f.read()


reader = DataReader()
r = reader.f
for number in r:
    print(number)