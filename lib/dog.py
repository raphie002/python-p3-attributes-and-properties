#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        name_error_message = "Name must be string between 1 and 25 characters."
        
        is_name_valid = False
        if isinstance(name, str) and (1 <= len(name) <= 25):
            is_name_valid = True
            self.name = name
        elif name is not None:
            print(name_error_message)
            self.name = None
        else:
            self.name = None
            
        breed_error_message = "Breed must be in list of approved breeds."
        
        if breed and breed not in APPROVED_BREEDS:
            print(breed_error_message)
            self.breed = None
        elif breed:
            self.breed = breed
        else:
            self.breed = None