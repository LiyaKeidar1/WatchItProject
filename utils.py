import json
from consts import VALID, TOO_LOW, TOO_HIGH


# different utilities for the code
def load_json(path) -> json:
    with open(path, 'r') as file:
        return json.load(file)


def data_in_range(data, valid_range) -> int:
    if valid_range[0] <= data <= valid_range[1]:
        return VALID
    if data < valid_range[0]:
        return TOO_LOW
    if data > valid_range[1]:
        return TOO_HIGH
