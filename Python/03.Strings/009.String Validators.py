if __name__ == '__main__':
    s = input()

    print(any([data.isalnum() for data in s]))
    print(any([data.isalpha() for data in s]))
    print(any([data.isdigit() for data in s]))
    print(any([data.islower() for data in s]))
    print(any([data.isupper() for data in s]))