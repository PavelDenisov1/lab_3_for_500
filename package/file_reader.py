import json
from package import node

class file_reader:
    data: list[node]

    def __init__(self, path) -> None:
        self.data = json.load(open(path, encoding='utf-8')) #сохраняем в переменную data, все что содержится в файле output.txt
#теперь data - это список узлов node. То есть data=[node[0],node[1],node[2] ..... node[1000]]   СМОТРИ node.py
    def get_data(self) -> list[node]:
        return self.data