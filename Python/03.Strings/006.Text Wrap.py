import textwrap

result = []

def wrap(string, max_width):
    start, end = 0, max_width    
    for _ in string:
        result.append(string[start:end])
        start += max_width
        end += max_width

    return "\n".join(result)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)