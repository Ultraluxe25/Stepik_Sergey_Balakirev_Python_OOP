class Translator:
    def add(self, eng: str, rus: str):
        if "tr" not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add
        # self.tr[eng]: dict[list[str]]
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng: str):
        # здесь продолжайте метод remove
        # self.tr.pop(eng, "Нет такого слова в словаре.")
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng: str) -> list[str]:
        # здесь продолжайте метод translate
        return self.tr.get(eng, [])

            
# здесь создавайте объект класса Translator
tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")
print(*tr.translate("go"))

tr.add("go", "ехать")
tr.add("go", "ехать")
tr.add("go", "ехать")
tr.add("go", "ехать")

tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")
print(tr.translate("sex"))
      