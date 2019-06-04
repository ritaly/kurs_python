poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

#  poem - do takiej samej litery
#  poem - usunać znaki specjalne
#  poem - podzielic na wyrazy

poem = poem.lower()
poem = poem.replace(',', '')
poem = poem.split()

print(poem)
# pusty slownik
words = {}

# w pętli sprawdzic czy element istnieje w slowniku
# dodac element do slownika
for i in poem:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

# wyswietlanie

for k, v in words.items():
    print(k, '\t', v)
