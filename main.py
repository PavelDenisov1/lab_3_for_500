from time import sleep

import yaml
from package.file_reader import file_reader  #импортируем из пакета класс file_reader
from package.sort import selection_sort  #импортируем из пакета функцию selection_sort

object = file_reader('output.txt') #создаем объект класса file_reader см. file_reader.py
data = object.get_data() #переменаня data - это список узлов node. То есть data=[node[0],node[1],node[2] ..... node[1000]]   СМОТРИ node.py
print(data)#неотсортированный список
selection_sort(data)#сортируем список data
sleep(10)
print(data)#отсортированный список СОРТИРУЕМ ПО ВОЗРАСТУ

ser = yaml.dump(object) #сериализуем объект класса file_reader в переменную ser
with open('sample.yaml', 'w') as f:#открываем файл на запись
    f.write(ser) #сохраняем результат сериализации в файл (сохраняем объект в файл)
f.close()#закрываем файл

with open('sample.yaml', 'r') as f:#открываем файл на чтение
    ser_2 = f.read()#сохраняем содержимое файла в переменную (ser=ser_2)
f.close()#закрываем файл

#десериализация
obj_2 = yaml.load(ser_2, Loader=yaml.Loader)#с помощью yaml.load десериализуем объект ( создаем новый объект obj_2 с такими же данными, что и у объекта data)
data_2 = obj_2.get_data()#переменаня data_2 - это список узлов node. То есть data=[node[0],node[1],node[2] ..... node[1000]]   СМОТРИ node.py
#data=data_2

f = open('sorted.txt', 'w', encoding='utf-8')
for i in data_2:#так как data_2 - это список, мы берем из списка каждый элемент поочередно и сохраняем его в файл
    f.write(str(i) + "\n")
f.close()