def swap_case(s):
    s_list = [data.lower() if data.isupper() else data.upper() for data in s]
    return "".join(s_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)