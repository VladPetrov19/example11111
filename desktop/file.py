from random import uniform

# 1

def generate_numbers(min, max, count):
    output = []
    for i in range(count):
        output.append(round(uniform(min, max), 1))
    return output

def write_numbers(numbers):
    file = open('numbers.txt', 'w')
    for number in numbers:
        file.write(str(number))
        file.write(',')
    file.close()
    pass

numbers_list = generate_numbers(1, 100, 10000)
write_numbers(numbers_list)

# 2

class Statistics(object):
    data = {}
    file_path = ''
    file = None

    def __init__(self, user_file_path):
        self.file_path = user_file_path

    def read(self):
        self.file = open(self.file_path)
        while True:
            number = self._read_next_number()
            if number is None:
                break
            self._set_or_update_counter(number)
        self.file.close()
        return

    def _read_next_number(self):
        buffer = []
        while True:
            char = self.file.read(1)
            if char == ',':
                break
            if char == '':
                return None
            buffer.append(char)
        str_value = ''.join(buffer)
        int_value = float(str_value)
        return int_value

    def _set_or_update_counter(self, number):
        if number in self.data:
            count = self.data[number]
            count += 1
            self.data[number] = count
        else:
            self.data[number] = 1

stat = Statistics('numbers.txt')
stat.read()
print(stat.data)


def get_max_number(stat):
    max_number = 0
    max_value = 0
    for key, value in stat.data.items():
        if value > max_value:
            max_value = value
            max_number = key
    return (max_number, max_value)

print(get_max_number(stat))

def get_avg_number(stat):
    numbers_list = stat.data.keys()
    average = sum(numbers_list) / len(numbers_list)
    return round(average, 6)

print(get_avg_number(stat))