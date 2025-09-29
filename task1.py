#lista med favorit filmer 

movies_list = ['Scarface', 'Rambo', 'Titanic']
# Lägg till en film med append()
movies_list.append('Seven')

print(movies_list)
for movie in movies_list:
    print(movie)
print("Första filmen:", movies_list[0])
print("Sista filmen:", movies_list[-1])