from .file_reader import * #(импортируем все что есть в file_reader.py)
#from .file_reader означает, что мы переходим в файл, import * означает что мы импортируем все что есть в файле file_reader
from .node import * #(импортируем все что есть в node.py)
from .sort import * #(импортируем все что есть в sort.py)
#так как в пакете есть все файлы проекта, мы можем испортировать из пакета нужные функции и т.д.   from package.file_reader import file_reader
#from package.sort import selection_sort    СМОТРИ main.py

NAME = "lab3 package" #имя пакета