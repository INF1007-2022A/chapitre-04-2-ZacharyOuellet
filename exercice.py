#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	return name.split("-")[0].capitalize()

def get_random_sentence(animals, adjectives, fruits):
	animal = animals[random.randint(0, len(animals)-1)]
	adjectif = adjectives[random.randint(0,len(adjectives)-1)]
	fruit = fruits[random.randint(0,len(fruits)-1)]
	return f"Aujourd’hui, j’ai vu un {animal} s’emparer d’un panier {adjectif} plein de {fruit}."

def encrypt(text, shift):
	""
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
