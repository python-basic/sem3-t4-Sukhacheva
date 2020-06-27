"""
Разработать программу для считывания данных JSON-формата из файла и вывод их в табличном виде на экран.
Организовать тестирование работоспособности программы с помощью assert, print.
"""

import json

def json_table(data):

  table = []
  sstr = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
  t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id','first_name','last_name','email','gender','ip_address')
  roof = '-'*len(t_caption)
  
  table.append(roof)  
  table.append(t_caption)
  table.append(roof)  

  for el in range(len(data)):
      temp = data[el]
      res = sstr.format(**temp)
      table.append(res)
  table.append(roof)
  return(table)


def test_func(func,arg):
  """
  Эта функция тестирует функцию json_table
  func - тестируемая функция  
  """

  try:
    assert func(arg)[1] == '| id  | first_name |    last_name    |             email              | gender |    ip_address    |'
  except:
    print('Данные не соответсвуют требуемых')
  try:
    assert type(func(arg)) is tuple
  except:
    print('Неправильный тип', type(func(arg)))
  try:
    assert len(func(arg)) == 100
  except:
    print('Неправильное количесиво строк -',len(func(arg)))
 

def main():
  with open('MOCKDATA.json') as f:
    data_dict = json.load(f)

  test_func(json_table,data_dict)
  """
  for el in table:
    print(el)
  """
main()
