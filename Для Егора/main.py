class NotOneNumber(Exception):
    pass
def get_age():
    age_int = None
    while age_int == None:
        try:
            age = input("Введите возраст: ")
            if len(list(age.split())) != 1:
                raise NotOneNumber
        except NotOneNumber:
            print("Введите ровно одно число")
            pass
        else:
            try:
                age_int = int(age)
                if 100 <= age_int or age_int <= 0:
                  age_int = None
                  print('Возраст должен быть от 1 до 99')
            except ValueError:
                print('Возраст должен быть числом')
            else:
                pass


    return age_int

print('Ваш возраст: ', get_age())