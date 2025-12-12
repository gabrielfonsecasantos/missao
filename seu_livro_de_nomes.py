#!/usr/bin/env python3

pessoas = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier",
}


def array_de_nomes(persons: dict):
    array = []
    for key, value in persons.items():
        first_name = key.capitalize()
        last_name = value.capitalize()
        whole_name = (first_name + " " + last_name)
        array.append(whole_name)
    
    return array

print(array_de_nomes(pessoas))