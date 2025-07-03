class ReaderWriter():
    def ReadFromFile(self, file_name: str) -> None:
        main_permutation = list(range(1, 10)) * 9
        insert_list_indexes = []
        insert_list_symbols = []

        with open(file_name, 'r') as file:
            file_field = [item.split(' ') for item in file.read().split('\n')]

        for x in range(9):
            for y in range(9):
                symbol = file_field[x][y]
                if symbol != 'x':
                    insert_list_indexes.append((x, y))
                    insert_list_symbols.append(int(symbol))
                    main_permutation.remove(int(symbol))
        return main_permutation, insert_list_indexes, insert_list_symbols

    def ReadFromList(self, arr: list[list[str]]) -> None:
        main_permutation = list(range(1, 10)) * 9
        insert_list_indexes = []
        insert_list_symbols = []
        for x in range(9):
            for y in range(9):
                symbol = arr[x][y]
                if symbol != 'x':
                    insert_list_indexes.append((x, y))
                    insert_list_symbols.append(int(symbol))
                    main_permutation.remove(int(symbol))
        return main_permutation, insert_list_indexes, insert_list_symbols