info = [
    '1 Сергей 35 120000',
    '2 Федор 23 12000',
    '3 Иван 13 1200'
]

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, info))  # считывание списка строк из входного потока


class DataBase:
    lst_data: list = []
    FIELDS: tuple = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data: list[str]):
        for person in data:
            person_info = dict(zip(self.FIELDS, person.split()))                     
            # person_info: dict = {}
            # for index, value in enumerate(person.split()):
                # person_info[self.FIELDS[index]] = value
                
            self.lst_data.append(person_info)
        
    def select(self, a: int, b: int) -> list[dict[str]]:
        return self.lst_data[a : b + 1]


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
