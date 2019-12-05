if __name__ == '__main__':
    N = int(input())
    result = []

    for num in range(N):
        data = input().split(" ")
        content = data[0]
        
        if content == "insert":
            result.insert(int(data[1]), int(data[2]))
        if content == "append":
            result.append(int(data[1]))
        if content == "print":
            print(result)
        if content == "remove":
            result.remove(int(data[1]))
        if content == "sort":
            result = sorted(result)
        if content == "pop":
            result.pop()
        if content == "reverse":
            result.reverse()