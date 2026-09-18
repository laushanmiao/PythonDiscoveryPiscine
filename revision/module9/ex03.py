#!/usr/bin/env python3

class Person:
    def famous_births(birthday_dict):
        for scientist in birthday_dict.values():
            name = scientist['name']
            date = scientist['date_of_birth']
            print(f"{name} is a great scientist born in {date}.")

famous_births = Person.famous_births

women_scientists = {
        'ada':{'name':'Ada Lovelace','date_of_birth':"1815"},
        'cecilia':{'name':'Cecilia Payne','date_of_birth':"1900"},
        'lise':{'name':'Lise Meitner','date_of_birth':"1878"},
        'grace':{'name':'Grace Hopper','date_of_birth':"1906"}
        }

famous_births(women_scientists)
