import numpy as np
"""
Получение начальной расстановки и создание популяции
"""
class FieldCreator():
    def __init__(self):
        self.main_permutation = list(range(1, 10)) * 9
        self.insert_list_indexes = []
        self.insert_list_symbols = []
    def ReadFromFile(self, file_name: str) -> None:
        with open(file_name, 'r') as file:
            file_field = [item.split(' ') for item in file.read().split('\n')]

        for x in range(9):
            for y in range(9):
                symbol = file_field[x][y]
                if symbol != 'x':
                    self.insert_list_indexes.append((x, y))
                    self.insert_list_symbols.append(int(symbol))
                    self.main_permutation.remove(int(symbol))
        

    def GeneratePopulation(self, entities_amount: int) -> list:
        population = []
        for _ in range(entities_amount):
            new_entity = np.random.permutation(self.main_permutation).tolist()
            for index in range(len(self.insert_list_symbols)):
                new_entity.insert(self.insert_list_indexes[index][0] * 9 + self.insert_list_indexes[index][1], self.insert_list_symbols[index])
            new_entity = [new_entity[i:i + 9] for i in range(0, 81, 9)]
            population.append(new_entity)

        return population



def main():
    field_creator = FieldCreator()
    field_creator.ReadFromFile('example.txt')
    print(field_creator.insert_list)
    population = field_creator.GeneratePopulation(5)
    for item in population:
        print('\n'.join([' '.join(list(map(str, item[i]))) for i in range(9)]) + '\n')



if __name__ == '__main__':
    main()