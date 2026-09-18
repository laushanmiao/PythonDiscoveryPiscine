#!/usr/bin/env python3

class Family:
    def find_the_redheads(familydict):
        redheads = {name:colour for name,colour in familydict.items() if colour=='red'}
        return(list(redheads))

find_the_redheads = Family.find_the_redheads

dupont_family = {
        'florian':'red',
        'marie':'blond',
        'virginie':'brunette',
        'david':'red',
        'frank':'red'
        }

print(find_the_redheads(dupont_family))
