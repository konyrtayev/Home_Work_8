# w - перезапись
# r - чтение
# a - дозапись
# r+ - чтение + запись
# b - байт

import function

is_active = True

while is_active:
  print("[1] Показать список")
  print("[2] Добавить запись")
  print("[3] Редактировать запись")
  print("[4] Удалить запись")
  print("[5] Выход")
  print()
  res = int(input("Введите номер задачи: "))

  if res == 1:
    function.show_contacts()
  elif res == 2:
    function.add_contact()
  elif res == 3:
    function.edit_contact()
  elif res == 4:
    function.delete_contact()
  elif res == 5:
    is_active = False
  else:
    print("Ошибка")