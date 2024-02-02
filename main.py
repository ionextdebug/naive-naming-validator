# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:34:49 2024

@author: ionextdebug

@description: Naive example about how to analyze a text structure,
                in this case the structure <[compound] name> <surname>.
                
                
@recommendations:
                - You can improve it using Hamming Distance Algorithm
                - You can apply regular expressions
                - You can refactor this code using Class

"""


valid_names = [
                "Liam",
                "Olivia",
                "Noah",
                "Emma",
                "Oliver",
                "Charlotte",
                "James",
                "Amelia",
                "Elijah",
                "Sophia",
                "William",
                "Isabella",
                "Henry",
                "Ava",
                "Lucas",
                "Mia",
                "Benjamin",
                "Evelyn",
                "Theodore",
                "Luna",
                    ]

valid_surnames = [
                "Smith",
                "Johnson",
                "Williams",
                "Brown",
                "Jones",
                "Garcia",
                "Miller",
                "Davis",
                "Rodriguez",
                "Martinez",
                ]



def is_valid_name(target, reference):
    if target in valid_names:
        return True
    else:
        return False    


def is_valid_surname(target, reference):
    if target in valid_surnames:
        return True
    else:
        return False
    
def is_valid_name_surname(name, surname):
    return is_valid_name(name, valid_names) and is_valid_surname(surname, valid_surnames)


def is_valid_compound_name_surname(primary_name, secondary_name, surname):
    return is_valid_name(primary_name, valid_names) and is_valid_name(secondary_name, valid_names) and is_valid_surname(surname, valid_surnames)
    
if __name__ == "__main__":
    
    text : str = input("Write the name-surname to be tested: ")
    splited_text = text.split(" ")
    
    match len(splited_text):
        case 0: print("The structure is wrong.")
        case 1: print("The structure is wrong.")
        case 2:
            if is_valid_name_surname(splited_text[0], splited_text[1]): print("Valid name-surname structure.")
            else: print("The structure is wrong.")
        case 3:
            if is_valid_compound_name_surname(splited_text[0], splited_text[1], splited_text[2]): print("Valid compound-name-surname structure.")
            else: print("The structure is wrong.")
