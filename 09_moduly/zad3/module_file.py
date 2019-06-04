import os


def read_from_file(user_file):
    if os.path.isfile(user_file) and os.stat(user_file).st_size > 0:
        with open(user_file, 'r') as f:
            return f.read() #zwraca string
    else:
        print('Nie ma takiego pliku')
        return '' #pusty string - zwracamy ten sam typ


def save_to_file(user_file, user_data):
    with open(user_file, 'a') as f:
        f.write(user_data)
