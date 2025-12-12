#!/usr/bin/env python3




def famous_births(historic_figures):
    sorted_dict = sorted(historic_figures.items(), key= lambda item: item[1]["date_of_birth"])
    res = dict(sorted_dict)
    for key, value in res.items():
        print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")
    return 


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"} 
}


famous_births(women_scientists)
