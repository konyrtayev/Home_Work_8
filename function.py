FILE_PATH = r"phone_book.txt"

def show_contacts():
  with open(FILE_PATH, 'r', encoding="utf-8") as f:
    i = 1
    for line in (list(map(lambda x: x.strip(), f.readlines()))):
      print(f"{i}. {line}")
      i += 1
    print()

def add_contact():
  surname = input("Фамилия: ")
  name = input("Имя: ")
  second_name = input("Отчество: ")
  phone = input("Телефон: ")
  with open(FILE_PATH, 'a+', encoding="utf-8") as f:
    f.write(f"{surname},{name},{second_name},{phone}\n")
  print()

def delete_contact():
  contacts = list()
  with open(FILE_PATH, 'r', encoding="utf-8") as f:
    contacts = list(map(lambda x: x.strip(), f.readlines()))
    index = int(input("Введите номер удаляемого контакта: ")) - 1
    del contacts[index]

  with open(FILE_PATH, 'w', encoding="utf-8") as f:
    for i in contacts:
      f.write(f"{i}\n")

def edit_contact():
  contacts = list()
  with open(FILE_PATH, 'r', encoding="utf-8") as f:
    contacts = list(map(lambda x: x.strip(), f.readlines()))
    index = int(input("Введите номер контакта для редактирования: ")) - 1

    surname = input("Фамилия: ")
    name = input("Имя: ")
    second_name = input("Отчество: ")
    phone = input("Телефон: ")
    contacts[index] = f"{surname},{name},{second_name},{phone}"
    
  with open(FILE_PATH, 'w', encoding="utf-8") as f:
    for i in contacts:
      f.write(f"{i}\n")