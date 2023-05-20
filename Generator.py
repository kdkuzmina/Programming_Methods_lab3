from russian_names import RussianNames
import pandas as pd
import random
import time
import datetime
import xlsxwriter

long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 10]

def random_date(start, end, prop):
    time_format = '%m/%d/%Y %I:%M %p'
    ptime = time.mktime(time.strptime(start, time_format)) + prop * time.mktime(time.strptime(end, time_format))
    return time.strftime(time_format, time.localtime(ptime))

def line_generator():
  arr = []
  date = []
  date.append(random.randint(2000, 2023))
  date.append(random.randint(1, 12))
  if date[-1] in long_months:
      date.append(random.randint(1, 31))
  elif date[-1] in short_months:
      date.append(random.randint(1, 30))
  else:
      date.append(random.randint(1, 28))
  date.append(random.randint(0, 23))
  date.append(random.randint(0, 59))
  date.append(random.randint(0, 59))
  arr.append(datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5]))
  arr.append(random.randint(0, 10000))
  rn = RussianNames(count = 1, patronymic = True, transliterate = True)
  for person in rn:
        arr.append(person)
  arr.append(random.randint(0,150))
  return arr

def table_generator (n: int):
  arr = []
  for i in range(n):
    arr.append(line_generator())
  return arr

def xlsx_file_generator(n: int) -> object:
  start_time = time.time()
  df = pd.DataFrame(table_generator(n), columns = ['Date', 'Flight', 'Full Name', 'Place'])
  data_file = 'flight_info_' + str(n) + '.xlsx'
  writer = pd.ExcelWriter(data_file, engine='xlsxwriter')
  df.to_excel(writer, 'flight_table1')
  writer.close()
  print(data_file + ':')
  print("       %s seconds       " % (time.time() - start_time))

xlsx_file_generator(100)
xlsx_file_generator(500)
xlsx_file_generator(1000)
xlsx_file_generator(2500)
xlsx_file_generator(5000)
xlsx_file_generator(7500)
xlsx_file_generator(10000)
