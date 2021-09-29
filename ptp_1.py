password = input('Введите пароль: ')

try:
    1/len(password) 
    int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль') 
except ValueError:
    print('Требования к паролю соблюдены') 
