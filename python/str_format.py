#age =26
#name = "Swaroop"
#print("Возраст {0} -- {1} лет." .format(name, age))
#print('Почему {0} забавляется с этим python?'.format(name))

#без цифр тоже работает
age =26
name = "Swaroop"
print("Возраст {} -- {} лет." .format(name, age))
print('Почему {} забавляется с этим python?'.format(name))
#десятичное число (.) с точностью 3 знакка для плавующих:
print('{0:.3}'.format(1/3))
#заполнить подчеркиваниеми (_) с центровкой текста (^) по ширене 11:
print('{0:_^11}'.format('hello')) 
#по ключевым словам
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))