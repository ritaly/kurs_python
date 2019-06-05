def get_user_input():
    while True:
        print('--------------------------------------')
        try:
            id = int(input('Put here integer number: '))
            v = input('Example value: ')
            break
        except ValueError as e:
            print('Sorry,', e, 'Try again!')
    return id, v


def substitute_value(seq, id_val):
    """
    Method substitutes element in sequence
    with given value by given id
    """
    index, value = id_val  # rozpakowanie krotki

    try:
        seq[index] = value
    except TypeError:
        seq = list(seq)
        seq[index] = value

    return seq


def main():
    tv = ('FullHD', 1920, 'LCD/LED', 7.2, 'A++')

    data = get_user_input()
    new_tv = substitute_value(tv, data)

    print('Done: ', new_tv)


if __name__ == '__main__':
    main()
