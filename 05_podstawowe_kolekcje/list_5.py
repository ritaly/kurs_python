"""
5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

Dorota, Wellman, dziennikarka

Adam, Małysz, sportowiec

Robert, Lewandowski, piłkarz

Krystyna, Janda, aktorka

Wyświetl w sposób przyjazny dla użytkownika
"""

people = [
    ['Dorota', 'W', 'dzienn'],
    ['Adam', 'M', 'sport'],
    ['Robert', 'L', 'pilkarz']
]

# for i in people:
#     print(i)
#     print(i[0])


print(people[2][2])

# people = []
#
# for i in range(3):
#     name = input("podaje imie ")
#     surname = input("podaj nazwisko ")
#     job = input("podaje zawod ")
#     people.append([name, surname, job])

print(people)



for i in people:
    print('\t'.join(i))