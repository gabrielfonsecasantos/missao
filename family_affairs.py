#!/usr/bin/env python3

familia_dupont = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
    "john": "brunette",
    "gabriel": "red"
}

def filter_function(pair):
    wanted_value = "red"
    key, value = pair
    if value == wanted_value:
        return True
    else:
        return False

def find_the_redheads(family: dict):
    readheads = dict(filter(filter_function, family.items())).keys()
    readheads_list = list(readheads)
    return readheads_list

print(find_the_redheads(familia_dupont))