import json
import os

FILENAME = 'data.json'


def field_to_str(field: list[list[int]]) -> str:
    string = ''
    for x in range(9):
        for y in range(9):
            string += str(field[x][y])
    return string


def str_to_field(string: str) -> list[list[int]]:
    field = []
    for x in range(9):
        row = []
        for y in range(9):
            row.append(int(string[x * 9 + y]))
        field.append(row)
    return field


def format_9x9_square(arr):
    lines = []
    for i in range(9):
        row = arr[i] if i < len(arr) else [0] * 9
        row_9 = row[:9] + [0] * (9 - len(row))
        line = " | ".join(str(x) for x in row_9)
        lines.append(line)
    return "\n".join(lines)


def save_data(id: int, data_array: list):
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = {}
    else:
        all_data = {}

    all_data['best_fitness'].append(data_array[0])
    all_data[str(id)] = data_array

    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)


def read_data():
    if not os.path.exists(FILENAME):
        return None

    with open(FILENAME, 'r', encoding='utf-8') as f:
        try:
            all_data = json.load(f)
        except json.JSONDecodeError:
            return None

    return all_data


def data_init():
    all_data = {}
    all_data['best_fitness'] = []
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)


def clean_data():
    with open(FILENAME, 'w', encoding='utf-8') as f:
        pass