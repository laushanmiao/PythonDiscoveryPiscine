#!/usr/bin/env python3

class Person:
    def array_of_name(persondict):
        namelist=[]
        for fname, lname in persondict.items():
            namelist.append(f"{fname.capitalize()} {lname.capitalize()}")
        return(namelist)

array_of_names = Person.array_of_name

persons = {
        'jeans': 'val',
        'ha': 'she',
        'hajd': 'haj'
        }

print(array_of_names(persons))
