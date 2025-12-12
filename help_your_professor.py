#!/usr/bin/env python3

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

def average(classe):
    grades = 0
    for key, value in classe.items():
        grades += value
    
    return grades/len(classe)

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")