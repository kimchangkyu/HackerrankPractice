if __name__ == '__main__':
    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]

    result = [x for x in lis if x != max(lis)]

    print(max(result))
