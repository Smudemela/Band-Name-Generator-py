from random import randint

welcome_banner = """
Welcome to the Random Band Name Generator!
Answer the prompts to generate your random band name.
"""
print(welcome_banner)

lead_singer_name = input("What is the Lead singer's first name? ")
music_adjective = input("Adjective describing the music: ")
plural_noun = input("A plural noun: ")
month = input("A month of the year: ")
verb = input("A verb ending in -ing ")
animal = input("A plural animal ")
color = input("A color ")
body_part = input("A body part ")

random_number = randint(0, 5)

if random_number == 0:
      band_name = f" {lead_singer_name} and the {plural_noun}"
if random_number == 1:
      band_name = f" Uptempo Pankcakes{music_adjective}"
if random_number == 2:
      band_name = f"Lowtempo Pancakes {plural_noun}"
if random_number == 3:
      band_name = f"{lead_singer_name} and {verb} {plural_noun}"
if random_number == 4:
      band_name = f"{color}, {plural_noun}"
  
print(f"Your random band name is ... {band_name}")

