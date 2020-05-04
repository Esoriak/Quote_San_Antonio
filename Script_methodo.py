# -*- coding: utf8 -*- 

#On affiche une information avec la fonction print()
#Pour passer à la ligne on peut écrire \n

print("Coucou c'est \n suspens...")




### TYPES D'OBJET
#Il existe plusieurs types d'objets.
#Les nombres : integer =>  nb entier ( 2, 4, 27) , float => nombre décimaux ( 1.2, 4.7; 27.34)
#les booléens : True or False, ils indiquent si une information est vrai ou fausse
#les string : chaîne de caractère, à mettre entre "" pour éviter d'échapper le caractère ' qui peut poser soucis. 
#les listes : ce sont des tableaux [], ils sont indéxés à 0.
#les tuples : c'est une liste de données immuables, aucune entrées ne pourra être modifiées. ( "un", "deux")
#les dictionnaires : Un dictionnaire en python est une sorte de liste mais au lieu d'utiliser des index , on utilise des clés alphanumériques.




#NUMBER METHOD



#is_integer est la plus classique elle permet de vérifier si un nombre est entier ou non

print((2.17).is_integer())

# x= number
#int(x) et float(x) peuvent convertir le type d'un nombre.




#STRING METHOD



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



#LIST METHOD

friends = [ "Monia", "Antho", "Kahina", "Said", "Mathilde", "Thomas", "Abdou", "Helder", "Bertrand", "Sandy"]

#index est une méthode qui prend en paramètre l'élèment recherché et renvoie l'index ou il se trouve
print(friends.index("Sandy"))

#append permet d'ajouter un élèment à la liste
friends.append("Manon")
print(friends)

#insert permer d'indiquer à quel index vous souhaiter ajouter un élèment
friends.insert(6, "Seb")
print(friends)

#pour modifier une valeur grâce à l'index :
friends[11] = "Marc"
print(friends)

#pop permet de supprimer le dernier élèment de la liste
friends.pop()
print(friends)

#remove permet de supprimer la première valeur trouvée qui correspond au paramètre
friends.remove("Said")
print(friends)




#DICT METHOD

So_family= {"husband": "Jf","Kids" : [ "Germaine"]}
print(So_family)

#update permet de mettre à jour une ou plusieurs valeurs en même temps
So_family.update({"husband" : "JF", "Kids" : ["Shelly-Ann"]} )
print(So_family)

#pop pour supprimer un élément
So_family.pop("husband")
print(So_family)

#pour ajouter un élément dans un dictionnaire
So_family["husband"] = "JF"
print(So_family)

#pour ajouter un élément  à une liste dans un dictionnaire
So_family.update({"Kids" : ["Shelly-Ann","Soann" ]})
print(So_family)