poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

words = {}

poem = poem.lower()
poem = poem.replace(',', '')
poem = poem.split()


for i in poem:
    if i in words.keys():
        words[i] += 1
    else:
        words[i] = 1

for key, value in words.items():
    print(key, " : ", value)
