import time
import pandas as pd
import Data
import re
import matplotlib.pyplot as plt
import openpyxl

class ComplexHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def complex_hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def insert(self, data):
        complex_hash = self.complex_hash_function(data.FullName)
        data.set_complex_hash(complex_hash)
        if self.table[complex_hash] is None:
            self.table[complex_hash] = []
        else:
            self.resolve_collision(complex_hash)  # Разрешение коллизий
        self.table[complex_hash].append(data)

    def resolve_collision(self, hash_value):
        self.collisions += 1
        while self.table[hash_value] is not None:
            hash_value = (hash_value + 1) % self.size

    def search(self, key):
        f = open('times.txt', 'a')
        start_time = time.time()
        hash_value = self.complex_hash_function(key)
        if self.table[hash_value] is not None:
            for data in self.table[hash_value]:
                if data.FullName == key:
                    note = 'search time COMPLEX = ' + str(time.time() - start_time) + '\n'
                    f.write(note)
                    f.close()
                    return data
        return None

    def get_collisions(self):
        return self.collisions


class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def simple_hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, data):
        simple_hash = self.simple_hash_function(data.FullName)
        data.set_simple_hash(simple_hash)
        if self.table[simple_hash] is None:
            self.table[simple_hash] = []
        else:
            self.resolve_collision(simple_hash)  # Разрешение коллизий
        self.table[simple_hash].append(data)

    def resolve_collision(self, hash_value):
        self.collisions += 1
        while self.table[hash_value] is not None:
            hash_value = (hash_value + 1) % self.size

    def search(self, key):
        f = open('times.txt', 'a')
        start_time = time.time()
        hash_value = self.simple_hash_function(key)
        if self.table[hash_value] is not None:
            for data in self.table[hash_value]:
                if data.FullName == key:
                    note = 'search time SIMPLE = ' + str(time.time() - start_time) + '\n'
                    f.write(note)
                    f.close()
                    return data
        return None

    def get_collisions(self):
        return self.collisions



def to_excel_file(arr, file_name: str):
    df = pd.DataFrame(data=data_array(arr), columns=['Date', 'Flight', 'Full Name', 'Place'])
    file_name = file_name + '.xlsx'
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, 'flight_table1')
    writer.close()


def from_excel_file(file_name: str):
    xl = pd.ExcelFile(file_name)
    df = xl.parse('flight_table1')
    arr = []
    for i in range(len(df)):
        row = df.iloc[i]
        data = Data.Data(row[1].to_pydatetime(), int(row[2]), str(row[3]), int(row[4]))
        arr.append(data)
    return arr

def data_array(array):
    arr = []
    for i in range(len(array)):
        arr2 = []
        arr2.append(array[i].Date)
        arr2.append(array[i].Flight)
        arr2.append(array[i].FullName)
        arr2.append(array[i].Place)
        arr.append(arr2)
    return arr

def create_table_complex (data_file: str, text_file: str):
    f = open(text_file, 'a')
    number = int(re.findall(r'\d+', data_file)[0])
    array = from_excel_file(data_file)
    start_time = time.time()
    hash_table_c = ComplexHashTable(number)
    for data in array:
        hash_table_c.insert(data)
    note = data_file + ' time = ' + str(time.time() - start_time) + ' !! CREATE !!' + '\n'
    f.write(note)
    f.close()
    return hash_table_c

def create_table_simple (data_file: str, text_file: str):
    f = open(text_file, 'a')
    number = int(re.findall(r'\d+', data_file)[0])
    array = from_excel_file(data_file)
    start_time = time.time()
    hash_table_s = SimpleHashTable(number)
    for data in array:
        hash_table_s.insert(data)
    note = data_file + ' time = ' + str(time.time() - start_time) + ' !! CREATE !!' + '\n'
    f.write(note)
    f.close()
    return hash_table_s

# Пример использования
collisions_simple = []
collisions_complex = []

hash_table_s = create_table_simple('flight_info_100.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_100.xlsx', 'times.txt')

search_key = "Lydmila Eduardovna Sinyakaeva"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())


hash_table_s = create_table_simple('flight_info_500.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_500.xlsx', 'times.txt')

search_key = "Natalya Mihaylovna Bekbaeva"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())


hash_table_s = create_table_simple('flight_info_1000.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_1000.xlsx', 'times.txt')

search_key = "Dmitriy Yakovlevich Kochetinin"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())


hash_table_s = create_table_simple('flight_info_2500.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_2500.xlsx', 'times.txt')

search_key = "Arkadiy Vasilievich Avdyshev"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())


hash_table_s = create_table_simple('flight_info_5000.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_5000.xlsx', 'times.txt')

search_key = "Zinaida Eduardovna Poluneeva"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())


hash_table_s = create_table_simple('flight_info_7500.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_7500.xlsx', 'times.txt')

search_key = "Yakov Fedorovich Katrichev"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())


hash_table_s = create_table_simple('flight_info_10000.xlsx', 'times.txt')
hash_table_c = create_table_complex('flight_info_10000.xlsx', 'times.txt')

search_key = "Klavdiya Nikitichna Kaursinova"
found_data = hash_table_s.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")
found_data = hash_table_c.search(search_key)
if found_data is not None:
    print("Найден элемент:", found_data)
else:
    print("Элемент с ключом", search_key, "не найден")

collisions_simple.append(hash_table_s.get_collisions())
collisions_complex.append(hash_table_c.get_collisions())

print("SIMPLE COLLISION NUMBERS \n")
print(collisions_simple)
print("COMPLEX COLLISION NUMBERS \n")
print(collisions_complex)
