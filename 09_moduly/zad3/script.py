# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import module_file as mf

def menu():
    x = input('1 - read from file\n2 - save to file\n')

    if x == '1':
        filename = input('File name or path to read:')
        content = mf.read_from_file(filename)
        print(content)
    elif x == '2':
        save_file = input('File name or path to save:')
        content = input('Write your content here: ')
        mf.save_to_file(save_file, content)
        print('Saved!')
    else:
        print("Wrong input")


def main():
    menu()


if __name__ == '__main__':
    main()
