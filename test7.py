while True:
    line = input('>')
    if line[0] ==   '#':
        continue        #Возвращает обратнов начало
    if line == 'done':
        break        #Если done то срабатывает брейк и работает последний принт
    print (line)
print('Done!')