def incremento(x):
    return x+1

resultado= incremento(10)
print(resultado)

increment = lambda x:x+1

result = increment(10)
print(result)

full_name= lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

nombre= full_name('samir','gallego')
print(nombre)