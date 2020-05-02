# -*- coding: utf8 -*- 
#Définir une fonction qui permet de prendre des paramètres pour rendre l'affichage et le formatage dynamique

def create_message(character, quote):
  print( "{} a dit : {}".format(character, quote))

create_message(character="Le Génie", quote="Oui, Ali, oui c'est bien lui, Ali Ababoua ! A genoux, prosternez-vous, soyez ravis...")


#Split permet de créer un tableau en coupant une chaîne de caractère à chaque espace
my_credo = "your potentiel is infinite"

print(my_credo.split())

#Strip permet d'enlever les espaces d'une chaine de caractère
my_white_space = "       aaahhhh le silence est d'or ...               "

print(my_white_space.strip())

#Upper permet de mettre toutes les lettres en capitales

little_var = " i'm a little woman."

print(little_var.upper())

#Lower permet de mettre en minuscule toutes les lettres d'une chaîne de caractère

big_word = " WOW "

print(big_word)
print(big_word.lower())


#Capitalize permet de mettre une majuscule au premier mot d'une chaîne de caractère

hey = "hello world "

print(hey.capitalize())
