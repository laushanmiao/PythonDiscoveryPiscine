#!/usr/bin/env python3

class Redhead:
    def find_the_redhead(familydict):
        namelist=[]
        for name, colour in familydict.items():
            if colour == 'red':
                namelist.append(name)
        return(namelist)

find_the_redhead=Redhead.find_the_redhead

dupont_family = {
        'a':'red',
        'b':'ysh',
        'c':'red'
        }

print(find_the_redhead(dupont_family))

'''
def find_the_redheads(familydict):
    return [name for name, colour in familydict.items() if colour == 'red']
'''

'''
def find_the_redheads(familydict):
    redheads = {name:colour for name,colour in familydict.items() if colour=='red'}
    return(list(redheads))
'''
