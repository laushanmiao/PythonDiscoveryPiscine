#!/usr/bin/env python3

def array_of_names(name_dict):
    namelist = []
    for firstname, lastname in name_dict.items():
        wholename = f"{firstname.capitalize()} {lastname.capitalize()}"
        namelist.append(wholename)
    return(namelist)

persons = {
        'jean':'valjean',
        'grace':'hopper',
        'xavier':'niel',
        'fifi':'brindacier'
        }

print(array_of_names(persons))
