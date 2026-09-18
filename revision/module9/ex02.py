#!/usr/bin/env python3

class Classroom:
    def average(classroom_dict):
        average_mark = sum(classroom_dict.values())/len(classroom_dict)
        return(round(average_mark,1))

average = Classroom.average

class_3B = {
        'mrine': 18,
        'jean': 15,
        'coline': 8,
        'luc': 9
        }

class_3C = {
        'quen': 17,
        'julie':15,
        'marc':8
        }

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
