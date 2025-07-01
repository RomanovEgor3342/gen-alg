import json
import os

FILENAME = 'data.json'


def save_data(id=int, data_array=list):
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = {}
    else:
        all_data = {}

    all_data[str(id)] = data_array

    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)


def read_data(id=int):
    if not os.path.exists(FILENAME):
        return None

    with open(FILENAME, 'r', encoding='utf-8') as f:
        try:
            all_data = json.load(f)
        except json.JSONDecodeError:
            return None

    return all_data.get(str(id))


def clean_data():
    with open(FILENAME, 'w', encoding='utf-8') as f:
        pass